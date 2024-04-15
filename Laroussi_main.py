#!/usr/bin/env python3.12.1
# T-REX Tool (c) Laroussi.Boulanouar, G.Kreileman 2024
# Based of MTK Flash Client (c) B.Kerler 2018-2023 GPLv3 License
# Licensed under GPLv3 License.
import sys
import os
import time
import mock
import threading
import logging
import subprocess
from functools import partial

from PySide6.QtCore import Qt,Signal, QTimer, Signal, QObject, QTranslator, QLocale, QLibraryInfo, \
    Slot, QCoreApplication
from PySide6.QtGui import QTextDocument, QTextOption, QPixmap, QTextCharFormat, QFont, QColor, QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QListWidgetItem, QMessageBox, QLayout, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QCheckBox, QVBoxLayout, QHBoxLayout, QLineEdit, \
                            QPushButton

from mtkclient.Library.mtk import Mtk
from mtkclient.Library.DA.mtk_da_handler import DA_handler
from mtkclient.Library.gpt import gpt_settings
from mtkclient.Library.mtk_main import Main, Mtk_Config

from mtkclient.gui.readFlashPartitions import ReadFlashWindow
from mtkclient.gui.writeFlashPartitions import WriteFlashWindow
from mtkclient.gui.eraseFlashPartitions import EraseFlashWindow
from mtkclient.gui.toolkit import asyncThread, trap_exc_during_debug, convert_size, CheckBox, FDialog, TimeEstim
from mtkclient.config.payloads import pathconfig
from ui_Hatem_gui import Ui_MainWindow
from ui_Testpoint import Ui_T_point_Window


lock = threading.Lock()

os.environ['QT_MAC_WANTS_LAYER'] = '1'  # This fixes a bug in pyside2 on MacOS Big Sur
# TO do Move all GUI modifications to signals!
# install exception hook: without this, uncaught exception would cause application to exit
sys.excepthook = trap_exc_during_debug

# Initiate MTK classes
variables = mock.Mock()
variables.cmd = "stage"
variables.debugmode = True
path = pathconfig()
# if sys.platform.startswith('darwin'):
#    config.ptype = "kamakiri" #Temp for Mac testing
MtkTool = Main(variables)

guiState = "welcome"
phoneInfo = {"chipset": "", "bootMode": "", "daInit": False, "cdcInit": False}

class DeviceHandler(QObject):
    sendToLogSignal = Signal(str)
    update_status_text = Signal(str)
    sendToProgressSignal = Signal(int)
    da_handler = None

    def __init__(self, parent, preloader: str = None, loglevel=logging.INFO, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        config = Mtk_Config(loglevel=logging.INFO, gui=self.sendToLogSignal, guiprogress=self.sendToProgressSignal,
                            update_status_text=self.update_status_text)
        config.gpt_settings = gpt_settings(gpt_num_part_entries='0', gpt_part_entry_size='0',
                                           gpt_part_entry_start_lba='0')  # This actually sets the right GPT settings..
        config.reconnect = True
        config.uartloglevel = 2
        self.loglevel = logging.DEBUG
        self.da_handler = DA_handler(Mtk(config=config, loglevel=logging.INFO), loglevel)

def getDevInfo(self, parameters):
    # loglevel = parameters[0]
    phoneInfo = parameters[1]
    devhandler = parameters[2]

    mtkClass = devhandler.da_handler.mtk
    try:
        if not mtkClass.port.cdc.connect():
            mtkClass.preloader.init()
        else:
            phoneInfo['cdcInit'] = True
    except Exception:
        phoneInfo['cantConnect'] = True
    phoneInfo['chipset'] = (str(mtkClass.config.chipconfig.name) + " (" + str(mtkClass.config.chipconfig.description) +
                            ")")
    self.sendUpdateSignal.emit()

def AuthBypass(self, parameters):
    #loglevel = parameters[0]
    phoneInfo = parameters[1]
    devhandler = parameters[2]

    mtkClass = devhandler.da_handler.mtk
    da_handler = devhandler.da_handler

    mtkClass = da_handler.configure_da(mtkClass, preloader=None)
    if mtkClass:
        phoneInfo['daInit'] = True
        phoneInfo['chipset'] = (str(mtkClass.config.chipconfig.name) + " (" +
                                str(mtkClass.config.chipconfig.description) + ")")
        if mtkClass.config.is_brom:
            phoneInfo['bootMode'] = "Bootrom mode"
        elif mtkClass.config.chipconfig.damode:
            phoneInfo['bootMode'] = "DA mode"
        else:
            phoneInfo['bootMode'] = "Preloader mode"
        self.sendUpdateSignal.emit()
    else:
        phoneInfo['cantConnect'] = True
        self.sendUpdateSignal.emit()

def check_device(self, parameters):
    devhandler = parameters[0]

    mtkClass = devhandler.da_handler.mtk
    da_handler = devhandler.da_handler

    mtkClass = da_handler.configure_da(mtkClass, preloader=None)

def load_translations(application):
    # Load application translations and the QT base translations for the current locale
    locale = QLocale.system()
    translator = QTranslator(application)
    directory = os.path.dirname(__file__)
    lang = 'mtkclient/gui/i18n/' + locale.name()
    if locale.name() == "en_NL":
        lang = lang.replace("en_NL", "nl_NL")
    # lang = 'mtkclient/gui/i18n/fr_FR'
    # lang = 'mtkclient/gui/i18n/de_DE'
    # lang = 'mtkclient/gui/i18n/en_GB'
    # lang = 'mtkclient/gui/i18n/es_ES'
    if translator.load(lang, directory):
        application.installTranslator(translator)

    translations_path = QLibraryInfo.path(QLibraryInfo.TranslationsPath)
    base_translator = QTranslator(application)
    if base_translator.load(locale, "qtbase", "_", translations_path):
        application.installTranslator(base_translator)


def execute_command(command):
    subprocess.run(command)


class MainWindow(QMainWindow):
    startGetDevInfoSignal = Signal(list)
    exitSignal = Signal()
    # Add a new signal for canceling the progress
    cancelProgressSignal = Signal()    

    # Class variable to store the color for the canceled message
    Red_color = QColor(231, 76, 60)  # Red color
    Green_color = QColor(0, 255, 0)  # Green color
    Bleu_color = QColor(0, 102, 255)  # Bleu color
    Orenge_color = QColor(241, 196, 15)  # Orenge color

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fdialog = FDialog(self)
        self.Status = {}
        self.timeEst = TimeEstim()
        self.timeEstTotal = TimeEstim()        

        self.devhandler = None
        self.readflash = None

        # Set Default Home Page
        self.Home_tab()
        self.Handel_Button()
        self.Handel_log_tab()

        self.process = None  # Initialize process as None
        # Connect Start_BTN click event to the handle_start_button method
        self.ui.Start_BTN.clicked.connect(self.handle_start_button)
        # Connect Start_BTN click event to the handle_stop_button method
        self.ui.Stop_BTN.clicked.connect(self.handle_stop_button)
        # Connect Open_Devmgmt click event to open Device Manager
        self.ui.Open_Devmgmt.clicked.connect(self.open_devmgmt)

        self.ui.TestPoints.clicked.connect(self.Test_point)

        # Assing Exit Button
        self.ui.Exit_Button.clicked.connect(self.close)
        # Remove Windows Default Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Set Custom Navigation Bar
        self.ui.Menu_Frame.mouseMoveEvent = self.MoveWindow
        # Assing Minimize Button
        self.ui.Minimize_Button.clicked.connect(self.showMinimized)

        # Customized tableWidget
        self.ui.readpartitionList.setColumnWidth(0, 10)
        self.ui.Checkpartitionsbtn.clicked.connect(self.readpartition)

        self.log_instructions = [
            "1 - ► Make sure device is powered off.\n",
            "2 - ► Power off, if needed. Wait 20 seconds after\n",
            "2 - ► Hold VOL (+) And VOL (-) Then Insert Usb Cable\n",
            "2 - ► Insert USB cable in phone\n",
            "3 - ► Phone Must have a battery inside!\n",
        ]

        # Create a QTimer instance
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_next_instruction)

    def Handel_Button(self):
        #self.ui.tabWidget.tabBar().setVisible(False)
        self.ui.Home_Btn.clicked.connect(self.Home_tab)
        self.ui.MediaTek_Btn.clicked.connect(self.MediaTek_tab)
        self.ui.Huawei_Btn.clicked.connect(self.Huawei_tab)
        self.ui.Qualcomm_Btn.clicked.connect(self.Qualcomm_tab)
        self.ui.Samsung_Btn.clicked.connect(self.Samsung_tab)
        self.ui.Android_Btn.clicked.connect(self.Android_tab)
        self.ui.About_Btn.clicked.connect(self.About_tab)

    def Home_tab(self):
        self.ui.Container_tab.setCurrentIndex(0)
    def MediaTek_tab(self):        
        self.ui.Container_tab.setCurrentIndex(1)
    def Huawei_tab(self):        
        self.ui.Container_tab.setCurrentIndex(2)
    def Qualcomm_tab(self):        
        self.ui.Container_tab.setCurrentIndex(3)
    def Samsung_tab(self):        
        self.ui.Container_tab.setCurrentIndex(4)
    def Android_tab(self):        
        self.ui.Container_tab.setCurrentIndex(5)
    def About_tab(self):        
        self.ui.Container_tab.setCurrentIndex(6)

    def Handel_log_tab(self):
        self.ui.SignUp_Button.clicked.connect(self.registration)
        self.ui.back2Login_Button_2.clicked.connect(self.login)
        self.ui.back2Login_Button.clicked.connect(self.login)
        self.ui.Forget_Pass_Button.clicked.connect(self.forget_pass)

    def login(self):
        self.ui.log_win_tab.setCurrentIndex(0)
        
    def registration(self):
        self.ui.log_win_tab.setCurrentIndex(1)

    def forget_pass(self):
        self.ui.log_win_tab.setCurrentIndex(2)


    def show_next_instruction(self):
        if self.current_instruction_index < len(self.log_instructions):
            instruction = self.log_instructions[self.current_instruction_index]
            cursor = self.ui.logBox.textCursor()

            # Create a QTextCharFormat instance
            format = QTextCharFormat()
            format.setFontPointSize(10)  # Set the font size (you can adjust as needed)
            format.setFontWeight(QFont.Bold)  # Set the font weight to Normal

            # Move the cursor to the end of the text and apply the format
            cursor.movePosition(QTextCursor.End)
            cursor.insertText(instruction, format)

            # Move the cursor to the end again to preserve the formatting for the next instruction
            cursor.movePosition(QTextCursor.End)

            self.current_instruction_index += 1
        else:
            # All instructions have been displayed, stop the timer
            self.timer.stop()

    def MoveWindow(self, event):
        if not self.isMaximized():
            self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()

    # Show Test point Window
    def Test_point(self):
        self.Show_T_point = T_point_Window() 
        self.Show_T_point.show()



    def handle_start_button(self):
        # Clear the logBox before appending new messages
        self.ui.logBox.clear()
        if self.ui.read_info_radioButton.isChecked():
            
            # Insert the unformatted text
            R_info = self.ui.read_info_radioButton.text()
            operation_message = f"SELECTED OPERATION : {R_info}\t\n\n"

            # Append the operation message without the applied format
            self.ui.logBox.setPlainText(operation_message)

            # Set the color for the "operation message" message
            cursor = self.ui.logBox.textCursor()
            format = QTextCharFormat()
            format.setForeground(self.Green_color)  # Use Green color
            format.setFontPointSize(13)  # Set font size to 12 (you can adjust the 
            format.setFontWeight(QFont.Bold)  # Set font weight to Bold
            try:
                cursor.setPosition(self.ui.logBox.toPlainText().index(operation_message))
                cursor.movePosition(QTextCursor.EndOfBlock, QTextCursor.KeepAnchor)
                cursor.mergeCharFormat(format)
            except ValueError:
                # Handle the case when substring is not found
                pass

            # Start the timer to display instructions one by one
            self.current_instruction_index = 0
            self.timer.start(300)  # Adjust the timeout interval as needed
    
            loglevel = logging.INFO
            devhandler = DeviceHandler(parent=app, preloader=None, loglevel=loglevel)
            devhandler.sendToLogSignal.connect(self.sendToLog)

            # Get the device info asynchronously
            self.thread = asyncThread(parent=app, n=0, function=getDevInfo, parameters=[loglevel, phoneInfo, devhandler])
            self.thread.sendToLogSignal.connect(self.sendToLog)
            self.thread.sendUpdateSignal.connect(self.updateGui)
            self.thread.sendToProgressSignal.connect(self.updateProgress)
            self.thread.start()

            self.setdevhandler(devhandler)

        elif self.ui.auth_bypass_radioButton.isChecked():
            
            # Insert the unformatted text
            Auth_Bypass = self.ui.auth_bypass_radioButton.text()
            operation_message = f"SELECTED OPERATION : {Auth_Bypass}\t\n\n"

            # Append the operation message without the applied format
            self.ui.logBox.setPlainText(operation_message)

            # Set the color for the "operation message" message
            cursor = self.ui.logBox.textCursor()
            format = QTextCharFormat()
            format.setForeground(self.Green_color)  # Use Green color
            format.setFontPointSize(13)  # Set font size to 12 (you can adjust the 
            format.setFontWeight(QFont.Bold)  # Set font weight to Bold
            try:
                cursor.setPosition(self.ui.logBox.toPlainText().index(operation_message))
                cursor.movePosition(QTextCursor.EndOfBlock, QTextCursor.KeepAnchor)
                cursor.mergeCharFormat(format)
            except ValueError:
                # Handle the case when substring is not found
                pass

            # Start the timer to display instructions one by one
            self.current_instruction_index = 0
            self.timer.start(300)  # Adjust the timeout interval as needed 

            loglevel = logging.INFO
            devhandler = DeviceHandler(parent=app, preloader=None, loglevel=loglevel)
            devhandler.sendToLogSignal.connect(self.sendToLog)

            # Get the device info asynchronously
            self.thread = asyncThread(parent=app, n=0, function=AuthBypass, parameters=[loglevel, phoneInfo, devhandler])
            self.thread.sendToLogSignal.connect(self.sendToLog)
            self.thread.sendUpdateSignal.connect(self.updateGui)
            self.thread.sendToProgressSignal.connect(self.updateProgress)
            self.thread.start()

            self.setdevhandler(devhandler)

        elif self.ui.FRP_radioButton.isChecked():
            # Clear the log box
            self.ui.logBox.clear()

            loglevel = logging.INFO
            devhandler = DeviceHandler(parent=app, preloader=None, loglevel=loglevel)
            devhandler.sendToLogSignal.connect(self.sendToLog)

            # Get the device info asynchronously
            self.thread = asyncThread(parent=app, n=0, function=check_device, parameters=[devhandler])
            self.thread.sendToLogSignal.connect(self.sendToLog)
            self.thread.sendUpdateSignal.connect(self.updateGui)
            self.thread.sendToProgressSignal.connect(self.updateProgress)
            self.thread.start()

            # Define the command to run in the background
            command = ["python", "mtk", "e", "frp"]

            # Start a new thread to execute the command
            command_thread = threading.Thread(target=execute_command, args=(command,))
            command_thread.start()


    def on_thread_finished(self):
        # This method will be called when the asynchronous thread finishes
       pass

    def handle_stop_button(self):   
        canceled_message = "Operation canceled by user."
        self.ui.logBox.setPlainText(canceled_message)
        if hasattr(self, 'thread') and self.thread.isRunning():
            self.thread.terminate()
            self.thread.wait()

        # Emit the cancelProgressSignal
        self.cancelProgressSignal.emit()

        # Set the color for the "Operation canceled by user." message
        cursor = self.ui.logBox.textCursor()
        format = QTextCharFormat()
        format.setForeground(self.Orenge_color)  # Use Orenge color
        format.setFontPointSize(13)  # Set font size to 12 (you can adjust the 
        format.setFontWeight(QFont.Bold)  # Set font weight to Bold
        try:
            cursor.setPosition(self.ui.logBox.toPlainText().index(canceled_message))
            cursor.movePosition(QTextCursor.EndOfBlock, QTextCursor.KeepAnchor)
            cursor.mergeCharFormat(format)
        except ValueError:
            # Handle the case when substring is not found
            pass

    @Slot()
    def updateState(self):
        global lock
        lock.acquire()
        doneBytes = 0
        if "currentPartitionSizeDone" in self.Status:
            curpartBytes = self.Status["currentPartitionSizeDone"]
        else:
            curpartBytes = self.Status["currentPartitionSize"]

        if "allPartitions" in self.Status:
            for partition in self.Status["allPartitions"]:
                if self.Status["allPartitions"][partition]['done'] and partition != self.Status["currentPartition"]:
                    doneBytes = doneBytes + self.Status["allPartitions"][partition]['size']
            doneBytes = curpartBytes + doneBytes
            totalBytes = self.Status["totalsize"]
            fullPercentageDone = int((doneBytes / totalBytes) * 100)
            self.ui.fullProgress.setValue(fullPercentageDone)
            timeinfototal = self.timeEstTotal.update(fullPercentageDone, 100)
            self.ui.fullProgressText.setText("<table width='100%'><tr><td><b>Total:</b> " +
                                             convert_size(doneBytes) + " / " + convert_size(totalBytes) +
                                             "</td><td align='right'>" + timeinfototal +
                                             QCoreApplication.translate("main", " left") +
                                             "</td></tr></table>")
        else:
            partBytes = self.Status["currentPartitionSize"]
            doneBytes = self.Status["currentPartitionSizeDone"]
            fullPercentageDone = int((doneBytes / partBytes) * 100)
            self.ui.fullProgress.setValue(fullPercentageDone)
            timeinfototal = self.timeEstTotal.update(fullPercentageDone, 100)
            self.ui.fullProgressText.setText("<table width='100%'><tr><td><b>Total:</b> " +
                                             convert_size(doneBytes) + " / " + convert_size(partBytes) +
                                             "</td><td align='right'>" +
                                             timeinfototal + QCoreApplication.translate("main",
                                                                                        " left") + "</td></tr></table>")

        if "currentPartitionSize" in self.Status:
            partBytes = self.Status["currentPartitionSize"]
            partDone = (curpartBytes / partBytes) * 100
            self.ui.partProgress.setValue(partDone)
            timeinfo = self.timeEst.update(curpartBytes, partBytes)
            txt = "<table width='100%'><tr><td><b>Current partition:</b> " + self.Status["currentPartition"] + \
                  " (" + convert_size(curpartBytes) + " / " + convert_size(partBytes) + ") </td><td align='right'>" + \
                  timeinfo + QCoreApplication.translate("main", " left") + "</td></tr></table>"
            self.ui.partProgressText.setText(txt)

        lock.release()

    def updateStateAsync(self, toolkit, parameters):
        while not self.Status["done"]:
            # print(self.dumpStatus)
            time.sleep(0.1)
        print("DONE")
        self.ui.readpartitionsbtn.setEnabled(True)

        self.ui.writepartbtn.setEnabled(True)

        self.ui.erasepartitionsbtn.setEnabled(True)


    @Slot(int)
    def updateProgress(self, progress):
        try:
            if self.Status["rpmb"]:
                self.Status["currentPartitionSizeDone"] = progress
            else:
                self.Status["currentPartitionSizeDone"] = progress * self.devhandler.da_handler.mtk.daloader.progress.pagesize

            self.updateState()
        except:
            pass

    def setdevhandler(self, devhandler):
        self.devhandler = devhandler
        devhandler.sendToProgressSignal.connect(self.updateProgress)
        devhandler.update_status_text.connect(self.update_status_text)

    def initread(self):
        self.readflash = ReadFlashWindow(self.ui, self, self.devhandler.da_handler, self.sendToLog)
        self.thread.sendUpdateSignal.connect(win.updateGui)
        self.ui.readpartitionsbtn.clicked.connect(self.readflash.dumpPartition)
        self.ui.readselectallcheckbox.clicked.connect(self.readflash.selectAll)


    def initerase(self):
        self.eraseflash = EraseFlashWindow(self.ui, self, self.devhandler.da_handler, self.sendToLog)
        self.ui.eraseselectallpartitionscheckbox.clicked.connect(self.eraseflash.selectAll)
        self.ui.erasepartitionsbtn.clicked.connect(self.on_erasepartflash)


    def initwrite(self):
        self.writeflash = WriteFlashWindow(self.ui, self, self.devhandler.da_handler, self.sendToLog)
        self.ui.writeselectfromdir.clicked.connect(self.writeflash.selectFiles)
        self.ui.writepartbtn.clicked.connect(self.on_writepartflash)


    def initerase(self):
        self.eraseflash = EraseFlashWindow(self.ui, self, self.devhandler.da_handler, self.sendToLog)

    @Slot(str)
    def update_status_text(self, text):
        self.ui.logBox.append(text)

    @Slot()
    def enablebuttons(self):
        self.ui.readpartitionsbtn.setEnabled(True)        
        self.ui.partProgress.setValue(100)
        self.ui.fullProgress.setValue(100)
        self.ui.fullProgressText.setText("")
        self.ui.partProgressText.setText(self.tr("Done."))
        self.Status = {}

    def readpartition(self):
        # Clear the logBox before appending new messages
        self.ui.logBox.clear()

        # Insert the unformatted text
        
        Read_Partition = self.ui.Checkpartitionsbtn.text()
        operation_message = f"SELECTED OPERATION : {Read_Partition}\t\n\n"

        # Append the operation message without the applied format
        self.ui.logBox.setPlainText(operation_message)

        # Set the color for the "operation message" message
        cursor = self.ui.logBox.textCursor()
        format = QTextCharFormat()
        format.setForeground(self.Green_color)  # Use Green color
        format.setFontPointSize(13)  # Set font size to 12 (you can adjust the 
        format.setFontWeight(QFont.Bold)  # Set font weight to Bold
        try:
            cursor.setPosition(self.ui.logBox.toPlainText().index(operation_message))
            cursor.movePosition(QTextCursor.EndOfBlock, QTextCursor.KeepAnchor)
            cursor.mergeCharFormat(format)
        except ValueError:
            # Handle the case when substring is not found
            pass

        # Start the timer to display instructions one by one
        self.current_instruction_index = 0
        self.timer.start(300)  # Adjust the timeout interval as needed

        # Reset progress bars to 0 before starting a new operation
        self.ui.partProgress.setValue(0)
        self.ui.fullProgress.setValue(0)       

        loglevel = logging.INFO
        devhandler = DeviceHandler(parent=app, preloader=None, loglevel=loglevel)
        devhandler.sendToLogSignal.connect(self.sendToLog)

        # Get the device info asynchronously
        self.thread = asyncThread(parent=app, n=0, function=AuthBypass, parameters=[loglevel, phoneInfo, devhandler])
        self.thread.sendToLogSignal.connect(self.sendToLog)
        self.thread.sendUpdateSignal.connect(self.updateGui)
        self.thread.sendToProgressSignal.connect(self.updateProgress)
        self.thread.start()

        self.setdevhandler(devhandler)

    def getpartitions(self):
        data, guid_gpt = self.devhandler.da_handler.mtk.daloader.get_gpt()
        if guid_gpt is None:
            print("Error reading gpt")
            self.ui.readtitle.setText(QCoreApplication.translate("main", "Error reading gpt"))
        else:
            self.ui.readtitle.setText(QCoreApplication.translate("main", "Select partitions to dump"))

            # Clear existing items in the table
            self.ui.readpartitionList.clear()
            self.readpartitionCheckboxes = {}
            # Set the number of columns
            self.ui.readpartitionList.setColumnCount(6)  # Increase column count to accommodate the checkboxes
            self.ui.readpartitionList.setHorizontalHeaderLabels(["", "Partition Name", "Offset", "Length", "Type", "Size"])

            # Keep track of added partition names to avoid duplicates
            added_partitions = set()

            # Populate the table with partition data and checkboxes
            for partition in guid_gpt.partentries:
                size = partition.sectors * guid_gpt.sectorsize
                # Create a QTableWidgetItem for partition name
                partition_name = partition.name

                # Check if the partition name has been added already
                if partition_name in added_partitions:
                    continue

                # Mark the partition name as added
                added_partitions.add(partition_name)

                # Create QTableWidgetItem for each column
                offset_item = QTableWidgetItem(str(partition.first_lba))
                length_item = QTableWidgetItem(str(partition.sectors))
                
                # Attempt to determine the correct attribute for partition type
                if hasattr(partition, 'part_type'):
                    type_item = QTableWidgetItem(partition.part_type)
                elif hasattr(partition, 'type'):
                    type_item = QTableWidgetItem(partition.type)
                else:
                    type_item = QTableWidgetItem("Unknown")

                size_item = QTableWidgetItem(convert_size(size))

                # Add items to the table
                row = self.ui.readpartitionList.rowCount()
                self.ui.readpartitionList.insertRow(row)
                
                # Create a checkbox for the partition and add it to column 0
                checkbox = QCheckBox()
                self.ui.readpartitionList.setCellWidget(row, 0, checkbox)

                # Set other QTableWidgetItem for remaining columns
                self.ui.readpartitionList.setItem(row, 1, QTableWidgetItem(partition_name))
                self.ui.readpartitionList.setItem(row, 2, offset_item)
                self.ui.readpartitionList.setItem(row, 3, length_item)
                self.ui.readpartitionList.setItem(row, 4, type_item)
                self.ui.readpartitionList.setItem(row, 5, size_item)

            # Check if layout exists, if not, create a QVBoxLayout
            if self.ui.readpartitionList.layout() is None:
                self.ui.readpartitionList.setLayout(QVBoxLayout())

        writepartitionListWidgetVBox = QVBoxLayout()
        writepartitionListWidget = QWidget(self)
        writepartitionListWidget.setLayout(writepartitionListWidgetVBox)
        self.ui.writepartitionList.setWidget(writepartitionListWidget)
        self.ui.writepartitionList.setWidgetResizable(True)
        #self.ui.writepartitionList.setGeometry(10,40,380,320)
        self.ui.writepartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.writepartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.writepartitionCheckboxes = {}
        for partition in guid_gpt.partentries:
            self.writepartitionCheckboxes[partition.name] = {}
            self.writepartitionCheckboxes[partition.name]['size'] = (partition.sectors * guid_gpt.sectorsize)
            vb = QVBoxLayout()
            qc=CheckBox()
            qc.setReadOnly(True)
            qc.setText(partition.name + " (" + convert_size(partition.sectors * guid_gpt.sectorsize) + ")")
            hc=QHBoxLayout()
            ll=QLineEdit()
            lb=QPushButton(QCoreApplication.translate("main","Set"))
            lb.clicked.connect(partial(self.selectWriteFile,partition.name,qc,ll))
            hc.addWidget(ll)
            hc.addWidget(lb)
            vb.addWidget(qc)
            vb.addLayout(hc)
            ll.setDisabled(True)
            self.writepartitionCheckboxes[partition.name]['box'] = [qc,ll,lb]
            writepartitionListWidgetVBox.addLayout(vb)


        erasepartitionListWidgetVBox = QVBoxLayout()
        erasepartitionListWidget = QWidget(self)
        erasepartitionListWidget.setLayout(erasepartitionListWidgetVBox)
        self.ui.erasepartitionList.setWidget(erasepartitionListWidget)
        self.ui.erasepartitionList.setWidgetResizable(True)
        #self.ui.erasepartitionList.setGeometry(10,40,380,320)
        self.ui.erasepartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.erasepartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.erasepartitionCheckboxes = {}
        for partition in guid_gpt.partentries:
            self.erasepartitionCheckboxes[partition.name] = {}
            self.erasepartitionCheckboxes[partition.name]['size'] = (partition.sectors * guid_gpt.sectorsize)
            self.erasepartitionCheckboxes[partition.name]['box'] = QCheckBox()
            self.erasepartitionCheckboxes[partition.name]['box'].setText(partition.name + " (" +
                    convert_size(partition.sectors * guid_gpt.sectorsize)+")")
            erasepartitionListWidgetVBox.addWidget(self.erasepartitionCheckboxes[partition.name]['box'])

    def selectWriteFile(self, partition, checkbox, lineedit):
        fname=self.fdialog.open(partition+".bin")
        if fname is None:
            checkbox.setChecked(False)
            lineedit.setText("")
            lineedit.setDisabled(True)
            return ""
        checkbox.setChecked(True)
        lineedit.setText(fname)
        lineedit.setDisabled(False)
        return fname

    def on_writefullflash(self):
        self.writeflash.writeFlash("user")
        return

    def on_writepreloader(self):
        self.writeflash.writeFlash("boot1")
        return

    def on_writeboot2(self):
        self.writeflash.writeFlash("boot2")
        return

    def on_writerpmb(self):
        self.writeflash.writeFlash("rpmb")
        return

    def on_writepartflash(self):
        self.writeflash.writePartition()
        return

    def on_erasepartflash(self):
        self.eraseflash.erasePartition()
        return

    def on_eraseboot2(self):
        self.eraseflash.eraseBoot2()

    def on_erasepreloader(self):
        self.eraseflash.erasePreloader()

    def on_eraserpmb(self):
        self.eraseflash.eraseRpmb()

    def on_readpreloader(self):
        self.readflash.dumpFlash("boot1")
        return

    def on_readboot2(self):
        self.readflash.dumpFlash("boot2")
        return

    def on_readfullflash(self):
        self.readflash.dumpFlash("user")

    def on_readrpmb(self):
        self.readflash.dumpFlash("rpmb")
        return


    def sendToLog(self, info):
        unwanted_texts = ["Status: Waiting for PreLoader VCOM, please connect mobile", "Checksum:"]
        if not any(text in info for text in unwanted_texts):
            self.ui.logBox.append("✦ " + info)
            self.ui.logBox.verticalScrollBar().setValue(self.ui.logBox.verticalScrollBar().maximum())


    def sendToProgress(self, progress):
        return

    def updateGui(self):
        global phoneInfo
        phoneInfo['chipset'] = phoneInfo['chipset'].replace("()", "")
        if phoneInfo['cdcInit'] and phoneInfo['bootMode'] == "":
            self.ui.logBox.append(
                QCoreApplication.translate("main", "Phone detected:\nReading model info..."))
        else:
            self.ui.logBox.append(QCoreApplication.translate("main",
                                                                        "Phone detected:\n" + phoneInfo[
                                                                            'chipset'] + "\n" + phoneInfo['bootMode']))
        # Disabled due to graphical steps. Maybe this should come back somewhere else.
        # self.ui.status.setText(QCoreApplication.translate("main","Device detected, please wait.\nThis can take a while..."))
        if phoneInfo['daInit']:
            self.ui.logBox.append(QCoreApplication.translate("main","Device connected :)"))
            self.ui.logBox.append("")
            self.initread()
            self.initerase()
            self.getpartitions()            

        else:
            if 'cantConnect' in phoneInfo:
                self.ui.logBox.insertPlainText(
                    QCoreApplication.translate("main", "Error initialising. Did you install the drivers?"))

    # Open Device Manager 
    def open_devmgmt(self):
        os.system("cmd /c devmgmt")



################################################
############# Show T.Point Window ##############

class T_point_Window(QMainWindow):
    def __init__(self):
        super(T_point_Window, self).__init__()
        self.ui = Ui_T_point_Window()  # Use Ui_T_point_Window to set up the UI
        self.ui.setupUi(self)

        # Assing Exit Button
        self.ui.Exit_Button.clicked.connect(self.close)
        # Remove Windows Default Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Set Custom Navigation Bar
        self.ui.Menu_Frame.mouseMoveEvent = self.MoveWindow
        # Assing Minimize Button
        self.ui.Minimize_Button.clicked.connect(self.showMinimized)

        # Assing Phone Models Button's
        self.ui.XIAOMI_BTN.clicked.connect(self.xiaomi_list)
        self.ui.SAMSUNG_BTN.clicked.connect(self.samsung_list)
        self.ui.HUAWEI_BTN.clicked.connect(self.huawei_list)
        #self.ui.VIVO_BTN.clicked.connect(self.vivo_list)
        #self.ui.OPPO_BTN.clicked.connect(self.oppo_list)
        #self.ui.LENOVO_BTN.clicked.connect(self.lenovo_list)
        #self.ui.VSMART_BTN.clicked.connect(self.vsmart_list)
        #self.ui.NOKIA_BTN.clicked.connect(self.nokia_list)
        #self.ui.AZUS_BTN.clicked.connect(self.azus_list)
        #self.ui.LG_BTN.clicked.connect(self.lg_list)
        #self.ui.MEIZU_BTN.clicked.connect(self.meizu_list)


       # Connect Phone_List clicked signal to display_image method
        self.ui.Phone_List.clicked.connect(self.display_image)

        # Dictionary to map phone models to image paths
        self.image_paths = {
            # Add Xiaomi Images Paths
            "Redmi Note 5A": "TestPoint/Xiaomi/Xiaomi Redmi Note 5A.png",
            "Redmi Note 8 Pro": "TestPoint/Xiaomi/Xiaomi Redmi Note 8 Pro.png",
            "Xiaomi Redmi A1+": "TestPoint/Xiaomi/Xiaomi Redmi A1+.png",
            "Xiaomi Redmi K30 Pro": "TestPoint/Xiaomi/Xiaomi Redmi K30 Pro.png",

            # Add Samsung Images Paths
            "Samsung Galaxy A02": "TestPoint/Samsung/Samsung Galaxy A02.png",
            "Samsung Galaxy A25 5G": "TestPoint/Samsung/Samsung Galaxy A25 5G.png",
            "Samsung Galaxy S21 Plus 5G": "TestPoint/Samsung/Samsung Galaxy S21 Plus 5G.png",

            # Add Huawei Images Paths
            "Huawei P20 Lite Dual SIM": "TestPoint/Huawei/Huawei P20 Lite Dual SIM.png",
            "Huawei P10": "TestPoint/Huawei/Huawei P10.png",
            "Huawei Y8P": "TestPoint/Huawei/Huawei Y8P.png",
        }


    def MoveWindow(self, event):
        if not self.isMaximized():
            self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()



    def xiaomi_list(self):
        phone_models = ["Redmi Note 5A", "Redmi Note 8 Pro", "Xiaomi Redmi A1+", "Xiaomi Redmi K30 Pro"]
        self.ui.Phone_List.clear()  # Clear previous items in the list
        for model in phone_models:
            item = QListWidgetItem(model)
            self.ui.Phone_List.addItem(item)

    def samsung_list(self):
        phone_models = ["Samsung Galaxy A02", "Samsung Galaxy A25 5G", "Samsung Galaxy S21 Plus 5G"]
        self.ui.Phone_List.clear()  # Clear previous items in the list
        for model in phone_models:
            item = QListWidgetItem(model)
            self.ui.Phone_List.addItem(item)

    def huawei_list(self):
        phone_models = ["Huawei P20 Lite Dual SIM", "Huawei P10", "Huawei Y8P"]
        self.ui.Phone_List.clear()  # Clear previous items in the list
        for model in phone_models:
            item = QListWidgetItem(model)
            self.ui.Phone_List.addItem(item)

    def display_image(self, index):
        item = self.ui.Phone_List.itemFromIndex(index)
        if item is not None:
            selected_model = item.text()
            if selected_model in self.image_paths:
                image_path = self.image_paths[selected_model]
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    QMessageBox.warning(self, "Image Not Found", "The image for this phone model is not found.")
                else:
                    # Scale the image to fit the QLabel
                    scaled_pixmap = pixmap.scaled(self.ui.IMG_Label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    self.ui.IMG_Label.setPixmap(scaled_pixmap)
            else:
                QMessageBox.warning(self, "Image Not Found", "No image found for this phone model.")


if __name__ == '__main__':
    # Enable nice 4K Scaling
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    # Init the app window
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show() 

    # Run loop the app
    app.exec()
