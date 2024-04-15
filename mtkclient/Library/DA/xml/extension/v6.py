import os
import sys
from struct import unpack, pack
# from keystone import *
from mtkclient.config.payloads import pathconfig
from mtkclient.config.brom_config import efuse
from mtkclient.Library.error import ErrorHandler
from mtkclient.Library.Hardware.hwcrypto import crypto_setup, hwcrypto
from mtkclient.Library.utils import LogBase, progress, logsetup, find_binary
from mtkclient.Library.Hardware.seccfg import seccfgV3, seccfgV4
from mtkclient.Library.utils import mtktee
import json

rpmb_error = [
    "",
    "General failure",
    "Authentication failure",
    "Counter failure",
    "Address failure",
    "Write failure",
    "Read failure",
    "Authentication key not yet programmed"
]


class xmlflashext(metaclass=LogBase):
    def __init__(self, mtk, xmlflash, loglevel):
        self.pathconfig = pathconfig()
        self.__logger = logsetup(self, self.__logger, loglevel, mtk.config.gui)
        self.mtk = mtk
        self.loglevel = loglevel
        self.__logger = self.__logger
        self.eh = ErrorHandler()
        self.config = self.mtk.config
        self.usbwrite = self.mtk.port.usbwrite
        self.usbread = self.mtk.port.usbread
        self.echo = self.mtk.port.echo
        self.rbyte = self.mtk.port.rbyte
        self.rdword = self.mtk.port.rdword
        self.rword = self.mtk.port.rword
        self.xflash = xmlflash
        self.xsend = self.xflash.xsend
        self.xread = self.xflash.xread
        self.da2 = None
        self.da2address = None

    def patch_command(self, da2):
        self.da2address = self.xflash.daconfig.da_loader.region[2].m_start_addr  # at_address
        data = bytearray(da2)
        idx = data.find(b"\x00CMD:SET-HOST-INFO\x00")
        base = self.da2address
        if idx != -1:
            first_op, second_op = offset_to_op_mov(idx + 1, 0, base)
            first_op = int.to_bytes(first_op, 4, 'little')
            second_op = int.to_bytes(second_op, 4, 'little')
            midx = data.find(first_op)
            midx2 = data.find(second_op, midx)
            if midx + 8 == midx2:
                instr1 = int.from_bytes(data[midx + 4:midx + 8], 'little')
                instr2 = int.from_bytes(data[midx2 + 4:midx2 + 8], 'little')
                addr = op_mov_to_offset(instr1, instr2, 2) - base
                # rw_primitive = bytes.fromhex("FF412DE90040A0E30460A0E30C708DE20050A0E10710A0E1003090E508008DE200408" +
                # "DE506808DE004408DE508408DE50C608DE533FF2FE108309DE50710A0E10D00A0E10C608DE5040053E1003095E50A00001" +
                # "A33FF2FE100309DE50610A0E10C608DE50800A0E1003093E504308DE5043095E533FF2FE110D08DE2F081BDE833FF2FE10" +
                # "03095E50710A0E10800A0E10C608DE533FF2FE100309DE50400A0E104209DE5002083E5F2FFFFEA")
                # ks = Ks(KS_ARCH_ARM, KS_MODE_ARM + KS_MODE_LITTLE_ENDIAN)
                # content =
                """
                PUSH            {R4-R6,R10,R11,LR}
                ADD             R11, SP, #0x10
                MOV             R8, R0
                MOVW            R0, #0xF000
                MOVT            R0, #0x6800
                MOV             R1, #4
                LDR             R2, [R8]
                BLX             R2

                MOVW            R0, #0xF000
                MOVT            R0, #0x6800
                MOV             R1, [R0]
                MOVW            R0, #0x0000
                MOVT            R0, #0x6800
                LDR             R2, [R8]
                BLX             R2

                MOVW            R0, #0x0000
                MOVT            R0, #0x6800
                BLX             R0

                POP             {R4-R6,R10,R11,PC}
                """
                # encoding, length = ks.asm(content, addr=addr)
                # newdata = b"".join(int.to_bytes(val, 1, 'little') for val in encoding)

                newdata = bytes.fromhex(
                    "704c2de910b08de20080a0e100000fe3000846e30410a0e3002098e532ff2fe100000fe3000846e3000000e3000846e3002098e532ff2fe1000000e3000846e330ff2fe1708cbde8")
                sys.stdout.flush()
                data[addr:addr + len(newdata)] = newdata
                newcmd = b"CMD:CUSTOM\x00"
                data[idx + 1:idx + 1 + len(newcmd)] = newcmd
                return data
        return da2

    def ack(self):
        xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMACK")
        if self.xsend(xmlcmd):
            # result =
            self.xflash.get_response()
            # DATA data =
            self.xflash.get_response(raw=True)
            # CMD:END result =
            self.xflash.get_response()
            self.xflash.ack()
            # CMD:START result =
            self.xflash.get_response()
            self.xflash.ack()
            if data == b"\xA4\xA3\xA2\xA1":
                return True
        return False

    def patch(self):
        self.da2 = self.xflash.daconfig.da2
        self.da2address = self.xflash.daconfig.da_loader.region[2].m_start_addr  # at_address
        daextensions = os.path.join(self.pathconfig.get_payloads_path(), "da_xml.bin")
        if os.path.exists(daextensions):
            daextdata = bytearray(open(daextensions, "rb").read())
            register_ptr = daextdata.find(b"\x11\x11\x11\x11")
            mmc_get_card_ptr = daextdata.find(b"\x22\x22\x22\x22")
            mmc_set_part_config_ptr = daextdata.find(b"\x33\x33\x33\x33")
            mmc_rpmb_send_command_ptr = daextdata.find(b"\x44\x44\x44\x44")
            ufshcd_queuecommand_ptr = daextdata.find(b"\x55\x55\x55\x55")
            ufshcd_get_free_tag_ptr = daextdata.find(b"\x66\x66\x66\x66")
            ptr_g_ufs_hba_ptr = daextdata.find(b"\x77\x77\x77\x77")

            # register_xml_cmd("CMD:GET-SYS-PROPERTY", & a1, cmd_get_sys_property);

            # open("out" + hex(self.da2address) + ".da", "wb").write(da2)
            register_xml_cmd = find_binary(self.da2,
                                           b"\x70\x4C\x2D\xE9\x10\xB0\x8D\xE2\x00\x50\xA0\xE1\x14\x00\xA0\xE3")

            # UFS
            idx = self.da2.find(b"\x00\x00\x94\xE5\x34\x10\x90\xE5\x01\x00\x11\xE3\x03\x00\x00\x0A")
            g_ufs_hba = 0
            ufshcd_queuecommand = 0
            ufshcd_get_free_tag = 0
            if idx != -1:
                instr1 = int.from_bytes(self.da2[idx - 0x8:idx - 0x4], 'little')
                instr2 = int.from_bytes(self.da2[idx - 0x4:idx], 'little')
                g_ufs_hba = op_mov_to_offset(instr1, instr2, 4)
                ufshcd_queuecommand = find_binary(self.da2,
                                                  b"\xF0\x4D\x2D\xE9\x18\xB0\x8D\xE2\x08\xD0\x4D\xE2\x48\x40\x90\xE5")
                if ufshcd_queuecommand is None:
                    ufshcd_queuecommand = 0
                else:
                    ufshcd_queuecommand = ufshcd_queuecommand + self.da2address

                ufshcd_get_free_tag = find_binary(self.da2,
                                                  b"\x10\x4C\x2D\xE9\x08\xB0\x8D\xE2\x00\x40\xA0\xE3\x00\x00\x51\xE3")
                if ufshcd_get_free_tag is None:
                    ufshcd_get_free_tag = 0
                else:
                    ufshcd_get_free_tag = ufshcd_get_free_tag + self.da2address

            # EMMC

            mmc_get_card = find_binary(self.da2, b"\x90\x12\x20\xE0\x1E\xFF\x2F\xE1")
            if mmc_get_card is not None:
                mmc_get_card -= 0xC
            else:
                mmc_get_card = 0

            mmc_set_part_config = find_binary(self.da2, b"\xF0\x4B\x2D\xE9\x18\xB0\x8D\xE2\x23\xDE\x4D\xE2")
            if mmc_set_part_config is None:
                mmc_set_part_config = 0

            mmc_rpmb_send_command = find_binary(self.da2, b"\xF0\x48\x2D\xE9\x10\xB0\x8D\xE2\x08\x70\x9B\xE5")
            if mmc_rpmb_send_command is None:
                mmc_rpmb_send_command = 0

            #########################################
            if register_ptr != -1:
                if register_xml_cmd:
                    register_xml_cmd = register_xml_cmd + self.da2address
                else:
                    register_xml_cmd = 0

                # Patch the addr
                daextdata[register_ptr:register_ptr + 4] = pack("<I", register_xml_cmd)
                daextdata[mmc_get_card_ptr:mmc_get_card_ptr + 4] = pack("<I", mmc_get_card)
                daextdata[mmc_set_part_config_ptr:mmc_set_part_config_ptr + 4] = pack("<I", mmc_set_part_config)
                daextdata[mmc_rpmb_send_command_ptr:mmc_rpmb_send_command_ptr + 4] = pack("<I", mmc_rpmb_send_command)
                daextdata[ufshcd_get_free_tag_ptr:ufshcd_get_free_tag_ptr + 4] = pack("<I", ufshcd_get_free_tag)
                daextdata[ufshcd_queuecommand_ptr:ufshcd_queuecommand_ptr + 4] = pack("<I", ufshcd_queuecommand)
                daextdata[ptr_g_ufs_hba_ptr:ptr_g_ufs_hba_ptr + 4] = pack("<I", g_ufs_hba)

                # print(hexlify(daextdata).decode('utf-8'))
                # open("daext.bin","wb").write(daextdata)
                return daextdata
        return None

    def patch_da1(self, da1):
        pass

    def patch_da2(self, da2):
        self.info("Patching da2 ...")
        da2patched = bytearray(da2)
        pos = 0
        idx = 0
        while idx is not None:
            idx = find_binary(da2, b"\x00\x00\xA0\xE3\x04\x10\xA0\xE1\x00\x20\xA0\xE3..\x00\xEB\x01\x40\x00\xE3",
                              pos)
            if idx is not None:
                offset = int.from_bytes(da2patched[idx + 0xC:idx + 0xE], 'little') - 1
                da2patched[idx:idx + 0x14] = (b"\x00\x00\xA0\xE3\x04\x10\xA0\xE1\x2C\x22\x0E\xE3\x00\x20\x44\xE3" +
                                              offset.to_bytes(2, 'little') + b"\x00\xEB")
                patched = True
                pos += idx
            pos += 0x14
        if patched:
            self.info("Patched read_register / write_register")
        da2patched = self.patch_command(da2)

        idx = find_binary(da2patched,
                          b"\x00\xA0\xE3\x1E\xFF\x2F\xE1.\x00\xA0\xE3\x1E\xFF\x2F\xE1.\x00\xA0\xE3\x1E\xFF\x2F\xE1\x70\x4C")
        if idx is not None:
            da2patched[idx - 1:idx - 1 + (
                    3 * 8)] = b"\x01\x00\xA0\xE3\x1E\xFF\x2F\xE1\x01\x00\xA0\xE3\x1E\xFF\x2F\xE1\x01\x00\xA0\xE3\x1E\xFF\x2F\xE1"
            patched = True
            self.info("Patched write partitions / allow_read / allow_write")
        if not patched:
            self.warning("Write not allowed not patched.")
        return da2patched

    def custom_rpmb_read(self, sector, ufs=False):
        data = b''
        xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMRPMBR")
        if ufs:
            xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMURPMBR")
        if self.xsend(xmlcmd):
            result = self.xflash.get_response()
            if result == "OK":
                self.xsend(sector)
                resp = unpack("<H", self.xflash.get_response(raw=True))[0]
                if resp == 0x0:
                    data = self.xflash.get_response(raw=True)
                else:
                    self.error(rpmb_error[resp])
                # CMD:END
                result = self.xflash.get_response()
                self.xflash.ack()
                # CMD:START
                result = self.xflash.get_response()
                self.xflash.ack()
        return data

    def custom_rpmb_write(self, sector, data: bytes, ufs=False):
        if len(data) != 0x100:
            self.error("Incorrect rpmb frame length. Aborting")
            return False
        xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMRPMBW")
        if ufs:
            xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMURPMBW")
        if self.xsend(xmlcmd):
            result = self.xflash.get_response()
            if result == "OK":
                self.xsend(sector)
                self.xsend(data[:0x100])
                resp = unpack("<H", self.xflash.get_response(raw=True))[0]
                if resp != 0:
                    self.error(rpmb_error[resp])
                    # CMD:END
                    result = self.xflash.get_response()
                    self.xflash.ack()
                    # CMD:START
                    result = self.xflash.get_response()
                    self.xflash.ack()
                    return False
                # CMD:END
                result = self.xflash.get_response()
                self.xflash.ack()
                # CMD:START
                result = self.xflash.get_response()
                self.xflash.ack()
                return True
            # CMD:END
            result = self.xflash.get_response()
            self.xflash.ack()
            # CMD:START
            result = self.xflash.get_response()
            self.xflash.ack()
        return False

    def custom_rpmb_init(self):
        hwc = self.cryptosetup()
        if self.config.chipconfig.meid_addr:
            meid = self.config.get_meid()
            otp = self.config.get_otp()
            if meid != b"\x00" * 16:
                # self.config.set_meid(meid)
                self.info("Generating sej rpmbkey...")
                rpmbkey = hwc.aes_hwcrypt(mode="rpmb", data=meid, btype="sej", otp=otp)
                if rpmbkey is not None:
                    xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMRPMBKEY")
                    if self.xsend(xmlcmd):
                        result = self.xflash.get_response()
                        if result == "OK":
                            self.xsend(rpmbkey)
                            read_key = self.xflash.get_response(raw=True)
                            # CMD:END
                            result = self.xflash.get_response()
                            self.xflash.ack()
                            # CMD:START
                            result = self.xflash.get_response()
                            self.xflash.ack()
                            if rpmbkey == read_key:
                                self.info("Setting rpmbkey: ok")
        ufs = False
        if self.xflash.emmc.rpmb_size != 0:
            ufs = False
        elif self.xflash.ufs.block_size != 0:
            ufs = True
        xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMMMCINIT")
        if ufs:
            xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMUFSINIT")
        if self.xsend(xmlcmd):
            result = self.xflash.get_response()
            if result == "OK":
                derivedrpmb = self.xflash.get_response(raw=True)
                if int.from_bytes(derivedrpmb[:4], 'little') != 0xff:
                    # CMD:END
                    result = self.xflash.get_response()
                    self.xflash.ack()
                    # CMD:START
                    result = self.xflash.get_response()
                    self.xflash.ack()
                    self.info("Derived rpmb key:" + derivedrpmb.hex())
                    return True
            self.error("Failed to derive a valid rpmb key.")
        # CMD:END
        result = self.xflash.get_response()
        self.xflash.ack()
        # CMD:START
        result = self.xflash.get_response()
        self.xflash.ack()
        return False

    def setotp(self, hwc):
        otp = None
        if self.mtk.config.preloader is not None:
            idx = self.mtk.config.preloader.find(b"\x4D\x4D\x4D\x01\x30")
            if idx != -1:
                otp = self.mtk.config.preloader[idx + 0xC:idx + 0xC + 32]
        if otp is None:
            otp = 32 * b"\x00"
        hwc.sej.sej_set_otp(otp)

    def read_rpmb(self, filename=None, display=True):
        progressbar = progress(1, self.mtk.config.guiprogress)
        sectors = 0
        # val = self.custom_rpmb_init()
        ufs = False
        if self.xflash.emmc is not None:
            sectors = self.xflash.emmc.rpmb_size // 0x100
            ufs = False
        elif self.xflash.ufs.lu1_size != 0:
            sectors = (512 * 256)
            ufs = True
        if filename is None:
            filename = "rpmb.bin"
        if sectors > 0:
            with open(filename, "wb") as wf:
                for sector in range(sectors):
                    if display:
                        progressbar.show_progress("RPMB read", sector * 0x100, sectors * 0x100, display)
                    data = self.custom_rpmb_read(sector=sector, ufs=ufs)
                    if data == b"":
                        self.error("Couldn't read rpmb.")
                        return False
                    wf.write(data)
            self.info("Done reading rpmb to " + filename)
            return True
        return False

    def write_rpmb(self, filename=None, display=True):
        progressbar = progress(1, self.mtk.config.guiprogress)
        if filename is None:
            self.error("Filename has to be given for writing to rpmb")
            return False
        if not os.path.exists(filename):
            self.error(f"Couldn't find {filename} for writing to rpmb.")
            return False
        ufs = False
        sectors = 0
        if self.xflash.emmc.rpmb_size != 0:
            sectors = self.xflash.emmc.rpmb_size // 0x100
        elif self.xflash.ufs.block_size != 0:
            sectors = (512 * 256)
        if self.custom_rpmb_init():
            if sectors > 0:
                with open(filename, "rb") as rf:
                    for sector in range(sectors):
                        if display:
                            progressbar.show_progress("RPMB written", sector * 0x100, sectors * 0x100, display)
                        if not self.custom_rpmb_write(sector=sector, data=rf.read(0x100), ufs=ufs):
                            self.error(f"Couldn't write rpmb at sector {sector}.")
                            return False
                self.info(f"Done reading writing {filename} to rpmb")
                return True
        return False

    def erase_rpmb(self, display=True):
        progressbar = progress(1, self.mtk.config.guiprogress)
        ufs = False
        sectors = 0
        if self.xflash.emmc.rpmb_size != 0:
            sectors = self.xflash.emmc.rpmb_size // 0x100
        elif self.xflash.ufs.block_size != 0:
            sectors = (512 * 256)
        if self.custom_rpmb_init():
            if sectors > 0:
                for sector in range(sectors):
                    if display:
                        progressbar.show_progress("RPMB erased", sector * 0x100, sectors * 0x100, display)
                    if not self.custom_rpmb_write(sector=sector, data=b"\x00" * 0x100, ufs=ufs):
                        self.error(f"Couldn't erase rpmb at sector {sector}.")
                        return False
                self.info("Done erasing rpmb")
                return True
        return False

    def custom_read(self, addr, length) -> bytes:
        xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMMEMR")
        if self.xsend(xmlcmd):
            result = self.xflash.get_response()
            if result == "OK":
                # DATA
                self.xsend(data=addr, is64bit=True)
                self.xsend(length)
                data = self.xflash.get_response(raw=True)
                # CMD:END
                result = self.xflash.get_response()
                self.xflash.ack()
                # CMD:START
                result = self.xflash.get_response()
                self.xflash.ack()
                return data
        return b""

    def custom_read_reg(self, addr: int, length: int) -> bytes:
        data = bytearray()
        for pos in range(addr, addr + length, 4):
            tmp = self.custom_readregister(pos)
            if tmp == b"":
                break
            data.extend(tmp.to_bytes(4, 'little'))
        return data

    def custom_readregister(self, addr) -> (int, None):
        xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMREGR")
        if self.xsend(xmlcmd):
            result = self.xflash.get_response()
            if result == "OK":
                # DATA
                self.xsend(data=addr)
                data = self.xflash.get_response(raw=True)
                # CMD:END
                result = self.xflash.get_response()
                self.xflash.ack()
                # CMD:START
                result = self.xflash.get_response()
                self.xflash.ack()
                return int.from_bytes(data, 'little')
        return None

    def custom_write(self, addr, data) -> bool:
        xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMMEMR")
        if self.xsend(xmlcmd):
            result = self.xflash.get_response()
            if result == "OK":
                # DATA
                self.xsend(data=addr, is64bit=True)
                self.xsend(len(data))
                self.xsend(data)
                # CMD:END
                result = self.xflash.get_response()
                self.xflash.ack()
                # CMD:START
                result = self.xflash.get_response()
                self.xflash.ack()
                return True
        return False

    def custom_writeregister(self, addr: int, data: int):
        xmlcmd = self.xflash.Cmd.create_cmd("CUSTOMREGW")
        if self.xsend(xmlcmd):
            result = self.xflash.get_response()
            if result == "OK":
                # DATA
                self.xsend(addr)
                self.xsend(data)
                # CMD:END
                result = self.xflash.get_response()
                self.xflash.ack()
                # CMD:START
                result = self.xflash.get_response()
                self.xflash.ack()
                return True
        return False

    def readmem(self, addr, dwords=1):
        res = []
        if dwords < 0x20:
            for pos in range(dwords):
                val = self.custom_readregister(addr + pos * 4)
                if val == b"":
                    return False
                if dwords == 1:
                    self.debug(f"RX: {hex(addr + (pos * 4))} -> " + hex(val))
                    return val
                res.append(val)
        else:
            res = self.custom_read(addr, dwords * 4)
            res = [unpack("<I", res[i:i + 4])[0] for i in range(0, len(res), 4)]

        self.debug(f"RX: {hex(addr)} -> " + bytearray(b"".join(pack("<I", val) for val in res)).hex())
        return res

    def writeregister(self, addr, dwords):
        if isinstance(dwords, int):
            dwords = [dwords]
        pos = 0
        if len(dwords) < 0x20:
            for val in dwords:
                self.debug(f"TX: {hex(addr + pos)} -> " + hex(val))
                if not self.custom_writeregister(addr + pos, val):
                    return False
                pos += 4
        else:
            dat = b"".join([pack("<I", val) for val in dwords])
            self.custom_write(addr, dat)
        return True

    def writemem(self, addr, data):
        for i in range(0, len(data), 4):
            value = data[i:i + 4]
            while len(value) < 4:
                value += b"\x00"
            self.writeregister(addr + i, unpack("<I", value))
        return True

    def cryptosetup(self):
        setup = crypto_setup()
        setup.blacklist = self.config.chipconfig.blacklist
        setup.gcpu_base = self.config.chipconfig.gcpu_base
        setup.dxcc_base = self.config.chipconfig.dxcc_base
        setup.efuse_base = self.config.chipconfig.efuse_addr
        setup.da_payload_addr = self.config.chipconfig.da_payload_addr
        setup.sej_base = self.config.chipconfig.sej_base
        setup.read32 = self.readmem
        setup.write32 = self.writeregister
        setup.writemem = self.writemem
        setup.hwcode = self.config.hwcode
        return hwcrypto(setup, self.loglevel, self.config.gui)

    def seccfg(self, lockflag):
        if lockflag not in ["unlock", "lock"]:
            return False, "Valid flags are: unlock, lock"
        data, guid_gpt = self.xflash.partition.get_gpt(self.mtk.config.gpt_settings, "user")
        seccfg_data = None
        partition = None
        if guid_gpt is None:
            return False, "Error getting the partition table."
        for rpartition in guid_gpt.partentries:
            if rpartition.name == "seccfg":
                partition = rpartition
                seccfg_data = self.xflash.readflash(
                    addr=partition.sector * self.mtk.daloader.daconfig.pagesize,
                    length=partition.sectors * self.mtk.daloader.daconfig.pagesize,
                    filename="", parttype="user", display=False)
                break
        if seccfg_data is None:
            return False, "Couldn't detect existing seccfg partition. Aborting unlock."
        if seccfg_data[:4] != pack("<I", 0x4D4D4D4D):
            return False, "Unknown seccfg partition header. Aborting unlock."
        hwc = self.cryptosetup()
        if seccfg_data[:0xC] == b"AND_SECCFG_v":
            self.info("Detected V3 Lockstate")
            sc_org = seccfgV3(hwc, self.mtk)
        elif seccfg_data[:4] == b"\x4D\x4D\x4D\x4D":
            self.info("Detected V4 Lockstate")
            sc_org = seccfgV4(hwc, self.mtk)
        else:
            return False, "Unknown lockstate or no lockstate"
        if not sc_org.parse(seccfg_data):
            return False, "Device has is either already unlocked or algo is unknown. Aborting."
        ret, writedata = sc_org.create(lockflag=lockflag)
        if ret is False:
            return False, writedata
        if self.xflash.writeflash(addr=partition.sector * self.mtk.daloader.daconfig.pagesize,
                                  length=len(writedata),
                                  filename=None, wdata=writedata, parttype="user", display=True):
            return True, "Successfully wrote seccfg."
        return False, "Error on writing seccfg config to flash."

    def decrypt_tee(self, filename="tee1.bin", aeskey1: bytes = None, aeskey2: bytes = None):
        hwc = self.cryptosetup()
        with open(filename, "rb") as rf:
            data = rf.read()
            idx = 0
            while idx != -1:
                idx = data.find(b"EET KTM ", idx + 1)
                if idx != -1:
                    mt = mtktee()
                    mt.parse(data[idx:])
                    rdata = hwc.mtee(data=mt.data, keyseed=mt.keyseed, ivseed=mt.ivseed,
                                     aeskey1=aeskey1, aeskey2=aeskey2)
                    open("tee_" + hex(idx) + ".dec", "wb").write(rdata)

    def read_fuse(self, idx):
        if self.mtk.config.chipconfig.efuse_addr is not None:
            base = self.mtk.config.chipconfig.efuse_addr
            hwcode = self.mtk.config.hwcode
            efuseconfig = efuse(base, hwcode)
            addr = efuseconfig.efuses[idx]
            if addr < 0x1000:
                return int.to_bytes(addr, 4, 'little')
            data = bytearray(self.mtk.daloader.peek_reg(addr=addr, length=4))
            return data
        return None

    def read_pubk(self):
        if self.mtk.config.chipconfig.efuse_addr is not None:
            base = self.mtk.config.chipconfig.efuse_addr
            addr = base + 0x90
            data = bytearray(self.mtk.daloader.peek_reg(addr=addr, length=0x20))
            return data
        return None

    def readfuses(self):
        if self.mtk.config.chipconfig.efuse_addr is not None:
            base = self.mtk.config.chipconfig.efuse_addr
            hwcode = self.mtk.config.hwcode
            efuseconfig = efuse(base, hwcode)
            data = []
            for idx in range(len(efuseconfig.efuses)):
                addr = efuseconfig.efuses[idx]
                if addr < 0x1000:
                    return data.append(int.to_bytes(addr, 4, 'little'))
                else:
                    data.append(bytearray(self.mtk.daloader.peek(addr=addr, length=4)))
            return data

    def generate_keys(self):
        if self.config.hwcode in [0x2601, 0x6572]:
            base = 0x11141000
        elif self.config.hwcode == 0x6261:
            base = 0x70000000
        elif self.config.hwcode in [0x8172, 0x8176]:
            base = 0x122000
        else:
            base = 0x100000
        if self.config.meid is None:
            try:
                data = b"".join([pack("<I", val) for val in self.readmem(base + 0x8EC, 0x16 // 4)])
                self.config.meid = data
                self.config.set_meid(data)
            except Exception:
                return
        if self.config.socid is None:
            try:
                data = b"".join([pack("<I", val) for val in self.readmem(base + 0x934, 0x20 // 4)])
                self.config.socid = data
                self.config.set_socid(data)
            except Exception:
                return
        hwc = self.cryptosetup()
        meid = self.config.get_meid()
        socid = self.config.get_socid()
        hwcode = self.config.get_hwcode()
        cid = self.config.get_cid()
        otp = self.config.get_otp()
        retval = {}
        # data=hwc.aes_hwcrypt(data=bytes.fromhex("A9 E9 DC 38 BF 6B BD 12 CC 2E F9 E6 F5 65 E8 C6 88 F7 14 11 80 2E 4D 91 8C 2B 48 A5 BB 03 C3 E5"), mode="sst", btype="sej",
        #                encrypt=False)
        # self.info(data.hex())
        pubk = self.read_pubk()
        if pubk is not None:
            retval["pubkey"] = pubk.hex()
            self.info("PUBK        : " + pubk.hex())
            self.config.hwparam.writesetting("pubkey", pubk.hex())
        if meid is not None:
            self.info("MEID        : " + meid.hex())
            retval["meid"] = meid.hex()
            self.config.hwparam.writesetting("meid", meid.hex())
        if socid is not None:
            self.info("SOCID       : " + socid.hex())
            retval["socid"] = socid.hex()
            self.config.hwparam.writesetting("socid", socid.hex())
        if hwcode is not None:
            self.info("HWCODE      : " + hex(hwcode))
            retval["hwcode"] = hex(hwcode)
            self.config.hwparam.writesetting("hwcode", hex(hwcode))
        if cid is not None:
            self.info("CID         : " + cid)
            retval["cid"] = cid
        if self.config.chipconfig.dxcc_base is not None:
            self.info("Generating dxcc rpmbkey...")
            rpmbkey = hwc.aes_hwcrypt(btype="dxcc", mode="rpmb")
            self.info("Generating dxcc mirpmbkey...")
            mirpmbkey = hwc.aes_hwcrypt(btype="dxcc", mode="mirpmb")
            self.info("Generating dxcc fdekey...")
            fdekey = hwc.aes_hwcrypt(btype="dxcc", mode="fde")
            self.info("Generating dxcc rpmbkey2...")
            rpmb2key = hwc.aes_hwcrypt(btype="dxcc", mode="rpmb2")
            self.info("Generating dxcc km key...")
            ikey = hwc.aes_hwcrypt(btype="dxcc", mode="itrustee", data=self.config.hwparam.appid)
            # self.info("Generating dxcc platkey + provkey key...")
            # platkey, provkey = hwc.aes_hwcrypt(btype="dxcc", mode="prov")
            # self.info("Provkey     : " + provkey.hex())
            # self.info("Platkey     : " + platkey.hex())
            if mirpmbkey is not None:
                self.info("MIRPMB      : " + mirpmbkey.hex())
                self.config.hwparam.writesetting("mirpmbkey", mirpmbkey.hex())
                retval["mirpmbkey"] = mirpmbkey.hex()
            if rpmbkey is not None:
                self.info("RPMB        : " + rpmbkey.hex())
                self.config.hwparam.writesetting("rpmbkey", rpmbkey.hex())
                retval["rpmbkey"] = rpmbkey.hex()
            if rpmb2key is not None:
                self.info("RPMB2       : " + rpmb2key.hex())
                self.config.hwparam.writesetting("rpmb2key", rpmb2key.hex())
                retval["rpmb2key"] = rpmb2key.hex()
            if fdekey is not None:
                self.info("FDE         : " + fdekey.hex())
                self.config.hwparam.writesetting("fdekey", fdekey.hex())
                retval["fdekey"] = fdekey.hex()
            if ikey is not None:
                self.info("iTrustee    : " + ikey.hex())
                self.config.hwparam.writesetting("kmkey", ikey.hex())
                retval["kmkey"] = ikey.hex()
            if self.config.chipconfig.prov_addr:
                provkey = self.custom_read(self.config.chipconfig.prov_addr, 16)
                self.info("PROV        : " + provkey.hex())
                self.config.hwparam.writesetting("provkey", provkey.hex())
                retval["provkey"] = provkey.hex()

            val = self.read_fuse(0xC)
            if val is not None:
                val += self.read_fuse(0xD)
                val += self.read_fuse(0xE)
                val += self.read_fuse(0xF)
                self.info("HRID        : " + val.hex())
                self.config.hwparam.writesetting("hrid", val.hex())
                retval["hrid"] = val.hex()

            if hwcode == 0x699 and self.config.chipconfig.sej_base is not None:
                mtee3 = hwc.aes_hwcrypt(mode="mtee3", btype="sej")
                if mtee3:
                    self.config.hwparam.writesetting("mtee3", mtee3.hex())
                    self.info("MTEE3       : " + mtee3.hex())
                    retval["mtee3"] = mtee3.hex()
            return retval
        elif self.config.chipconfig.sej_base is not None:
            if os.path.exists("tee.json"):
                val = json.loads(open("tee.json", "r").read())
                self.decrypt_tee(val["filename"], bytes.fromhex(val["data"]), bytes.fromhex(val["data2"]))
            if meid == b"":
                meid = self.custom_read(0x1008ec, 16)
            if meid != b"":
                # self.config.set_meid(meid)
                self.info("Generating sej rpmbkey...")
                self.setotp(hwc)
                rpmbkey = hwc.aes_hwcrypt(mode="rpmb", data=meid, btype="sej", otp=otp)
                if rpmbkey:
                    self.info("RPMB        : " + rpmbkey.hex())
                    self.config.hwparam.writesetting("rpmbkey", rpmbkey.hex())
                    retval["rpmbkey"] = rpmbkey.hex()
                self.info("Generating sej mtee...")
                mtee = hwc.aes_hwcrypt(mode="mtee", btype="sej", otp=otp)
                if mtee:
                    self.config.hwparam.writesetting("mtee", mtee.hex())
                    self.info("MTEE        : " + mtee.hex())
                    retval["mtee"] = mtee.hex()
                mtee3 = hwc.aes_hwcrypt(mode="mtee3", btype="sej", otp=otp)
                if mtee3:
                    self.config.hwparam.writesetting("mtee3", mtee3.hex())
                    self.info("MTEE3       : " + mtee3.hex())
                    retval["mtee3"] = mtee3.hex()
            else:
                self.info("SEJ Mode: No meid found. Are you in brom mode ?")
        if self.config.chipconfig.gcpu_base is not None:
            if self.config.hwcode in [0x335, 0x8167, 0x8163, 0x8176]:
                self.info("Generating gcpu mtee2 key...")
                mtee2 = hwc.aes_hwcrypt(btype="gcpu", mode="mtee")
                if mtee2 is not None:
                    self.info("MTEE2       : " + mtee2.hex())
                    self.config.hwparam.writesetting("mtee2", mtee2.hex())
                    retval["mtee2"] = mtee2.hex()
        return retval


def offset_to_op_mov(addr, register, base):
    offset = addr + base
    low = (((offset & 0xFFFF) >> 12) & 0xF) << 16 | (register << 14) | offset & 0xFFF
    offset = (offset >> 16)
    shift = 4
    high = (((offset & 0xFFFF) >> 12) & 0xF) << 16 | (register << 14) | offset & 0xFFF | (shift << 20)
    first_op = (0xE3 << 24) + low
    second_op = (0xE3 << 24) + high
    return first_op, second_op


def op_mov_to_offset(first_op, second_op, register):
    reglo = (first_op & 0xF000) >> 12
    reghi = (second_op & 0xF000) >> 12
    shiftlo = (first_op & 0xF00000) >> 20
    shifthi = (second_op & 0xF00000) >> 20
    hi = ((second_op & 0xF0000) >> 4 | second_op & 0xFFF) << shifthi * 4
    lo = ((first_op & 0xF0000) >> 4 | first_op & 0xFFF) << shiftlo * 4
    if reglo == reghi == register:
        return hi | lo
    return None


if __name__ == "__main__":
    with open("/home/bjk/Projects/mtkclient_github/Research/new_loaders/MT6789_oppo_realme_10/normal/da2_40000000.bin",
              "rb") as rf:
        data = bytearray(rf.read())
        idx = data.find(b"\x00\x00\x94\xE5\x34\x10\x90\xE5\x01\x00\x11\xE3\x03\x00\x00\x0A")
        base = 0x40000000
        if idx != -1:
            instr1 = int.from_bytes(data[idx - 0x8:idx - 0x4], 'little')
            instr2 = int.from_bytes(data[idx - 0x4:idx], 'little')
            g_ufs_ptr = op_mov_to_offset(instr1, instr2, 4)
