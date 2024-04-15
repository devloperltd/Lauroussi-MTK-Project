#!/usr/bin/python3
# -*- coding: utf-8 -*-
# (c) B.Kerler 2018-2023

try:
    from mtkclient.Library.utils import LogBase, structhelper
except Exception:
    from utils import LogBase, structhelper


class pmt(metaclass=LogBase):
    class pt_resident:
        def __init__(self, data):
            sh = structhelper(data)
            self.name = sh.bytes(64)
            self.size = sh.qword()
            self.part_id = sh.qword()
            self.offset = sh.qword()
            self.mask_flags = sh.qword()

    class pt_info:
        def __init__(self, data):
            sh = structhelper(data)
            self.sequencenumber = sh.bytes(1)
            self.tool_or_sd_update = sh.bytes(1)
            tmp = sh.bytes(1)
            self.mirror_pt_dl = (tmp >> 4) & 0xF
            self.mirror_pt_has_space = tmp & 0xF
            tmp = sh.bytes(1)
            self.pt_changed = (tmp >> 4) & 0xF
            self.pt_has_space = tmp & 0xF

    class pmt_header:
        def __init__(self, data):
            sh = structhelper(data)
            self.signature = sh.bytes(8)
            self.revision = sh.dword()
            self.header_size = sh.dword()
            self.crc32 = sh.dword()
            self.reserved = sh.dword()
            self.current_lba = sh.qword()
            self.backup_lba = sh.qword()
            self.first_usable_lba = sh.qword()
            self.last_usable_lba = sh.qword()
            self.disk_guid = sh.bytes(16)
            self.part_entry_start_lba = sh.qword()
            self.num_part_entries = sh.dword()
            self.part_entry_size = sh.dword()
