# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestpointkhWOdK.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import rc_ico

class Ui_T_point_Window(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(989, 574)
        MainWindow.setStyleSheet(u"QStatusBar {\n"
"    background:rgb(26, 26, 26);\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid red;\n"
"    border-radius: 3px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Menu_Frame = QFrame(self.centralwidget)
        self.Menu_Frame.setObjectName(u"Menu_Frame")
        self.Menu_Frame.setGeometry(QRect(0, 0, 1001, 41))
        self.Menu_Frame.setStyleSheet(u"#Menu_Frame{\n"
"background-color:rgb(26, 26, 26);\n"
"}")
        self.Menu_Frame.setFrameShape(QFrame.StyledPanel)
        self.Menu_Frame.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.Menu_Frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(5, 5, 31, 31))
        self.pushButton_4.setStyleSheet(u"border:0;\n"
"background-color:rgb(26, 26, 26);")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/google.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(16, 16))
        self.pushButton_4.setFlat(True)
        self.label = QLabel(self.Menu_Frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 11, 291, 16))
        font = QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(152, 152, 152);\n"
"background-color:rgb(26, 26, 26);")
        self.Exit_Button = QPushButton(self.Menu_Frame)
        self.Exit_Button.setObjectName(u"Exit_Button")
        self.Exit_Button.setGeometry(QRect(956, 6, 31, 31))
        self.Exit_Button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"	border:0;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(235, 59, 90);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Exit_Button.setIcon(icon1)
        self.Exit_Button.setIconSize(QSize(16, 16))
        self.Exit_Button.setFlat(True)
        self.pushButton_5 = QPushButton(self.Menu_Frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(923, 6, 31, 31))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"	border:0;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/images/Images/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(16, 16))
        self.pushButton_5.setFlat(True)
        self.Minimize_Button = QPushButton(self.Menu_Frame)
        self.Minimize_Button.setObjectName(u"Minimize_Button")
        self.Minimize_Button.setGeometry(QRect(890, 6, 31, 31))
        self.Minimize_Button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"	border:0;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Minimize_Button.setIcon(icon3)
        self.Minimize_Button.setIconSize(QSize(16, 16))
        self.Minimize_Button.setFlat(True)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(0, 40, 1001, 521))
        self.main_frame.setStyleSheet(u"QFrame#main_frame {\n"
"background-color: rgb(45, 45, 45);\n"
"}\n"
"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget QTableCornerButton::section{\n"
"	background-color: rgb(19, 34, 64);\n"
"	border:1px solid rgb(19, 34, 66);\n"
"}\n"
"\n"
"/* ScrollBar Vertical */\n"
"\n"
"QScrollBar::vertical{\n"
"	border:none;\n"
"	background-color:rgb(62, 62, 62);\n"
"	width:14px;\n"
"	margin:15px 0 15px 0;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical{\n"
"	background-color:#1C1C1C;\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"QScrollBar::handle::vertical:hover{\n"
"	background-color: #2E2E2E;\n"
"}\n"
"QScrollBar::handle::vertical:pressed{\n"
"	background-color: rgb(255, 84, 152);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	height:15px;\n"
"	border-top-left-radius:2px;\n"
"	border-top-right-radius:2px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"	"
                        "background-color:rgb(255, 84, 152);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color:  rgb(255, 84, 152);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	height:15px;\n"
"	border-bottom-left-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover{\n"
"	background-color:rgb(255, 84, 152);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color:  rgb(255, 84, 152);\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	background:none;\n"
"}	\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background:none;\n"
"}	\n"
"\n"
"\n"
"/* ScrollBar Horizontal */\n"
"\n"
"QScrollBar::horizontal{\n"
"	border:none;\n"
"	background-color:rgb(62, 62, 62);\n"
"	height:14px;\n"
"	margin:0 15px 0 15px;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::horizontal{\n"
"	background-color:#1C1"
                        "C1C;\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"QScrollBar::handle::horizontal:hover{\n"
"	background-color: #2E2E2E;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	width:15px;\n"
"	border-top-left-radius:2px;\n"
"	border-bottom-left-radius:2px;\n"
"	subcontrol-position:left;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover{\n"
"	background-color: rgb(255, 84, 152);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"	background-color: rgb(255, 84, 152);\n"
"}\n"
"QScrollBar::add-line:horizontal{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	width:15px;\n"
"	border-top-right-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:right;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover{\n"
"	background-color: rgb(255, 84, 152);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed{\n"
"	background-color:  rgb(255, 84, 152);\n"
"}\n"
"QScrollBar::up-arrow:horizontal"
                        ", QScrollBar::down-arrow:horizontal{\n"
"	background:none;\n"
"}	\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background:none;\n"
"}\n"
"QProgressBar{\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(35, 35, 35);	\n"
"	border-style: rgb(85, 255, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 20px;\n"
"	  background-color:qlineargradient(spread:pad, x1:0.051, y1:0.0516364, x2:1, y2:1, stop:0 rgba(229, 144, 38, 255), stop:1 rgba(249, 178, 0, 255));\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.Menu_Frame_2 = QFrame(self.main_frame)
        self.Menu_Frame_2.setObjectName(u"Menu_Frame_2")
        self.Menu_Frame_2.setGeometry(QRect(0, 0, 1081, 41))
        self.Menu_Frame_2.setStyleSheet(u"#Menu_Frame{\n"
"background-color:rgb(26, 26, 26);\n"
"}")
        self.Menu_Frame_2.setFrameShape(QFrame.StyledPanel)
        self.Menu_Frame_2.setFrameShadow(QFrame.Raised)
        self.Exit_Button_2 = QPushButton(self.Menu_Frame_2)
        self.Exit_Button_2.setObjectName(u"Exit_Button_2")
        self.Exit_Button_2.setGeometry(QRect(1036, 6, 31, 31))
        self.Exit_Button_2.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"	border:0;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(235, 59, 90);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Exit_Button_2.setIcon(icon1)
        self.Exit_Button_2.setIconSize(QSize(16, 16))
        self.Exit_Button_2.setFlat(True)
        self.pushButton_7 = QPushButton(self.Menu_Frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(1003, 6, 31, 31))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"	border:0;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QSize(16, 16))
        self.pushButton_7.setFlat(True)
        self.tab_frame = QFrame(self.main_frame)
        self.tab_frame.setObjectName(u"tab_frame")
        self.tab_frame.setGeometry(QRect(0, 0, 991, 51))
        self.tab_frame.setStyleSheet(u"QFrame{\n"
"    background-color: rgb(39, 39, 39);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(255, 255, 255);\n"
"	border:0;\n"
"	margin-right:2px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(95, 95, 95);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tab_frame.setFrameShape(QFrame.StyledPanel)
        self.tab_frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.tab_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 10, 461, 31))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Kurdish"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(243, 243, 243);")
        self.partProgress = QProgressBar(self.main_frame)
        self.partProgress.setObjectName(u"partProgress")
        self.partProgress.setGeometry(QRect(570, 560, 401, 16))
        self.partProgress.setStyleSheet(u"")
        self.partProgress.setValue(100)
        self.partProgress.setAlignment(Qt.AlignCenter)
        self.fullProgress = QProgressBar(self.main_frame)
        self.fullProgress.setObjectName(u"fullProgress")
        self.fullProgress.setGeometry(QRect(570, 580, 401, 16))
        self.fullProgress.setValue(100)
        self.fullProgress.setAlignment(Qt.AlignCenter)
        self.partProgressText = QLabel(self.main_frame)
        self.partProgressText.setObjectName(u"partProgressText")
        self.partProgressText.setGeometry(QRect(570, 560, 301, 16))
        self.fullProgressText = QLabel(self.main_frame)
        self.fullProgressText.setObjectName(u"fullProgressText")
        self.fullProgressText.setGeometry(QRect(570, 580, 301, 16))
        self.Stop_BTN = QPushButton(self.main_frame)
        self.Stop_BTN.setObjectName(u"Stop_BTN")
        self.Stop_BTN.setGeometry(QRect(980, 560, 81, 37))
        font2 = QFont()
        font2.setBold(True)
        self.Stop_BTN.setFont(font2)
        self.Stop_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color:#DE3163 ;\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(227, 68, 70);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stop_BTN.setIcon(icon4)
        self.Stop_BTN.setIconSize(QSize(12, 12))
        self.frame = QFrame(self.main_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 60, 181, 441))
        self.frame.setStyleSheet(u"QFrame{\n"
"border:1px solid rgb(61, 61, 61);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.XIAOMI_BTN = QPushButton(self.frame)
        self.XIAOMI_BTN.setObjectName(u"XIAOMI_BTN")
        self.XIAOMI_BTN.setGeometry(QRect(10, 7, 161, 31))
        self.XIAOMI_BTN.setFont(font2)
        self.XIAOMI_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.SAMSUNG_BTN = QPushButton(self.frame)
        self.SAMSUNG_BTN.setObjectName(u"SAMSUNG_BTN")
        self.SAMSUNG_BTN.setGeometry(QRect(10, 44, 161, 31))
        self.SAMSUNG_BTN.setFont(font2)
        self.SAMSUNG_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.HUAWEI_BTN = QPushButton(self.frame)
        self.HUAWEI_BTN.setObjectName(u"HUAWEI_BTN")
        self.HUAWEI_BTN.setGeometry(QRect(10, 81, 161, 31))
        self.HUAWEI_BTN.setFont(font2)
        self.HUAWEI_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.VIVO_BTN = QPushButton(self.frame)
        self.VIVO_BTN.setObjectName(u"VIVO_BTN")
        self.VIVO_BTN.setGeometry(QRect(10, 120, 161, 31))
        self.VIVO_BTN.setFont(font2)
        self.VIVO_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.OPPO_BTN = QPushButton(self.frame)
        self.OPPO_BTN.setObjectName(u"OPPO_BTN")
        self.OPPO_BTN.setGeometry(QRect(10, 160, 161, 31))
        self.OPPO_BTN.setFont(font2)
        self.OPPO_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.LENOVO_BTN = QPushButton(self.frame)
        self.LENOVO_BTN.setObjectName(u"LENOVO_BTN")
        self.LENOVO_BTN.setGeometry(QRect(10, 200, 161, 31))
        self.LENOVO_BTN.setFont(font2)
        self.LENOVO_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.VSMART_BTN = QPushButton(self.frame)
        self.VSMART_BTN.setObjectName(u"VSMART_BTN")
        self.VSMART_BTN.setGeometry(QRect(10, 240, 161, 31))
        self.VSMART_BTN.setFont(font2)
        self.VSMART_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.NOKIA_BTN = QPushButton(self.frame)
        self.NOKIA_BTN.setObjectName(u"NOKIA_BTN")
        self.NOKIA_BTN.setGeometry(QRect(10, 280, 161, 31))
        self.NOKIA_BTN.setFont(font2)
        self.NOKIA_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.AZUS_BTN = QPushButton(self.frame)
        self.AZUS_BTN.setObjectName(u"AZUS_BTN")
        self.AZUS_BTN.setGeometry(QRect(10, 320, 161, 31))
        self.AZUS_BTN.setFont(font2)
        self.AZUS_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.LG_BTN = QPushButton(self.frame)
        self.LG_BTN.setObjectName(u"LG_BTN")
        self.LG_BTN.setGeometry(QRect(10, 360, 161, 31))
        self.LG_BTN.setFont(font2)
        self.LG_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.MEIZU_BTN = QPushButton(self.frame)
        self.MEIZU_BTN.setObjectName(u"MEIZU_BTN")
        self.MEIZU_BTN.setGeometry(QRect(10, 400, 161, 31))
        self.MEIZU_BTN.setFont(font2)
        self.MEIZU_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(39, 39, 39);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.frame_2 = QFrame(self.main_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(200, 60, 251, 441))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"border:1px solid rgb(61, 61, 61);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 231, 22))
        self.lineEdit.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"border:none;\n"
"border-bottom:1px solid #99A3A4;\n"
"color: rgb(149, 149, 149);\n"
"padding:0 0 5px 5px;\n"
"")
        self.lineEdit.setMaxLength(200)
        self.Phone_List = QListWidget(self.frame_2)
        self.Phone_List.setObjectName(u"Phone_List")
        self.Phone_List.setGeometry(QRect(10, 40, 231, 391))
        self.Phone_List.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color: rgb(245, 245, 245);\n"
"padding:7px;")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(220, 10, 16, 16))
        self.widget.setStyleSheet(u"border-image: url(:/newPrefix/icons/search.png);")
        self.IMG_Label = QLabel(self.main_frame)
        self.IMG_Label.setObjectName(u"IMG_Label")
        self.IMG_Label.setGeometry(QRect(460, 60, 521, 441))
        self.IMG_Label.setStyleSheet(u"QLabel{\n"
"border:1px solid rgb(61, 61, 61);\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Laroussi Universal Tool V1.0 | https://laroussigsm.net/", None))
#if QT_CONFIG(tooltip)
        self.Exit_Button.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.Exit_Button.setText("")
        self.pushButton_5.setText("")
        self.Minimize_Button.setText("")
#if QT_CONFIG(tooltip)
        self.Exit_Button_2.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.Exit_Button_2.setText("")
        self.pushButton_7.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ALL ANDROID MOBILE TEST POINT", None))
        self.partProgressText.setText("")
        self.fullProgressText.setText("")
        self.Stop_BTN.setText(QCoreApplication.translate("MainWindow", u" STOP", None))
        self.XIAOMI_BTN.setText(QCoreApplication.translate("MainWindow", u"XIAOMI", None))
        self.SAMSUNG_BTN.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.HUAWEI_BTN.setText(QCoreApplication.translate("MainWindow", u"HUAWEI", None))
        self.VIVO_BTN.setText(QCoreApplication.translate("MainWindow", u"VIVO", None))
        self.OPPO_BTN.setText(QCoreApplication.translate("MainWindow", u"OPPO", None))
        self.LENOVO_BTN.setText(QCoreApplication.translate("MainWindow", u"LENOVO", None))
        self.VSMART_BTN.setText(QCoreApplication.translate("MainWindow", u"VSMART", None))
        self.NOKIA_BTN.setText(QCoreApplication.translate("MainWindow", u"NOKIA", None))
        self.AZUS_BTN.setText(QCoreApplication.translate("MainWindow", u"AZUS", None))
        self.LG_BTN.setText(QCoreApplication.translate("MainWindow", u"LG", None))
        self.MEIZU_BTN.setText(QCoreApplication.translate("MainWindow", u"MEIZU", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Searching By Model ...      ", None))
        self.IMG_Label.setText("")
    # retranslateUi