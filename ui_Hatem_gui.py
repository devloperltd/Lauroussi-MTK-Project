# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Hatem_guiYaUVVn.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QStackedWidget, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)
import rc_ico
import rc_img

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1076, 663)
        MainWindow.setStyleSheet(u"QStatusBar {\n"
"    background:rgb(26, 26, 26);\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid red;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
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
"	background-color:#1C1C1C;\n"
""
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
"QScrollBar::up-arrow:horizontal, QScroll"
                        "Bar::down-arrow:horizontal{\n"
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
"}\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.Menu_Frame = QFrame(self.main_frame)
        self.Menu_Frame.setObjectName(u"Menu_Frame")
        self.Menu_Frame.setGeometry(QRect(0, 0, 1081, 41))
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
        icon.addFile(u":/newPrefix/icons/bolt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(16, 16))
        self.pushButton_4.setFlat(True)
        self.label = QLabel(self.Menu_Frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 11, 461, 16))
        font = QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(152, 152, 152);\n"
"background-color:rgb(26, 26, 26);")
        self.Exit_Button = QPushButton(self.Menu_Frame)
        self.Exit_Button.setObjectName(u"Exit_Button")
        self.Exit_Button.setGeometry(QRect(1036, 6, 31, 31))
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
        self.pushButton_5.setGeometry(QRect(1003, 6, 31, 31))
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
        self.Minimize_Button.setGeometry(QRect(970, 6, 31, 31))
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
        self.tab_frame = QFrame(self.main_frame)
        self.tab_frame.setObjectName(u"tab_frame")
        self.tab_frame.setGeometry(QRect(0, 40, 1081, 101))
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
        self.Home_Btn = QPushButton(self.tab_frame)
        self.Home_Btn.setObjectName(u"Home_Btn")
        self.Home_Btn.setGeometry(QRect(220, 0, 91, 91))
        self.Home_Btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home_Btn.setIcon(icon4)
        self.Home_Btn.setIconSize(QSize(58, 58))
        self.MediaTek_Btn = QPushButton(self.tab_frame)
        self.MediaTek_Btn.setObjectName(u"MediaTek_Btn")
        self.MediaTek_Btn.setGeometry(QRect(310, 0, 91, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MediaTek_Btn.sizePolicy().hasHeightForWidth())
        self.MediaTek_Btn.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.MediaTek_Btn.setFont(font1)
        self.MediaTek_Btn.setAcceptDrops(False)
        self.MediaTek_Btn.setLayoutDirection(Qt.LeftToRight)
        self.MediaTek_Btn.setAutoFillBackground(False)
        self.MediaTek_Btn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/MEDIATEK.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MediaTek_Btn.setIcon(icon5)
        self.MediaTek_Btn.setIconSize(QSize(58, 58))
        self.MediaTek_Btn.setAutoRepeat(False)
        self.MediaTek_Btn.setAutoDefault(False)
        self.MediaTek_Btn.setFlat(False)
        self.Qualcomm_Btn = QPushButton(self.tab_frame)
        self.Qualcomm_Btn.setObjectName(u"Qualcomm_Btn")
        self.Qualcomm_Btn.setGeometry(QRect(490, 0, 91, 91))
        self.Qualcomm_Btn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/Qualcomm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Qualcomm_Btn.setIcon(icon6)
        self.Qualcomm_Btn.setIconSize(QSize(70, 70))
        self.TestPoints = QPushButton(self.tab_frame)
        self.TestPoints.setObjectName(u"TestPoints")
        self.TestPoints.setGeometry(QRect(760, 0, 91, 91))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.TestPoints.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/Test-Point.png", QSize(), QIcon.Normal, QIcon.Off)
        self.TestPoints.setIcon(icon7)
        self.TestPoints.setIconSize(QSize(50, 50))
        self.About_Btn = QPushButton(self.tab_frame)
        self.About_Btn.setObjectName(u"About_Btn")
        self.About_Btn.setGeometry(QRect(850, 0, 91, 91))
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icons/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.About_Btn.setIcon(icon8)
        self.About_Btn.setIconSize(QSize(50, 50))
        self.widget = QWidget(self.tab_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 51, 51))
        self.widget.setStyleSheet(u"border-image: url(:/newPrefix/icons/tyrannosaurus-rex.png);")
        self.label_2 = QLabel(self.tab_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 20, 101, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(25)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(222, 49, 99);\n"
"font: 700 25pt \"Segoe UI\";")
        self.label_3 = QLabel(self.tab_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 50, 101, 16))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.Samsung_Btn = QPushButton(self.tab_frame)
        self.Samsung_Btn.setObjectName(u"Samsung_Btn")
        self.Samsung_Btn.setGeometry(QRect(580, 0, 91, 91))
        self.Samsung_Btn.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icons/samsung.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Samsung_Btn.setIcon(icon9)
        self.Samsung_Btn.setIconSize(QSize(70, 70))
        self.Huawei_Btn = QPushButton(self.tab_frame)
        self.Huawei_Btn.setObjectName(u"Huawei_Btn")
        self.Huawei_Btn.setGeometry(QRect(400, 0, 91, 91))
        self.Huawei_Btn.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/icons/huawei.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Huawei_Btn.setIcon(icon10)
        self.Huawei_Btn.setIconSize(QSize(70, 70))
        self.Android_Btn = QPushButton(self.tab_frame)
        self.Android_Btn.setObjectName(u"Android_Btn")
        self.Android_Btn.setGeometry(QRect(670, 0, 91, 91))
        self.Android_Btn.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/icons/ANDROID.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Android_Btn.setIcon(icon11)
        self.Android_Btn.setIconSize(QSize(70, 70))
        self.label_9 = QLabel(self.main_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 134, 1081, 41))
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"background-color: rgb(26, 26, 26);\n"
"color: rgb(210, 218, 226);")
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.partProgressText = QLabel(self.main_frame)
        self.partProgressText.setObjectName(u"partProgressText")
        self.partProgressText.setGeometry(QRect(570, 560, 301, 16))
        self.fullProgressText = QLabel(self.main_frame)
        self.fullProgressText.setObjectName(u"fullProgressText")
        self.fullProgressText.setGeometry(QRect(570, 580, 301, 16))
        self.Container_tab = QStackedWidget(self.main_frame)
        self.Container_tab.setObjectName(u"Container_tab")
        self.Container_tab.setGeometry(QRect(0, 180, 1071, 471))
        self.Home_tab = QWidget()
        self.Home_tab.setObjectName(u"Home_tab")
        self.Home_tab.setStyleSheet(u"")
        self.log_win_tab = QStackedWidget(self.Home_tab)
        self.log_win_tab.setObjectName(u"log_win_tab")
        self.log_win_tab.setGeometry(QRect(0, 10, 1071, 451))
        font5 = QFont()
        font5.setPointSize(11)
        self.log_win_tab.setFont(font5)
        self.log_win_tab.setStyleSheet(u"QLineEdit {\n"
"    border: none ;\n"
"	color: rgb(50, 50, 50);\n"
"    border-radius: 2px;\n"
"    padding: 0 8px;\n"
"    background: rgb(68, 68, 68);\n"
"	border-bottom: 2px solid rgb(98, 98, 98);\n"
"	color: rgb(248, 248, 248);\n"
"    selection-background-color: darkgray;\n"
"}")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"")
        self.frame = QFrame(self.login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(350, 50, 371, 371))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(30, 30, 30);\n"
"border-radius:8px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 60, 221, 61))
        font6 = QFont()
        font6.setFamilies([u"MS Shell Dlg 2"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"background-color: 0;\n"
"color: qlineargradient(spread:pad, x1:0.961, y1:0.091, x2:1, y2:0.00568182, stop:0.409091 rgba(0, 175, 178, 255), stop:1 rgba(255, 255, 255, 255));")
        self.login_username = QLineEdit(self.frame)
        self.login_username.setObjectName(u"login_username")
        self.login_username.setGeometry(QRect(30, 140, 311, 31))
        self.login_username.setMinimumSize(QSize(231, 0))
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(False)
        self.login_username.setFont(font7)
        self.login_username.setAcceptDrops(True)
        self.login_username.setStyleSheet(u"")
        self.login_username.setFrame(True)
        self.login_password = QLineEdit(self.frame)
        self.login_password.setObjectName(u"login_password")
        self.login_password.setGeometry(QRect(30, 190, 311, 31))
        self.login_password.setMinimumSize(QSize(231, 0))
        font8 = QFont()
        font8.setPointSize(10)
        self.login_password.setFont(font8)
        self.login_password.setAcceptDrops(True)
        self.login_password.setStyleSheet(u"")
        self.login_password.setEchoMode(QLineEdit.Password)
        self.Forget_Pass_Button = QPushButton(self.frame)
        self.Forget_Pass_Button.setObjectName(u"Forget_Pass_Button")
        self.Forget_Pass_Button.setGeometry(QRect(30, 230, 131, 23))
        self.Forget_Pass_Button.setFont(font2)
        self.Forget_Pass_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Forget_Pass_Button.setStyleSheet(u"QPushButton{\n"
"  color: rgb(93, 173, 226);\n"
"	background-color:0;\n"
"border:0;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 2px;\n"
"}")
        self.login_Btn = QPushButton(self.frame)
        self.login_Btn.setObjectName(u"login_Btn")
        self.login_Btn.setGeometry(QRect(30, 270, 311, 31))
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setKerning(False)
        font9.setStyleStrategy(QFont.PreferDefault)
        self.login_Btn.setFont(font9)
        self.login_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_Btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.login_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 168, 83);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.SignUp_Button = QPushButton(self.frame)
        self.SignUp_Button.setObjectName(u"SignUp_Button")
        self.SignUp_Button.setGeometry(QRect(180, 310, 81, 23))
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(True)
        self.SignUp_Button.setFont(font10)
        self.SignUp_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.SignUp_Button.setStyleSheet(u"QPushButton{\n"
"  background-color: 0;\n"
"  color: rgb(93, 173, 226);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"}")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 311, 141, 21))
        font11 = QFont()
        font11.setFamilies([u"Yu Gothic UI"])
        font11.setPointSize(10)
        font11.setBold(False)
        self.label_7.setFont(font11)
        self.label_7.setStyleSheet(u"color: #F2F3F4;\n"
"background-color: 0;")
        self.widget_2 = QWidget(self.login)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(480, 0, 111, 111))
        self.widget_2.setStyleSheet(u"border-image: url(:/newPrefix/icons/T.logo2.png);")
        self.frame_4 = QFrame(self.login)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-110, -20, 361, 481))
        self.frame_4.setStyleSheet(u"border-image: url(:/newPrefix/icons/Texteur.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.login)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(830, 140, 401, 501))
        self.frame_5.setStyleSheet(u"border-image: url(:/newPrefix/icons/Texteur.png);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.log_win_tab.addWidget(self.login)
        self.frame_4.raise_()
        self.frame.raise_()
        self.widget_2.raise_()
        self.frame_5.raise_()
        self.registration = QWidget()
        self.registration.setObjectName(u"registration")
        self.frame_2 = QFrame(self.registration)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 1051, 431))
        self.frame_2.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_2.setStyleSheet(u"QFrame#frame_2{\n"
"border-radius:5px;\n"
"background-color: 0;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.Reg_Btn = QPushButton(self.frame_2)
        self.Reg_Btn.setObjectName(u"Reg_Btn")
        self.Reg_Btn.setGeometry(QRect(180, 250, 791, 41))
        self.Reg_Btn.setFont(font9)
        self.Reg_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Reg_Btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.Reg_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 168, 83);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(163, 228, 215);\n"
"}")
        self.Reg_First_username = QLineEdit(self.frame_2)
        self.Reg_First_username.setObjectName(u"Reg_First_username")
        self.Reg_First_username.setGeometry(QRect(180, 80, 301, 31))
        self.Reg_First_username.setMinimumSize(QSize(231, 0))
        self.Reg_First_username.setFont(font7)
        self.Reg_First_username.setAcceptDrops(True)
        self.Reg_First_username.setStyleSheet(u"")
        self.Reg_First_username.setFrame(True)
        self.Reg_email = QLineEdit(self.frame_2)
        self.Reg_email.setObjectName(u"Reg_email")
        self.Reg_email.setGeometry(QRect(180, 120, 301, 31))
        self.Reg_email.setMinimumSize(QSize(231, 0))
        self.Reg_email.setFont(font8)
        self.Reg_email.setAcceptDrops(True)
        self.Reg_email.setStyleSheet(u"")
        self.Reg_email.setEchoMode(QLineEdit.Normal)
        self.Reg_last_username = QLineEdit(self.frame_2)
        self.Reg_last_username.setObjectName(u"Reg_last_username")
        self.Reg_last_username.setGeometry(QRect(670, 80, 301, 31))
        self.Reg_last_username.setMinimumSize(QSize(231, 0))
        self.Reg_last_username.setFont(font7)
        self.Reg_last_username.setAcceptDrops(True)
        self.Reg_last_username.setStyleSheet(u"")
        self.Reg_last_username.setFrame(True)
        self.radio_female_Button = QRadioButton(self.frame_2)
        self.radio_female_Button.setObjectName(u"radio_female_Button")
        self.radio_female_Button.setGeometry(QRect(860, 170, 91, 17))
        self.radio_female_Button.setFont(font2)
        self.radio_female_Button.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radio_male_Button = QRadioButton(self.frame_2)
        self.radio_male_Button.setObjectName(u"radio_male_Button")
        self.radio_male_Button.setGeometry(QRect(670, 170, 81, 17))
        self.radio_male_Button.setFont(font2)
        self.radio_male_Button.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 170, 111, 16))
        font12 = QFont()
        font12.setPointSize(12)
        font12.setBold(True)
        self.label_5.setFont(font12)
        self.label_5.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.Country_Comb = QComboBox(self.frame_2)
        self.Country_Comb.addItem("")
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix2/Country Flags/af.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon12, "")
        icon13 = QIcon()
        icon13.addFile(u":/newPrefix2/Country Flags/al.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u":/newPrefix2/Country Flags/dz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon14, "")
        icon15 = QIcon()
        icon15.addFile(u":/newPrefix2/Country Flags/ad.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon15, "")
        icon16 = QIcon()
        icon16.addFile(u":/newPrefix2/Country Flags/ao.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon16, "")
        icon17 = QIcon()
        icon17.addFile(u":/newPrefix2/Country Flags/ag.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon17, "")
        icon18 = QIcon()
        icon18.addFile(u":/newPrefix2/Country Flags/ar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon18, "")
        icon19 = QIcon()
        icon19.addFile(u":/newPrefix2/Country Flags/am.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon19, "")
        icon20 = QIcon()
        icon20.addFile(u":/newPrefix2/Country Flags/ai.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon20, "")
        icon21 = QIcon()
        icon21.addFile(u":/newPrefix2/Country Flags/at.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon21, "")
        icon22 = QIcon()
        icon22.addFile(u":/newPrefix2/Country Flags/az.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon22, "")
        icon23 = QIcon()
        icon23.addFile(u":/newPrefix2/Country Flags/bs.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon23, "")
        icon24 = QIcon()
        icon24.addFile(u":/newPrefix2/Country Flags/bh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon24, "")
        icon25 = QIcon()
        icon25.addFile(u":/newPrefix2/Country Flags/bd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon25, "")
        icon26 = QIcon()
        icon26.addFile(u":/newPrefix2/Country Flags/bb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon26, "")
        icon27 = QIcon()
        icon27.addFile(u":/newPrefix2/Country Flags/by.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon27, "")
        icon28 = QIcon()
        icon28.addFile(u":/newPrefix2/Country Flags/be.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon28, "")
        icon29 = QIcon()
        icon29.addFile(u":/newPrefix2/Country Flags/bz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon29, "")
        icon30 = QIcon()
        icon30.addFile(u":/newPrefix2/Country Flags/bj.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon30, "")
        icon31 = QIcon()
        icon31.addFile(u":/newPrefix2/Country Flags/bt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon31, "")
        icon32 = QIcon()
        icon32.addFile(u":/newPrefix2/Country Flags/bo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon32, "")
        icon33 = QIcon()
        icon33.addFile(u":/newPrefix2/Country Flags/ba.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon33, "")
        icon34 = QIcon()
        icon34.addFile(u":/newPrefix2/Country Flags/bw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon34, "")
        icon35 = QIcon()
        icon35.addFile(u":/newPrefix2/Country Flags/br.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon35, "")
        icon36 = QIcon()
        icon36.addFile(u":/newPrefix2/Country Flags/bn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon36, "")
        icon37 = QIcon()
        icon37.addFile(u":/newPrefix2/Country Flags/bg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon37, "")
        icon38 = QIcon()
        icon38.addFile(u":/newPrefix2/Country Flags/bf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon38, "")
        icon39 = QIcon()
        icon39.addFile(u":/newPrefix2/Country Flags/bi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon39, "")
        icon40 = QIcon()
        icon40.addFile(u":/newPrefix2/Country Flags/ci.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon40, "")
        icon41 = QIcon()
        icon41.addFile(u":/newPrefix2/Country Flags/cv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon41, "")
        icon42 = QIcon()
        icon42.addFile(u":/newPrefix2/Country Flags/kh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon42, "")
        icon43 = QIcon()
        icon43.addFile(u":/newPrefix2/Country Flags/cm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon43, "")
        icon44 = QIcon()
        icon44.addFile(u":/newPrefix2/Country Flags/ca.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon44, "")
        icon45 = QIcon()
        icon45.addFile(u":/newPrefix2/Country Flags/cf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon45, "")
        icon46 = QIcon()
        icon46.addFile(u":/newPrefix2/Country Flags/ro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon46, "")
        icon47 = QIcon()
        icon47.addFile(u":/newPrefix2/Country Flags/cl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon47, "")
        icon48 = QIcon()
        icon48.addFile(u":/newPrefix2/Country Flags/cn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon48, "")
        icon49 = QIcon()
        icon49.addFile(u":/newPrefix2/Country Flags/co.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon49, "")
        icon50 = QIcon()
        icon50.addFile(u":/newPrefix2/Country Flags/km.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon50, "")
        icon51 = QIcon()
        icon51.addFile(u":/newPrefix2/Country Flags/cg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon51, "")
        icon52 = QIcon()
        icon52.addFile(u":/newPrefix2/Country Flags/cr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon52, "")
        icon53 = QIcon()
        icon53.addFile(u":/newPrefix2/Country Flags/hr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon53, "")
        icon54 = QIcon()
        icon54.addFile(u":/newPrefix2/Country Flags/cu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon54, "")
        icon55 = QIcon()
        icon55.addFile(u":/newPrefix2/Country Flags/cy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon55, "")
        icon56 = QIcon()
        icon56.addFile(u":/newPrefix2/Country Flags/cz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon56, "")
        icon57 = QIcon()
        icon57.addFile(u":/newPrefix2/Country Flags/cd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon57, "")
        icon58 = QIcon()
        icon58.addFile(u":/newPrefix2/Country Flags/dk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon58, "")
        icon59 = QIcon()
        icon59.addFile(u":/newPrefix2/Country Flags/dj.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon59, "")
        icon60 = QIcon()
        icon60.addFile(u":/newPrefix2/Country Flags/do.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon60, "")
        self.Country_Comb.addItem(icon60, "")
        icon61 = QIcon()
        icon61.addFile(u":/newPrefix2/Country Flags/ec.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon61, "")
        icon62 = QIcon()
        icon62.addFile(u":/newPrefix2/Country Flags/eg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon62, "")
        icon63 = QIcon()
        icon63.addFile(u":/newPrefix2/Country Flags/sv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon63, "")
        icon64 = QIcon()
        icon64.addFile(u":/newPrefix2/Country Flags/gq.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon64, "")
        icon65 = QIcon()
        icon65.addFile(u":/newPrefix2/Country Flags/er.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon65, "")
        icon66 = QIcon()
        icon66.addFile(u":/newPrefix2/Country Flags/ee.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon66, "")
        icon67 = QIcon()
        icon67.addFile(u":/newPrefix2/Country Flags/Esw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon67, "")
        icon68 = QIcon()
        icon68.addFile(u":/newPrefix2/Country Flags/et.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon68, "")
        icon69 = QIcon()
        icon69.addFile(u":/newPrefix2/Country Flags/fj.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon69, "")
        icon70 = QIcon()
        icon70.addFile(u":/newPrefix2/Country Flags/fi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon70, "")
        icon71 = QIcon()
        icon71.addFile(u":/newPrefix2/Country Flags/fr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon71, "")
        icon72 = QIcon()
        icon72.addFile(u":/newPrefix2/Country Flags/ga.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon72, "")
        icon73 = QIcon()
        icon73.addFile(u":/newPrefix2/Country Flags/gm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon73, "")
        icon74 = QIcon()
        icon74.addFile(u":/newPrefix2/Country Flags/ge.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon74, "")
        icon75 = QIcon()
        icon75.addFile(u":/newPrefix2/Country Flags/de.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon75, "")
        icon76 = QIcon()
        icon76.addFile(u":/newPrefix2/Country Flags/gh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon76, "")
        icon77 = QIcon()
        icon77.addFile(u":/newPrefix2/Country Flags/gr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon77, "")
        icon78 = QIcon()
        icon78.addFile(u":/newPrefix2/Country Flags/gd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon78, "")
        icon79 = QIcon()
        icon79.addFile(u":/newPrefix2/Country Flags/gt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon79, "")
        icon80 = QIcon()
        icon80.addFile(u":/newPrefix2/Country Flags/gn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon80, "")
        icon81 = QIcon()
        icon81.addFile(u":/newPrefix2/Country Flags/gw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon81, "")
        icon82 = QIcon()
        icon82.addFile(u":/newPrefix2/Country Flags/gy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon82, "")
        icon83 = QIcon()
        icon83.addFile(u":/newPrefix2/Country Flags/ht.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon83, "")
        icon84 = QIcon()
        icon84.addFile(u":/newPrefix2/Country Flags/va.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon84, "")
        icon85 = QIcon()
        icon85.addFile(u":/newPrefix2/Country Flags/hn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon85, "")
        icon86 = QIcon()
        icon86.addFile(u":/newPrefix2/Country Flags/hu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon86, "")
        icon87 = QIcon()
        icon87.addFile(u":/newPrefix2/Country Flags/is.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon87, "")
        icon88 = QIcon()
        icon88.addFile(u":/newPrefix2/Country Flags/in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon88, "")
        icon89 = QIcon()
        icon89.addFile(u":/newPrefix2/Country Flags/id.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon89, "")
        icon90 = QIcon()
        icon90.addFile(u":/newPrefix2/Country Flags/ir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon90, "")
        icon91 = QIcon()
        icon91.addFile(u":/newPrefix2/Country Flags/iq.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon91, "")
        icon92 = QIcon()
        icon92.addFile(u":/newPrefix2/Country Flags/ie.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon92, "")
        icon93 = QIcon()
        icon93.addFile(u":/newPrefix2/Country Flags/il.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon93, "")
        icon94 = QIcon()
        icon94.addFile(u":/newPrefix2/Country Flags/it.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon94, "")
        icon95 = QIcon()
        icon95.addFile(u":/newPrefix2/Country Flags/jm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon95, "")
        icon96 = QIcon()
        icon96.addFile(u":/newPrefix2/Country Flags/jp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon96, "")
        icon97 = QIcon()
        icon97.addFile(u":/newPrefix2/Country Flags/jo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon97, "")
        icon98 = QIcon()
        icon98.addFile(u":/newPrefix2/Country Flags/kz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon98, "")
        icon99 = QIcon()
        icon99.addFile(u":/newPrefix2/Country Flags/ke.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon99, "")
        icon100 = QIcon()
        icon100.addFile(u":/newPrefix2/Country Flags/ki.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon100, "")
        icon101 = QIcon()
        icon101.addFile(u":/newPrefix2/Country Flags/kw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon101, "")
        icon102 = QIcon()
        icon102.addFile(u":/newPrefix2/Country Flags/kg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon102, "")
        icon103 = QIcon()
        icon103.addFile(u":/newPrefix2/Country Flags/la.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon103, "")
        icon104 = QIcon()
        icon104.addFile(u":/newPrefix2/Country Flags/lv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon104, "")
        icon105 = QIcon()
        icon105.addFile(u":/newPrefix2/Country Flags/lb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon105, "")
        icon106 = QIcon()
        icon106.addFile(u":/newPrefix2/Country Flags/ls.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon106, "")
        icon107 = QIcon()
        icon107.addFile(u":/newPrefix2/Country Flags/lr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon107, "")
        icon108 = QIcon()
        icon108.addFile(u":/newPrefix2/Country Flags/ly.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon108, "")
        icon109 = QIcon()
        icon109.addFile(u":/newPrefix2/Country Flags/li.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon109, "")
        icon110 = QIcon()
        icon110.addFile(u":/newPrefix2/Country Flags/lt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon110, "")
        icon111 = QIcon()
        icon111.addFile(u":/newPrefix2/Country Flags/lu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon111, "")
        icon112 = QIcon()
        icon112.addFile(u":/newPrefix2/Country Flags/mg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon112, "")
        icon113 = QIcon()
        icon113.addFile(u":/newPrefix2/Country Flags/mw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon113, "")
        icon114 = QIcon()
        icon114.addFile(u":/newPrefix2/Country Flags/my.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon114, "")
        icon115 = QIcon()
        icon115.addFile(u":/newPrefix2/Country Flags/mv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon115, "")
        icon116 = QIcon()
        icon116.addFile(u":/newPrefix2/Country Flags/ml.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon116, "")
        icon117 = QIcon()
        icon117.addFile(u":/newPrefix2/Country Flags/mt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon117, "")
        icon118 = QIcon()
        icon118.addFile(u":/newPrefix2/Country Flags/mh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon118, "")
        icon119 = QIcon()
        icon119.addFile(u":/newPrefix2/Country Flags/mr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon119, "")
        icon120 = QIcon()
        icon120.addFile(u":/newPrefix2/Country Flags/mu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon120, "")
        icon121 = QIcon()
        icon121.addFile(u":/newPrefix2/Country Flags/mx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon121, "")
        icon122 = QIcon()
        icon122.addFile(u":/newPrefix2/Country Flags/fm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon122, "")
        icon123 = QIcon()
        icon123.addFile(u":/newPrefix2/Country Flags/md.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon123, "")
        icon124 = QIcon()
        icon124.addFile(u":/newPrefix2/Country Flags/mc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon124, "")
        icon125 = QIcon()
        icon125.addFile(u":/newPrefix2/Country Flags/mn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon125, "")
        icon126 = QIcon()
        icon126.addFile(u":/newPrefix2/Country Flags/me.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon126, "")
        icon127 = QIcon()
        icon127.addFile(u":/newPrefix2/Country Flags/ma.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon127, "")
        icon128 = QIcon()
        icon128.addFile(u":/newPrefix2/Country Flags/mz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon128, "")
        icon129 = QIcon()
        icon129.addFile(u":/newPrefix2/Country Flags/mm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon129, "")
        icon130 = QIcon()
        icon130.addFile(u":/newPrefix2/Country Flags/na.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon130, "")
        icon131 = QIcon()
        icon131.addFile(u":/newPrefix2/Country Flags/nr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon131, "")
        icon132 = QIcon()
        icon132.addFile(u":/newPrefix2/Country Flags/np.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon132, "")
        icon133 = QIcon()
        icon133.addFile(u":/newPrefix2/Country Flags/nl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon133, "")
        icon134 = QIcon()
        icon134.addFile(u":/newPrefix2/Country Flags/nz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon134, "")
        icon135 = QIcon()
        icon135.addFile(u":/newPrefix2/Country Flags/ni.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon135, "")
        icon136 = QIcon()
        icon136.addFile(u":/newPrefix2/Country Flags/ne.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon136, "")
        icon137 = QIcon()
        icon137.addFile(u":/newPrefix2/Country Flags/ng.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon137, "")
        icon138 = QIcon()
        icon138.addFile(u":/newPrefix2/Country Flags/kp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon138, "")
        icon139 = QIcon()
        icon139.addFile(u":/newPrefix2/Country Flags/mk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon139, "")
        icon140 = QIcon()
        icon140.addFile(u":/newPrefix2/Country Flags/no.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon140, "")
        icon141 = QIcon()
        icon141.addFile(u":/newPrefix2/Country Flags/om.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon141, "")
        icon142 = QIcon()
        icon142.addFile(u":/newPrefix2/Country Flags/pk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon142, "")
        icon143 = QIcon()
        icon143.addFile(u":/newPrefix2/Country Flags/pw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon143, "")
        icon144 = QIcon()
        icon144.addFile(u":/newPrefix2/Country Flags/ps.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon144, "")
        icon145 = QIcon()
        icon145.addFile(u":/newPrefix2/Country Flags/pa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon145, "")
        icon146 = QIcon()
        icon146.addFile(u":/newPrefix2/Country Flags/pg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon146, "")
        icon147 = QIcon()
        icon147.addFile(u":/newPrefix2/Country Flags/py.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon147, "")
        icon148 = QIcon()
        icon148.addFile(u":/newPrefix2/Country Flags/pe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon148, "")
        icon149 = QIcon()
        icon149.addFile(u":/newPrefix2/Country Flags/ph.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon149, "")
        icon150 = QIcon()
        icon150.addFile(u":/newPrefix2/Country Flags/pl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon150, "")
        icon151 = QIcon()
        icon151.addFile(u":/newPrefix2/Country Flags/pt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon151, "")
        icon152 = QIcon()
        icon152.addFile(u":/newPrefix2/Country Flags/qa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon152, "")
        self.Country_Comb.addItem(icon46, "")
        icon153 = QIcon()
        icon153.addFile(u":/newPrefix2/Country Flags/ru.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon153, "")
        icon154 = QIcon()
        icon154.addFile(u":/newPrefix2/Country Flags/rw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon154, "")
        icon155 = QIcon()
        icon155.addFile(u":/newPrefix2/Country Flags/kn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon155, "")
        self.Country_Comb.addItem(icon87, "")
        icon156 = QIcon()
        icon156.addFile(u":/newPrefix2/Country Flags/vc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon156, "")
        icon157 = QIcon()
        icon157.addFile(u":/newPrefix2/Country Flags/ws.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon157, "")
        icon158 = QIcon()
        icon158.addFile(u":/newPrefix2/Country Flags/sm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon158, "")
        icon159 = QIcon()
        icon159.addFile(u":/newPrefix2/Country Flags/st.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon159, "")
        icon160 = QIcon()
        icon160.addFile(u":/newPrefix2/Country Flags/sa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon160, "")
        icon161 = QIcon()
        icon161.addFile(u":/newPrefix2/Country Flags/sn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon161, "")
        icon162 = QIcon()
        icon162.addFile(u":/newPrefix2/Country Flags/rs.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon162, "")
        icon163 = QIcon()
        icon163.addFile(u":/newPrefix2/Country Flags/sc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon163, "")
        icon164 = QIcon()
        icon164.addFile(u":/newPrefix2/Country Flags/sl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon164, "")
        icon165 = QIcon()
        icon165.addFile(u":/newPrefix2/Country Flags/sg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon165, "")
        icon166 = QIcon()
        icon166.addFile(u":/newPrefix2/Country Flags/sk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon166, "")
        icon167 = QIcon()
        icon167.addFile(u":/newPrefix2/Country Flags/si.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon167, "")
        icon168 = QIcon()
        icon168.addFile(u":/newPrefix2/Country Flags/sb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon168, "")
        icon169 = QIcon()
        icon169.addFile(u":/newPrefix2/Country Flags/so.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon169, "")
        icon170 = QIcon()
        icon170.addFile(u":/newPrefix2/Country Flags/za.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon170, "")
        icon171 = QIcon()
        icon171.addFile(u":/newPrefix2/Country Flags/kr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon171, "")
        icon172 = QIcon()
        icon172.addFile(u":/newPrefix2/Country Flags/ss.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon172, "")
        icon173 = QIcon()
        icon173.addFile(u":/newPrefix2/Country Flags/es.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon173, "")
        icon174 = QIcon()
        icon174.addFile(u":/newPrefix2/Country Flags/lk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon174, "")
        icon175 = QIcon()
        icon175.addFile(u":/newPrefix2/Country Flags/sd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon175, "")
        icon176 = QIcon()
        icon176.addFile(u":/newPrefix2/Country Flags/sr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon176, "")
        icon177 = QIcon()
        icon177.addFile(u":/newPrefix2/Country Flags/se.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon177, "")
        icon178 = QIcon()
        icon178.addFile(u":/newPrefix2/Country Flags/ch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon178, "")
        icon179 = QIcon()
        icon179.addFile(u":/newPrefix2/Country Flags/sy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon179, "")
        icon180 = QIcon()
        icon180.addFile(u":/newPrefix2/Country Flags/tj.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon180, "")
        icon181 = QIcon()
        icon181.addFile(u":/newPrefix2/Country Flags/tz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon181, "")
        icon182 = QIcon()
        icon182.addFile(u":/newPrefix2/Country Flags/th.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon182, "")
        icon183 = QIcon()
        icon183.addFile(u":/newPrefix2/Country Flags/tl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon183, "")
        icon184 = QIcon()
        icon184.addFile(u":/newPrefix2/Country Flags/tg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon184, "")
        icon185 = QIcon()
        icon185.addFile(u":/newPrefix2/Country Flags/to.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon185, "")
        icon186 = QIcon()
        icon186.addFile(u":/newPrefix2/Country Flags/tt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon186, "")
        icon187 = QIcon()
        icon187.addFile(u":/newPrefix2/Country Flags/tn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon187, "")
        icon188 = QIcon()
        icon188.addFile(u":/newPrefix2/Country Flags/tr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon188, "")
        icon189 = QIcon()
        icon189.addFile(u":/newPrefix2/Country Flags/tm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon189, "")
        icon190 = QIcon()
        icon190.addFile(u":/newPrefix2/Country Flags/tv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon190, "")
        icon191 = QIcon()
        icon191.addFile(u":/newPrefix2/Country Flags/ug.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon191, "")
        icon192 = QIcon()
        icon192.addFile(u":/newPrefix2/Country Flags/ua.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon192, "")
        icon193 = QIcon()
        icon193.addFile(u":/newPrefix2/Country Flags/ae.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon193, "")
        icon194 = QIcon()
        icon194.addFile(u":/newPrefix2/Country Flags/gb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon194, "")
        icon195 = QIcon()
        icon195.addFile(u":/newPrefix2/Country Flags/us.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon195, "")
        icon196 = QIcon()
        icon196.addFile(u":/newPrefix2/Country Flags/uy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon196, "")
        icon197 = QIcon()
        icon197.addFile(u":/newPrefix2/Country Flags/uz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon197, "")
        icon198 = QIcon()
        icon198.addFile(u":/newPrefix2/Country Flags/vu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon198, "")
        icon199 = QIcon()
        icon199.addFile(u":/newPrefix2/Country Flags/ve.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon199, "")
        icon200 = QIcon()
        icon200.addFile(u":/newPrefix2/Country Flags/vn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon200, "")
        icon201 = QIcon()
        icon201.addFile(u":/newPrefix2/Country Flags/ye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon201, "")
        icon202 = QIcon()
        icon202.addFile(u":/newPrefix2/Country Flags/zm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon202, "")
        icon203 = QIcon()
        icon203.addFile(u":/newPrefix2/Country Flags/zw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Country_Comb.addItem(icon203, "")
        self.Country_Comb.setObjectName(u"Country_Comb")
        self.Country_Comb.setGeometry(QRect(670, 120, 301, 31))
        self.Country_Comb.setFont(font8)
        self.Country_Comb.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(250, 250, 250);\n"
"    border: 1px solid rgb(66, 66, 66);\n"
"    border-radius: 3px;\n"
"    padding: 0 0 0 8px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/newPrefix/icons/down-arrow.png);\n"
"	width:14px;\n"
"	height:14px;\n"
"	margin-right: 15px;\n"
"}\n"
"\n"
"QComboBox QListView { \n"
"	background-color: rgb(35, 35, 35);	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Country_Comb.setMaxVisibleItems(20)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(510, 130, 121, 21))
        self.label_6.setFont(font12)
        self.label_6.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 90, 101, 16))
        font13 = QFont()
        font13.setFamilies([u"PT Simple Bold Ruled"])
        font13.setPointSize(12)
        font13.setBold(True)
        self.label_8.setFont(font13)
        self.label_8.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(510, 90, 91, 16))
        self.label_15.setFont(font12)
        self.label_15.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 130, 61, 16))
        self.label_16.setFont(font12)
        self.label_16.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.Reg_username = QLineEdit(self.frame_2)
        self.Reg_username.setObjectName(u"Reg_username")
        self.Reg_username.setGeometry(QRect(180, 160, 301, 31))
        self.Reg_username.setMinimumSize(QSize(231, 0))
        self.Reg_username.setFont(font7)
        self.Reg_username.setAcceptDrops(True)
        self.Reg_username.setStyleSheet(u"")
        self.Reg_username.setFrame(True)
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 170, 91, 16))
        self.label_17.setFont(font12)
        self.label_17.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 210, 81, 16))
        self.label_18.setFont(font12)
        self.label_18.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.Reg_confirm_password = QLineEdit(self.frame_2)
        self.Reg_confirm_password.setObjectName(u"Reg_confirm_password")
        self.Reg_confirm_password.setGeometry(QRect(670, 200, 301, 31))
        self.Reg_confirm_password.setMinimumSize(QSize(231, 0))
        self.Reg_confirm_password.setFont(font8)
        self.Reg_confirm_password.setAcceptDrops(True)
        self.Reg_confirm_password.setStyleSheet(u"")
        self.Reg_confirm_password.setEchoMode(QLineEdit.Password)
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(510, 210, 151, 16))
        self.label_19.setFont(font12)
        self.label_19.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.Reg_password = QLineEdit(self.frame_2)
        self.Reg_password.setObjectName(u"Reg_password")
        self.Reg_password.setGeometry(QRect(180, 200, 301, 31))
        self.Reg_password.setMinimumSize(QSize(231, 0))
        self.Reg_password.setFont(font8)
        self.Reg_password.setAcceptDrops(True)
        self.Reg_password.setStyleSheet(u"")
        self.Reg_password.setEchoMode(QLineEdit.Password)
        self.back2Login_Button = QPushButton(self.frame_2)
        self.back2Login_Button.setObjectName(u"back2Login_Button")
        self.back2Login_Button.setGeometry(QRect(20, 390, 241, 23))
        self.back2Login_Button.setFont(font2)
        self.back2Login_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.back2Login_Button.setStyleSheet(u"QPushButton{\n"
"  background-color: 0;\n"
" color: rgb(93, 173, 226);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 3px;\n"
"}")
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(320, 0, 331, 41))
        font14 = QFont()
        font14.setFamilies([u"MS Shell Dlg 2"])
        font14.setPointSize(20)
        font14.setBold(True)
        self.label_20.setFont(font14)
        self.label_20.setStyleSheet(u"background-color: 0;\n"
"color: qlineargradient(spread:pad, x1:0.961, y1:0.091, x2:1, y2:0.00568182, stop:0.409091 rgba(0, 175, 178, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.Reg_confirm_password.raise_()
        self.Reg_password.raise_()
        self.Reg_Btn.raise_()
        self.Reg_First_username.raise_()
        self.Reg_email.raise_()
        self.Reg_last_username.raise_()
        self.radio_female_Button.raise_()
        self.radio_male_Button.raise_()
        self.Country_Comb.raise_()
        self.label_8.raise_()
        self.Reg_username.raise_()
        self.back2Login_Button.raise_()
        self.label_20.raise_()
        self.log_win_tab.addWidget(self.registration)
        self.forget_pass = QWidget()
        self.forget_pass.setObjectName(u"forget_pass")
        self.frame_3 = QFrame(self.forget_pass)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(240, 20, 531, 381))
        self.frame_3.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_3.setStyleSheet(u"QFrame#frame_2{\n"
"border-radius:5px;\n"
"background-color: 0;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.Submit_Btn = QPushButton(self.frame_3)
        self.Submit_Btn.setObjectName(u"Submit_Btn")
        self.Submit_Btn.setGeometry(QRect(210, 270, 251, 41))
        self.Submit_Btn.setFont(font9)
        self.Submit_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Submit_Btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.Submit_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 168, 83);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgb(163, 228, 215);\n"
"}")
        self.Forget_Reg_username = QLineEdit(self.frame_3)
        self.Forget_Reg_username.setObjectName(u"Forget_Reg_username")
        self.Forget_Reg_username.setGeometry(QRect(210, 100, 251, 35))
        self.Forget_Reg_username.setMinimumSize(QSize(231, 0))
        self.Forget_Reg_username.setFont(font7)
        self.Forget_Reg_username.setAcceptDrops(True)
        self.Forget_Reg_username.setStyleSheet(u"")
        self.Forget_Reg_username.setFrame(True)
        self.Forget_Reg_email = QLineEdit(self.frame_3)
        self.Forget_Reg_email.setObjectName(u"Forget_Reg_email")
        self.Forget_Reg_email.setGeometry(QRect(210, 141, 251, 35))
        self.Forget_Reg_email.setMinimumSize(QSize(231, 0))
        self.Forget_Reg_email.setFont(font8)
        self.Forget_Reg_email.setAcceptDrops(True)
        self.Forget_Reg_email.setStyleSheet(u"")
        self.Forget_Reg_email.setEchoMode(QLineEdit.Normal)
        self.back2Login_Button_2 = QPushButton(self.frame_3)
        self.back2Login_Button_2.setObjectName(u"back2Login_Button_2")
        self.back2Login_Button_2.setGeometry(QRect(20, 333, 121, 23))
        self.back2Login_Button_2.setFont(font2)
        self.back2Login_Button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.back2Login_Button_2.setStyleSheet(u"QPushButton{\n"
"  background-color: 0;\n"
" color: rgb(93, 173, 226);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:5px;\n"
"	padding-top: 3px;\n"
"}")
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 110, 91, 16))
        font15 = QFont()
        font15.setFamilies([u"PT Simple Bold Ruled"])
        font15.setPointSize(11)
        font15.setBold(True)
        self.label_21.setFont(font15)
        self.label_21.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 150, 61, 16))
        font16 = QFont()
        font16.setPointSize(11)
        font16.setBold(True)
        self.label_22.setFont(font16)
        self.label_22.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 190, 131, 16))
        self.label_23.setFont(font16)
        self.label_23.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.Confirm_Forget_New_password = QLineEdit(self.frame_3)
        self.Confirm_Forget_New_password.setObjectName(u"Confirm_Forget_New_password")
        self.Confirm_Forget_New_password.setGeometry(QRect(210, 220, 251, 35))
        self.Confirm_Forget_New_password.setMinimumSize(QSize(231, 0))
        self.Confirm_Forget_New_password.setFont(font8)
        self.Confirm_Forget_New_password.setAcceptDrops(True)
        self.Confirm_Forget_New_password.setStyleSheet(u"")
        self.Confirm_Forget_New_password.setEchoMode(QLineEdit.Password)
        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 230, 181, 20))
        self.label_24.setFont(font16)
        self.label_24.setStyleSheet(u"color: rgb(245, 245, 245);")
        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(110, 10, 271, 61))
        self.label_25.setFont(font14)
        self.label_25.setStyleSheet(u"background-color: 0;\n"
"color: qlineargradient(spread:pad, x1:0.961, y1:0.091, x2:1, y2:0.00568182, stop:0.409091 rgba(0, 175, 178, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Forget_New_password = QLineEdit(self.frame_3)
        self.Forget_New_password.setObjectName(u"Forget_New_password")
        self.Forget_New_password.setGeometry(QRect(210, 182, 251, 31))
        self.Forget_New_password.setMinimumSize(QSize(231, 0))
        self.Forget_New_password.setFont(font8)
        self.Forget_New_password.setAcceptDrops(True)
        self.Forget_New_password.setStyleSheet(u"")
        self.Forget_New_password.setEchoMode(QLineEdit.Password)
        self.back2Login_Button_2.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.Confirm_Forget_New_password.raise_()
        self.Forget_New_password.raise_()
        self.Submit_Btn.raise_()
        self.Forget_Reg_username.raise_()
        self.Forget_Reg_email.raise_()
        self.log_win_tab.addWidget(self.forget_pass)
        self.Container_tab.addWidget(self.Home_tab)
        self.MediaTek_tab = QWidget()
        self.MediaTek_tab.setObjectName(u"MediaTek_tab")
        self.tabWidget = QTabWidget(self.MediaTek_tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 2, 551, 411))
        font17 = QFont()
        font17.setBold(True)
        self.tabWidget.setFont(font17)
        self.tabWidget.setStyleSheet(u"QTabWidget #tabWidget {\n"
"background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border: 1px solid rgb(95, 95, 95);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"	background-color:rgb(26, 26, 26);\n"
"	color: rgb(231, 231, 231);\n"
"   \n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    min-width: 8ex;\n"
"    padding: 7px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(45, 45, 45, 255), stop:1 rgba(97, 130, 171, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
""
                        "    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 531, 321))
        self.groupBox_2.setFont(font8)
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"    border:1px solid rgb(95, 95, 95);\n"
"    border-radius:2px;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-top: 5ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 5 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(179, 55, 113, 255), stop:1 rgba(219, 78, 117, 255));\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QRadioButton {\n"
"	color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    \n"
"	image: url(:/newPrefix/icons/radio-button.png);\n"
"}\n"
"")
        self.read_info_radioButton = QRadioButton(self.groupBox_2)
        self.read_info_radioButton.setObjectName(u"read_info_radioButton")
        self.read_info_radioButton.setGeometry(QRect(20, 50, 141, 20))
        self.read_info_radioButton.setFont(font7)
        self.read_info_radioButton.setStyleSheet(u"")
        icon204 = QIcon()
        icon204.addFile(u":/newPrefix/icons/information.png", QSize(), QIcon.Normal, QIcon.Off)
        self.read_info_radioButton.setIcon(icon204)
        self.UL_radioButton = QRadioButton(self.groupBox_2)
        self.UL_radioButton.setObjectName(u"UL_radioButton")
        self.UL_radioButton.setGeometry(QRect(20, 140, 191, 20))
        self.UL_radioButton.setFont(font7)
        icon205 = QIcon()
        icon205.addFile(u":/newPrefix/icons/unlocked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.UL_radioButton.setIcon(icon205)
        self.RL_radioButton = QRadioButton(self.groupBox_2)
        self.RL_radioButton.setObjectName(u"RL_radioButton")
        self.RL_radioButton.setGeometry(QRect(20, 170, 181, 20))
        self.RL_radioButton.setFont(font7)
        icon206 = QIcon()
        icon206.addFile(u":/newPrefix/icons/lock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RL_radioButton.setIcon(icon206)
        self.factory_reset_radioButton = QRadioButton(self.groupBox_2)
        self.factory_reset_radioButton.setObjectName(u"factory_reset_radioButton")
        self.factory_reset_radioButton.setGeometry(QRect(20, 110, 141, 20))
        self.factory_reset_radioButton.setFont(font7)
        icon207 = QIcon()
        icon207.addFile(u":/newPrefix/icons/circle-of-two.png", QSize(), QIcon.Normal, QIcon.Off)
        self.factory_reset_radioButton.setIcon(icon207)
        self.FRP_radioButton = QRadioButton(self.groupBox_2)
        self.FRP_radioButton.setObjectName(u"FRP_radioButton")
        self.FRP_radioButton.setGeometry(QRect(20, 200, 141, 20))
        self.FRP_radioButton.setFont(font7)
        icon208 = QIcon()
        icon208.addFile(u":/newPrefix/icons/clean.png", QSize(), QIcon.Normal, QIcon.Off)
        self.FRP_radioButton.setIcon(icon208)
        self.auth_bypass_radioButton = QRadioButton(self.groupBox_2)
        self.auth_bypass_radioButton.setObjectName(u"auth_bypass_radioButton")
        self.auth_bypass_radioButton.setGeometry(QRect(20, 80, 141, 20))
        self.auth_bypass_radioButton.setFont(font7)
        self.auth_bypass_radioButton.setStyleSheet(u"")
        icon209 = QIcon()
        icon209.addFile(u":/newPrefix/icons/shield.png", QSize(), QIcon.Normal, QIcon.Off)
        self.auth_bypass_radioButton.setIcon(icon209)
        self.lockbutton = QPushButton(self.groupBox_2)
        self.lockbutton.setObjectName(u"lockbutton")
        self.lockbutton.setGeometry(QRect(130, 250, 238, 24))
        self.unlockbutton = QPushButton(self.groupBox_2)
        self.unlockbutton.setObjectName(u"unlockbutton")
        self.unlockbutton.setGeometry(QRect(130, 280, 238, 24))
        self.Start_BTN = QPushButton(self.tab)
        self.Start_BTN.setObjectName(u"Start_BTN")
        self.Start_BTN.setGeometry(QRect(10, 340, 531, 31))
        self.Start_BTN.setFont(font17)
        self.Start_BTN.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 168, 83);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        icon210 = QIcon()
        icon210.addFile(u":/newPrefix/icons/lightning-bolt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start_BTN.setIcon(icon210)
        icon211 = QIcon()
        icon211.addFile(u":/newPrefix/icons/google.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon211, "")
        self.readtab = QWidget()
        self.readtab.setObjectName(u"readtab")
        self.readselectallcheckbox = QCheckBox(self.readtab)
        self.readselectallcheckbox.setObjectName(u"readselectallcheckbox")
        self.readselectallcheckbox.setGeometry(QRect(12, 56, 16, 20))
        self.readselectallcheckbox.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.readDumpGPTCheckbox = QCheckBox(self.readtab)
        self.readDumpGPTCheckbox.setObjectName(u"readDumpGPTCheckbox")
        self.readDumpGPTCheckbox.setGeometry(QRect(10, 350, 95, 20))
        self.readDumpGPTCheckbox.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.readpartitionsbtn = QPushButton(self.readtab)
        self.readpartitionsbtn.setObjectName(u"readpartitionsbtn")
        self.readpartitionsbtn.setGeometry(QRect(440, 10, 101, 31))
        self.readpartitionsbtn.setFont(font17)
        self.readpartitionsbtn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 168, 83);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        icon212 = QIcon()
        icon212.addFile(u":/newPrefix/icons/diskette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.readpartitionsbtn.setIcon(icon212)
        self.readtitle = QLabel(self.readtab)
        self.readtitle.setObjectName(u"readtitle")
        self.readtitle.setGeometry(QRect(390, 350, 151, 20))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.readtitle.sizePolicy().hasHeightForWidth())
        self.readtitle.setSizePolicy(sizePolicy1)
        self.readtitle.setMinimumSize(QSize(0, 20))
        self.readtitle.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.readtitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.readpartitionList = QTableWidget(self.readtab)
        if (self.readpartitionList.columnCount() < 6):
            self.readpartitionList.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.readpartitionList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.readpartitionList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.readpartitionList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.readpartitionList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.readpartitionList.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.readpartitionList.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.readpartitionList.setObjectName(u"readpartitionList")
        self.readpartitionList.setGeometry(QRect(10, 50, 531, 291))
        self.readpartitionList.setAutoFillBackground(False)
        self.readpartitionList.setStyleSheet(u"QTableWidget {\n"
"	background-color: rgb(38, 38, 38);\n"
"	color: rgb(255, 255, 255);\n"
"	gridline-color:rgb(40, 55, 71);\n"
"	alternate-background-color:rgb(40, 55, 71);\n"
"	 selection-background-color:rgb(184, 233, 148);\n"
"    }\n"
"\n"
"QHeaderView::section{\n"
"	background-color:rgb(26, 26, 26);\n"
"	border:1px solid rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.readpartitionList.setFrameShape(QFrame.Box)
        self.readpartitionList.setFrameShadow(QFrame.Raised)
        self.readpartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.readpartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.readpartitionList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.readpartitionList.setAutoScroll(True)
        self.readpartitionList.setProperty("showDropIndicator", True)
        self.readpartitionList.setDragDropOverwriteMode(True)
        self.readpartitionList.setAlternatingRowColors(True)
        self.readpartitionList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.readpartitionList.setTextElideMode(Qt.ElideLeft)
        self.readpartitionList.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.readpartitionList.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.readpartitionList.setShowGrid(True)
        self.readpartitionList.setGridStyle(Qt.SolidLine)
        self.readpartitionList.setSortingEnabled(False)
        self.readpartitionList.setCornerButtonEnabled(True)
        self.readpartitionList.horizontalHeader().setCascadingSectionResizes(False)
        self.readpartitionList.verticalHeader().setVisible(False)
        self.Checkpartitionsbtn = QPushButton(self.readtab)
        self.Checkpartitionsbtn.setObjectName(u"Checkpartitionsbtn")
        self.Checkpartitionsbtn.setGeometry(QRect(10, 10, 141, 31))
        self.Checkpartitionsbtn.setFont(font17)
        self.Checkpartitionsbtn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 152, 219);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        self.Checkpartitionsbtn.setIcon(icon210)
        icon213 = QIcon()
        icon213.addFile(u":/newPrefix/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.readtab, icon213, "")
        self.readDumpGPTCheckbox.raise_()
        self.readpartitionsbtn.raise_()
        self.readtitle.raise_()
        self.readpartitionList.raise_()
        self.readselectallcheckbox.raise_()
        self.Checkpartitionsbtn.raise_()
        self.writetab = QWidget()
        self.writetab.setObjectName(u"writetab")
        self.writepartitionList = QScrollArea(self.writetab)
        self.writepartitionList.setObjectName(u"writepartitionList")
        self.writepartitionList.setGeometry(QRect(10, 50, 531, 291))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.writepartitionList.sizePolicy().hasHeightForWidth())
        self.writepartitionList.setSizePolicy(sizePolicy2)
        self.writepartitionList.setMinimumSize(QSize(0, 280))
        self.writepartitionList.setStyleSheet(u"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);")
        self.writepartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.writepartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.writepartitionList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.writepartitionList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 529, 289))
        self.writepartitionList.setWidget(self.scrollAreaWidgetContents_2)
        self.writepartbtn = QPushButton(self.writetab)
        self.writepartbtn.setObjectName(u"writepartbtn")
        self.writepartbtn.setGeometry(QRect(400, 10, 141, 31))
        self.writepartbtn.setFont(font17)
        self.writepartbtn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 168, 83);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        icon214 = QIcon()
        icon214.addFile(u":/newPrefix/icons/write.png", QSize(), QIcon.Normal, QIcon.Off)
        self.writepartbtn.setIcon(icon214)
        self.writeselectfromdir = QPushButton(self.writetab)
        self.writeselectfromdir.setObjectName(u"writeselectfromdir")
        self.writeselectfromdir.setGeometry(QRect(10, 10, 131, 31))
        self.writeselectfromdir.setFont(font17)
        self.writeselectfromdir.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(9, 132, 227);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(85, 161, 227);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        icon215 = QIcon()
        icon215.addFile(u":/newPrefix/icons/click.png", QSize(), QIcon.Normal, QIcon.Off)
        self.writeselectfromdir.setIcon(icon215)
        self.writetitle = QLabel(self.writetab)
        self.writetitle.setObjectName(u"writetitle")
        self.writetitle.setGeometry(QRect(10, 350, 311, 20))
        sizePolicy1.setHeightForWidth(self.writetitle.sizePolicy().hasHeightForWidth())
        self.writetitle.setSizePolicy(sizePolicy1)
        self.writetitle.setMinimumSize(QSize(0, 20))
        self.writetitle.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.writetitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        icon216 = QIcon()
        icon216.addFile(u":/newPrefix/icons/pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.writetab, icon216, "")
        self.erasetab = QWidget()
        self.erasetab.setObjectName(u"erasetab")
        self.erasepartitionList = QScrollArea(self.erasetab)
        self.erasepartitionList.setObjectName(u"erasepartitionList")
        self.erasepartitionList.setGeometry(QRect(10, 50, 531, 291))
        sizePolicy2.setHeightForWidth(self.erasepartitionList.sizePolicy().hasHeightForWidth())
        self.erasepartitionList.setSizePolicy(sizePolicy2)
        self.erasepartitionList.setMinimumSize(QSize(0, 280))
        self.erasepartitionList.setStyleSheet(u"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);")
        self.erasepartitionList.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.erasepartitionList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.erasepartitionList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.erasepartitionList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 529, 289))
        self.erasepartitionList.setWidget(self.scrollAreaWidgetContents_3)
        self.erasepartitionsbtn = QPushButton(self.erasetab)
        self.erasepartitionsbtn.setObjectName(u"erasepartitionsbtn")
        self.erasepartitionsbtn.setGeometry(QRect(420, 10, 121, 31))
        self.erasepartitionsbtn.setFont(font17)
        self.erasepartitionsbtn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(214, 48, 49);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(209, 109, 114);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        icon217 = QIcon()
        icon217.addFile(u":/newPrefix/icons/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.erasepartitionsbtn.setIcon(icon217)
        self.eraseselectallpartitionscheckbox = QCheckBox(self.erasetab)
        self.eraseselectallpartitionscheckbox.setObjectName(u"eraseselectallpartitionscheckbox")
        self.eraseselectallpartitionscheckbox.setGeometry(QRect(10, 20, 221, 20))
        self.eraseselectallpartitionscheckbox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.erasetitle = QLabel(self.erasetab)
        self.erasetitle.setObjectName(u"erasetitle")
        self.erasetitle.setGeometry(QRect(10, 350, 231, 20))
        sizePolicy1.setHeightForWidth(self.erasetitle.sizePolicy().hasHeightForWidth())
        self.erasetitle.setSizePolicy(sizePolicy1)
        self.erasetitle.setMinimumSize(QSize(0, 20))
        self.erasetitle.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.erasetitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        icon218 = QIcon()
        icon218.addFile(u":/newPrefix/icons/eraser1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.erasetab, icon218, "")
        self.Stop_BTN = QPushButton(self.MediaTek_tab)
        self.Stop_BTN.setObjectName(u"Stop_BTN")
        self.Stop_BTN.setGeometry(QRect(980, 370, 81, 37))
        self.Stop_BTN.setFont(font17)
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
        icon219 = QIcon()
        icon219.addFile(u":/newPrefix/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stop_BTN.setIcon(icon219)
        self.Stop_BTN.setIconSize(QSize(12, 12))
        self.fullProgress = QProgressBar(self.MediaTek_tab)
        self.fullProgress.setObjectName(u"fullProgress")
        self.fullProgress.setGeometry(QRect(570, 390, 401, 16))
        self.fullProgress.setValue(100)
        self.fullProgress.setAlignment(Qt.AlignCenter)
        self.partProgress = QProgressBar(self.MediaTek_tab)
        self.partProgress.setObjectName(u"partProgress")
        self.partProgress.setGeometry(QRect(570, 370, 401, 16))
        self.partProgress.setStyleSheet(u"")
        self.partProgress.setValue(100)
        self.partProgress.setAlignment(Qt.AlignCenter)
        self.logBox = QTextEdit(self.MediaTek_tab)
        self.logBox.setObjectName(u"logBox")
        self.logBox.setGeometry(QRect(570, 35, 491, 331))
        font18 = QFont()
        font18.setFamilies([u"Roboto"])
        font18.setBold(True)
        font18.setHintingPreference(QFont.PreferVerticalHinting)
        self.logBox.setFont(font18)
        self.logBox.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.logBox.setStyleSheet(u"QTextEdit {\n"
"border: 1px solid rgb(95, 95, 95);\n"
"border-radius:2px;	\n"
"color: rgb(247, 247, 247);\n"
"background-color: rgb(50, 50, 50);\n"
"padding: 5px;\n"
"}")
        self.logBox.setInputMethodHints(Qt.ImhMultiLine)
        self.logBox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.logBox.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.logBox.setLineWrapMode(QTextEdit.NoWrap)
        self.logBox.setReadOnly(True)
        self.logBox.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.Open_Devmgmt = QPushButton(self.MediaTek_tab)
        self.Open_Devmgmt.setObjectName(u"Open_Devmgmt")
        self.Open_Devmgmt.setGeometry(QRect(570, 4, 141, 29))
        self.Open_Devmgmt.setFont(font17)
        self.Open_Devmgmt.setStyleSheet(u"QPushButton{\n"
"  background-color:rgb(26, 26, 26);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(45, 45, 45, 255), stop:1 rgba(97, 130, 171, 255));\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}\n"
"")
        self.Open_Devmgmt.setIcon(icon210)
        self.Container_tab.addWidget(self.MediaTek_tab)
        self.Huawei_tab = QWidget()
        self.Huawei_tab.setObjectName(u"Huawei_tab")
        self.label_10 = QLabel(self.Huawei_tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(330, 160, 311, 81))
        font19 = QFont()
        font19.setPointSize(45)
        self.label_10.setFont(font19)
        self.Container_tab.addWidget(self.Huawei_tab)
        self.Qualcomm_tab = QWidget()
        self.Qualcomm_tab.setObjectName(u"Qualcomm_tab")
        self.label_11 = QLabel(self.Qualcomm_tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(340, 160, 411, 81))
        self.label_11.setFont(font19)
        self.Container_tab.addWidget(self.Qualcomm_tab)
        self.Samsung_tab = QWidget()
        self.Samsung_tab.setObjectName(u"Samsung_tab")
        self.label_12 = QLabel(self.Samsung_tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(330, 160, 411, 81))
        self.label_12.setFont(font19)
        self.Container_tab.addWidget(self.Samsung_tab)
        self.Android_tab = QWidget()
        self.Android_tab.setObjectName(u"Android_tab")
        self.label_13 = QLabel(self.Android_tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(340, 150, 411, 81))
        self.label_13.setFont(font19)
        self.Container_tab.addWidget(self.Android_tab)
        self.About_tab = QWidget()
        self.About_tab.setObjectName(u"About_tab")
        self.label_14 = QLabel(self.About_tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(450, 170, 291, 81))
        self.label_14.setFont(font19)
        self.Container_tab.addWidget(self.About_tab)
        self.label_26 = QLabel(self.main_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(610, 144, 241, 21))
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"background-color: rgb(26, 26, 26);\n"
"color: rgb(52, 168, 83);")

        self.gridLayout.addWidget(self.main_frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.MediaTek_Btn.setDefault(False)
        self.Container_tab.setCurrentIndex(1)
        self.log_win_tab.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


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
        self.Home_Btn.setText("")
#if QT_CONFIG(tooltip)
        self.MediaTek_Btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.MediaTek_Btn.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.MediaTek_Btn.setText("")
#if QT_CONFIG(tooltip)
        self.Qualcomm_Btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Qualcomm_Btn.setText("")
#if QT_CONFIG(tooltip)
        self.TestPoints.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.TestPoints.setText("")
#if QT_CONFIG(tooltip)
        self.About_Btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.About_Btn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"T-REX", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" UNIVERSAL TOOL", None))
#if QT_CONFIG(tooltip)
        self.Samsung_Btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Samsung_Btn.setText("")
#if QT_CONFIG(tooltip)
        self.Huawei_Btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Huawei_Btn.setText("")
#if QT_CONFIG(tooltip)
        self.Android_Btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Android_Btn.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO LAROUSSI T-REX TOOL V1.0 BETA                                                    ", None))
        self.partProgressText.setText("")
        self.fullProgressText.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"LOGIN T-REX SYSTEM", None))
        self.login_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Username", None))
        self.login_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Password", None))
        self.Forget_Pass_Button.setText(QCoreApplication.translate("MainWindow", u"Forget Password ?", None))
#if QT_CONFIG(tooltip)
        self.login_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Laroussi ", None))
#endif // QT_CONFIG(tooltip)
        self.login_Btn.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.SignUp_Button.setText(QCoreApplication.translate("MainWindow", u"Sign up Now", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Don't have an account!!!", None))
#if QT_CONFIG(tooltip)
        self.Reg_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Laroussi ", None))
#endif // QT_CONFIG(tooltip)
        self.Reg_Btn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.Reg_First_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your First Name ...", None))
        self.Reg_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXXX@Email.com", None))
        self.Reg_last_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Last Name ...", None))
        self.radio_female_Button.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.radio_male_Button.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Select Gender", None))
        self.Country_Comb.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Country", None))
        self.Country_Comb.setItemText(1, QCoreApplication.translate("MainWindow", u"Afghanistan", None))
        self.Country_Comb.setItemText(2, QCoreApplication.translate("MainWindow", u"Albania", None))
        self.Country_Comb.setItemText(3, QCoreApplication.translate("MainWindow", u"Algeria", None))
        self.Country_Comb.setItemText(4, QCoreApplication.translate("MainWindow", u"Andorra", None))
        self.Country_Comb.setItemText(5, QCoreApplication.translate("MainWindow", u"Angola", None))
        self.Country_Comb.setItemText(6, QCoreApplication.translate("MainWindow", u"Antigua and Barbuda	", None))
        self.Country_Comb.setItemText(7, QCoreApplication.translate("MainWindow", u"Argentina", None))
        self.Country_Comb.setItemText(8, QCoreApplication.translate("MainWindow", u"Armenia", None))
        self.Country_Comb.setItemText(9, QCoreApplication.translate("MainWindow", u"Australia", None))
        self.Country_Comb.setItemText(10, QCoreApplication.translate("MainWindow", u"Austria", None))
        self.Country_Comb.setItemText(11, QCoreApplication.translate("MainWindow", u"Azerbaijan", None))
        self.Country_Comb.setItemText(12, QCoreApplication.translate("MainWindow", u"Bahamas", None))
        self.Country_Comb.setItemText(13, QCoreApplication.translate("MainWindow", u"Bahrain", None))
        self.Country_Comb.setItemText(14, QCoreApplication.translate("MainWindow", u"Bangladesh", None))
        self.Country_Comb.setItemText(15, QCoreApplication.translate("MainWindow", u"Barbados", None))
        self.Country_Comb.setItemText(16, QCoreApplication.translate("MainWindow", u"Belarus", None))
        self.Country_Comb.setItemText(17, QCoreApplication.translate("MainWindow", u"Belgium", None))
        self.Country_Comb.setItemText(18, QCoreApplication.translate("MainWindow", u"Belize", None))
        self.Country_Comb.setItemText(19, QCoreApplication.translate("MainWindow", u"Benin", None))
        self.Country_Comb.setItemText(20, QCoreApplication.translate("MainWindow", u"Bhutan", None))
        self.Country_Comb.setItemText(21, QCoreApplication.translate("MainWindow", u"Bolivia", None))
        self.Country_Comb.setItemText(22, QCoreApplication.translate("MainWindow", u"Bosnia and Herzegovina", None))
        self.Country_Comb.setItemText(23, QCoreApplication.translate("MainWindow", u"Botswana", None))
        self.Country_Comb.setItemText(24, QCoreApplication.translate("MainWindow", u"Brazil", None))
        self.Country_Comb.setItemText(25, QCoreApplication.translate("MainWindow", u"Brunei", None))
        self.Country_Comb.setItemText(26, QCoreApplication.translate("MainWindow", u"Bulgaria", None))
        self.Country_Comb.setItemText(27, QCoreApplication.translate("MainWindow", u"Burkina Faso", None))
        self.Country_Comb.setItemText(28, QCoreApplication.translate("MainWindow", u"Burundi", None))
        self.Country_Comb.setItemText(29, QCoreApplication.translate("MainWindow", u"C\u00f4te d'Ivoire", None))
        self.Country_Comb.setItemText(30, QCoreApplication.translate("MainWindow", u"Cabo Verde", None))
        self.Country_Comb.setItemText(31, QCoreApplication.translate("MainWindow", u"Cambodia", None))
        self.Country_Comb.setItemText(32, QCoreApplication.translate("MainWindow", u"Cameroon", None))
        self.Country_Comb.setItemText(33, QCoreApplication.translate("MainWindow", u"Canada", None))
        self.Country_Comb.setItemText(34, QCoreApplication.translate("MainWindow", u"Central African Republic", None))
        self.Country_Comb.setItemText(35, QCoreApplication.translate("MainWindow", u"Chad", None))
        self.Country_Comb.setItemText(36, QCoreApplication.translate("MainWindow", u"Chile", None))
        self.Country_Comb.setItemText(37, QCoreApplication.translate("MainWindow", u"China", None))
        self.Country_Comb.setItemText(38, QCoreApplication.translate("MainWindow", u"Colombia", None))
        self.Country_Comb.setItemText(39, QCoreApplication.translate("MainWindow", u"Comoros", None))
        self.Country_Comb.setItemText(40, QCoreApplication.translate("MainWindow", u"Congo (Congo-Brazzaville)", None))
        self.Country_Comb.setItemText(41, QCoreApplication.translate("MainWindow", u"Costa Rica", None))
        self.Country_Comb.setItemText(42, QCoreApplication.translate("MainWindow", u"Croatia", None))
        self.Country_Comb.setItemText(43, QCoreApplication.translate("MainWindow", u"Cuba", None))
        self.Country_Comb.setItemText(44, QCoreApplication.translate("MainWindow", u"Cyprus", None))
        self.Country_Comb.setItemText(45, QCoreApplication.translate("MainWindow", u"Czechia (Czech Republic)", None))
        self.Country_Comb.setItemText(46, QCoreApplication.translate("MainWindow", u"Democratic Republic of the Congo", None))
        self.Country_Comb.setItemText(47, QCoreApplication.translate("MainWindow", u"Denmark", None))
        self.Country_Comb.setItemText(48, QCoreApplication.translate("MainWindow", u"Djibouti", None))
        self.Country_Comb.setItemText(49, QCoreApplication.translate("MainWindow", u"Dominica", None))
        self.Country_Comb.setItemText(50, QCoreApplication.translate("MainWindow", u"Dominican Republic", None))
        self.Country_Comb.setItemText(51, QCoreApplication.translate("MainWindow", u"Ecuador", None))
        self.Country_Comb.setItemText(52, QCoreApplication.translate("MainWindow", u"Egypt", None))
        self.Country_Comb.setItemText(53, QCoreApplication.translate("MainWindow", u"El Salvador", None))
        self.Country_Comb.setItemText(54, QCoreApplication.translate("MainWindow", u"Equatorial Guinea", None))
        self.Country_Comb.setItemText(55, QCoreApplication.translate("MainWindow", u"Eritrea", None))
        self.Country_Comb.setItemText(56, QCoreApplication.translate("MainWindow", u"Estonia", None))
        self.Country_Comb.setItemText(57, QCoreApplication.translate("MainWindow", u"Eswatini (fmr. \"Swaziland\")", None))
        self.Country_Comb.setItemText(58, QCoreApplication.translate("MainWindow", u"Ethiopia", None))
        self.Country_Comb.setItemText(59, QCoreApplication.translate("MainWindow", u"Fiji", None))
        self.Country_Comb.setItemText(60, QCoreApplication.translate("MainWindow", u"Finland", None))
        self.Country_Comb.setItemText(61, QCoreApplication.translate("MainWindow", u"France", None))
        self.Country_Comb.setItemText(62, QCoreApplication.translate("MainWindow", u"Gabon", None))
        self.Country_Comb.setItemText(63, QCoreApplication.translate("MainWindow", u"Gambia", None))
        self.Country_Comb.setItemText(64, QCoreApplication.translate("MainWindow", u"Georgia", None))
        self.Country_Comb.setItemText(65, QCoreApplication.translate("MainWindow", u"Germany", None))
        self.Country_Comb.setItemText(66, QCoreApplication.translate("MainWindow", u"Ghana", None))
        self.Country_Comb.setItemText(67, QCoreApplication.translate("MainWindow", u"Greece", None))
        self.Country_Comb.setItemText(68, QCoreApplication.translate("MainWindow", u"Grenada", None))
        self.Country_Comb.setItemText(69, QCoreApplication.translate("MainWindow", u"Guatemala", None))
        self.Country_Comb.setItemText(70, QCoreApplication.translate("MainWindow", u"Guinea", None))
        self.Country_Comb.setItemText(71, QCoreApplication.translate("MainWindow", u"Guinea-Bissau", None))
        self.Country_Comb.setItemText(72, QCoreApplication.translate("MainWindow", u"Guyana", None))
        self.Country_Comb.setItemText(73, QCoreApplication.translate("MainWindow", u"Haiti", None))
        self.Country_Comb.setItemText(74, QCoreApplication.translate("MainWindow", u"Holy See", None))
        self.Country_Comb.setItemText(75, QCoreApplication.translate("MainWindow", u"Honduras", None))
        self.Country_Comb.setItemText(76, QCoreApplication.translate("MainWindow", u"Hungary", None))
        self.Country_Comb.setItemText(77, QCoreApplication.translate("MainWindow", u"Iceland", None))
        self.Country_Comb.setItemText(78, QCoreApplication.translate("MainWindow", u"India", None))
        self.Country_Comb.setItemText(79, QCoreApplication.translate("MainWindow", u"Indonesia", None))
        self.Country_Comb.setItemText(80, QCoreApplication.translate("MainWindow", u"Iran", None))
        self.Country_Comb.setItemText(81, QCoreApplication.translate("MainWindow", u"Iraq", None))
        self.Country_Comb.setItemText(82, QCoreApplication.translate("MainWindow", u"Ireland", None))
        self.Country_Comb.setItemText(83, QCoreApplication.translate("MainWindow", u"Israel", None))
        self.Country_Comb.setItemText(84, QCoreApplication.translate("MainWindow", u"Italy", None))
        self.Country_Comb.setItemText(85, QCoreApplication.translate("MainWindow", u"Jamaica", None))
        self.Country_Comb.setItemText(86, QCoreApplication.translate("MainWindow", u"Japan", None))
        self.Country_Comb.setItemText(87, QCoreApplication.translate("MainWindow", u"Jordan", None))
        self.Country_Comb.setItemText(88, QCoreApplication.translate("MainWindow", u"Kazakhstan", None))
        self.Country_Comb.setItemText(89, QCoreApplication.translate("MainWindow", u"Kenya", None))
        self.Country_Comb.setItemText(90, QCoreApplication.translate("MainWindow", u"Kiribati", None))
        self.Country_Comb.setItemText(91, QCoreApplication.translate("MainWindow", u"Kuwait", None))
        self.Country_Comb.setItemText(92, QCoreApplication.translate("MainWindow", u"Kyrgyzstan", None))
        self.Country_Comb.setItemText(93, QCoreApplication.translate("MainWindow", u"Laos", None))
        self.Country_Comb.setItemText(94, QCoreApplication.translate("MainWindow", u"Latvia", None))
        self.Country_Comb.setItemText(95, QCoreApplication.translate("MainWindow", u"Lebanon", None))
        self.Country_Comb.setItemText(96, QCoreApplication.translate("MainWindow", u"Lesotho", None))
        self.Country_Comb.setItemText(97, QCoreApplication.translate("MainWindow", u"Liberia", None))
        self.Country_Comb.setItemText(98, QCoreApplication.translate("MainWindow", u"Libya", None))
        self.Country_Comb.setItemText(99, QCoreApplication.translate("MainWindow", u"Liechtenstein", None))
        self.Country_Comb.setItemText(100, QCoreApplication.translate("MainWindow", u"Lithuania", None))
        self.Country_Comb.setItemText(101, QCoreApplication.translate("MainWindow", u"Luxembourg", None))
        self.Country_Comb.setItemText(102, QCoreApplication.translate("MainWindow", u"Madagascar", None))
        self.Country_Comb.setItemText(103, QCoreApplication.translate("MainWindow", u"Malawi", None))
        self.Country_Comb.setItemText(104, QCoreApplication.translate("MainWindow", u"Malaysia", None))
        self.Country_Comb.setItemText(105, QCoreApplication.translate("MainWindow", u"Maldives", None))
        self.Country_Comb.setItemText(106, QCoreApplication.translate("MainWindow", u"Mali", None))
        self.Country_Comb.setItemText(107, QCoreApplication.translate("MainWindow", u"Malta", None))
        self.Country_Comb.setItemText(108, QCoreApplication.translate("MainWindow", u"Marshall Islands", None))
        self.Country_Comb.setItemText(109, QCoreApplication.translate("MainWindow", u"Mauritania", None))
        self.Country_Comb.setItemText(110, QCoreApplication.translate("MainWindow", u"Mauritius", None))
        self.Country_Comb.setItemText(111, QCoreApplication.translate("MainWindow", u"Mexico", None))
        self.Country_Comb.setItemText(112, QCoreApplication.translate("MainWindow", u"Micronesia", None))
        self.Country_Comb.setItemText(113, QCoreApplication.translate("MainWindow", u"Moldova", None))
        self.Country_Comb.setItemText(114, QCoreApplication.translate("MainWindow", u"Monaco", None))
        self.Country_Comb.setItemText(115, QCoreApplication.translate("MainWindow", u"Mongolia", None))
        self.Country_Comb.setItemText(116, QCoreApplication.translate("MainWindow", u"Montenegro", None))
        self.Country_Comb.setItemText(117, QCoreApplication.translate("MainWindow", u"Morocco", None))
        self.Country_Comb.setItemText(118, QCoreApplication.translate("MainWindow", u"Mozambique", None))
        self.Country_Comb.setItemText(119, QCoreApplication.translate("MainWindow", u"Myanmar (formerly Burma)", None))
        self.Country_Comb.setItemText(120, QCoreApplication.translate("MainWindow", u"Namibia", None))
        self.Country_Comb.setItemText(121, QCoreApplication.translate("MainWindow", u"Nauru", None))
        self.Country_Comb.setItemText(122, QCoreApplication.translate("MainWindow", u"Nepal", None))
        self.Country_Comb.setItemText(123, QCoreApplication.translate("MainWindow", u"Netherlands", None))
        self.Country_Comb.setItemText(124, QCoreApplication.translate("MainWindow", u"New Zealand", None))
        self.Country_Comb.setItemText(125, QCoreApplication.translate("MainWindow", u"Nicaragua", None))
        self.Country_Comb.setItemText(126, QCoreApplication.translate("MainWindow", u"Niger", None))
        self.Country_Comb.setItemText(127, QCoreApplication.translate("MainWindow", u"Nigeria", None))
        self.Country_Comb.setItemText(128, QCoreApplication.translate("MainWindow", u"North Korea", None))
        self.Country_Comb.setItemText(129, QCoreApplication.translate("MainWindow", u"North Macedonia", None))
        self.Country_Comb.setItemText(130, QCoreApplication.translate("MainWindow", u"Norway", None))
        self.Country_Comb.setItemText(131, QCoreApplication.translate("MainWindow", u"Oman", None))
        self.Country_Comb.setItemText(132, QCoreApplication.translate("MainWindow", u"Pakistan", None))
        self.Country_Comb.setItemText(133, QCoreApplication.translate("MainWindow", u"Palau", None))
        self.Country_Comb.setItemText(134, QCoreApplication.translate("MainWindow", u"Palestine State", None))
        self.Country_Comb.setItemText(135, QCoreApplication.translate("MainWindow", u"Panama", None))
        self.Country_Comb.setItemText(136, QCoreApplication.translate("MainWindow", u"Papua New Guinea", None))
        self.Country_Comb.setItemText(137, QCoreApplication.translate("MainWindow", u"Paraguay", None))
        self.Country_Comb.setItemText(138, QCoreApplication.translate("MainWindow", u"Peru", None))
        self.Country_Comb.setItemText(139, QCoreApplication.translate("MainWindow", u"Philippines", None))
        self.Country_Comb.setItemText(140, QCoreApplication.translate("MainWindow", u"Poland", None))
        self.Country_Comb.setItemText(141, QCoreApplication.translate("MainWindow", u"Portugal", None))
        self.Country_Comb.setItemText(142, QCoreApplication.translate("MainWindow", u"Qatar", None))
        self.Country_Comb.setItemText(143, QCoreApplication.translate("MainWindow", u"Romania", None))
        self.Country_Comb.setItemText(144, QCoreApplication.translate("MainWindow", u"Russia", None))
        self.Country_Comb.setItemText(145, QCoreApplication.translate("MainWindow", u"Rwanda", None))
        self.Country_Comb.setItemText(146, QCoreApplication.translate("MainWindow", u"Saint Kitts and Nevis", None))
        self.Country_Comb.setItemText(147, QCoreApplication.translate("MainWindow", u"Saint Lucia", None))
        self.Country_Comb.setItemText(148, QCoreApplication.translate("MainWindow", u"Saint Vincent and the Grenadines", None))
        self.Country_Comb.setItemText(149, QCoreApplication.translate("MainWindow", u"Samoa", None))
        self.Country_Comb.setItemText(150, QCoreApplication.translate("MainWindow", u"San Marino", None))
        self.Country_Comb.setItemText(151, QCoreApplication.translate("MainWindow", u"Sao Tome and Principe", None))
        self.Country_Comb.setItemText(152, QCoreApplication.translate("MainWindow", u"Saudi Arabia", None))
        self.Country_Comb.setItemText(153, QCoreApplication.translate("MainWindow", u"Senegal", None))
        self.Country_Comb.setItemText(154, QCoreApplication.translate("MainWindow", u"Serbia", None))
        self.Country_Comb.setItemText(155, QCoreApplication.translate("MainWindow", u"Seychelles", None))
        self.Country_Comb.setItemText(156, QCoreApplication.translate("MainWindow", u"Sierra Leone", None))
        self.Country_Comb.setItemText(157, QCoreApplication.translate("MainWindow", u"Singapore", None))
        self.Country_Comb.setItemText(158, QCoreApplication.translate("MainWindow", u"Slovakia", None))
        self.Country_Comb.setItemText(159, QCoreApplication.translate("MainWindow", u"Slovenia", None))
        self.Country_Comb.setItemText(160, QCoreApplication.translate("MainWindow", u"Solomon Islands", None))
        self.Country_Comb.setItemText(161, QCoreApplication.translate("MainWindow", u"Somalia", None))
        self.Country_Comb.setItemText(162, QCoreApplication.translate("MainWindow", u"South Africa", None))
        self.Country_Comb.setItemText(163, QCoreApplication.translate("MainWindow", u"South Korea", None))
        self.Country_Comb.setItemText(164, QCoreApplication.translate("MainWindow", u"South Sudan", None))
        self.Country_Comb.setItemText(165, QCoreApplication.translate("MainWindow", u"Spain", None))
        self.Country_Comb.setItemText(166, QCoreApplication.translate("MainWindow", u"Sri Lanka", None))
        self.Country_Comb.setItemText(167, QCoreApplication.translate("MainWindow", u"Sudan", None))
        self.Country_Comb.setItemText(168, QCoreApplication.translate("MainWindow", u"Suriname", None))
        self.Country_Comb.setItemText(169, QCoreApplication.translate("MainWindow", u"Sweden", None))
        self.Country_Comb.setItemText(170, QCoreApplication.translate("MainWindow", u"Switzerland", None))
        self.Country_Comb.setItemText(171, QCoreApplication.translate("MainWindow", u"Syria", None))
        self.Country_Comb.setItemText(172, QCoreApplication.translate("MainWindow", u"Tajikistan", None))
        self.Country_Comb.setItemText(173, QCoreApplication.translate("MainWindow", u"Tanzania", None))
        self.Country_Comb.setItemText(174, QCoreApplication.translate("MainWindow", u"Thailand", None))
        self.Country_Comb.setItemText(175, QCoreApplication.translate("MainWindow", u"Timor-Leste", None))
        self.Country_Comb.setItemText(176, QCoreApplication.translate("MainWindow", u"Togo", None))
        self.Country_Comb.setItemText(177, QCoreApplication.translate("MainWindow", u"Tonga", None))
        self.Country_Comb.setItemText(178, QCoreApplication.translate("MainWindow", u"Trinidad and Tobago", None))
        self.Country_Comb.setItemText(179, QCoreApplication.translate("MainWindow", u"Tunisia", None))
        self.Country_Comb.setItemText(180, QCoreApplication.translate("MainWindow", u"Turkey", None))
        self.Country_Comb.setItemText(181, QCoreApplication.translate("MainWindow", u"Turkmenistan", None))
        self.Country_Comb.setItemText(182, QCoreApplication.translate("MainWindow", u"Tuvalu", None))
        self.Country_Comb.setItemText(183, QCoreApplication.translate("MainWindow", u"Uganda", None))
        self.Country_Comb.setItemText(184, QCoreApplication.translate("MainWindow", u"Ukraine", None))
        self.Country_Comb.setItemText(185, QCoreApplication.translate("MainWindow", u"United Arab Emirates", None))
        self.Country_Comb.setItemText(186, QCoreApplication.translate("MainWindow", u"United Kingdom", None))
        self.Country_Comb.setItemText(187, QCoreApplication.translate("MainWindow", u"United States of America", None))
        self.Country_Comb.setItemText(188, QCoreApplication.translate("MainWindow", u"Uruguay", None))
        self.Country_Comb.setItemText(189, QCoreApplication.translate("MainWindow", u"Uzbekistan", None))
        self.Country_Comb.setItemText(190, QCoreApplication.translate("MainWindow", u"Vanuatu", None))
        self.Country_Comb.setItemText(191, QCoreApplication.translate("MainWindow", u"Venezuela", None))
        self.Country_Comb.setItemText(192, QCoreApplication.translate("MainWindow", u"Vietnam", None))
        self.Country_Comb.setItemText(193, QCoreApplication.translate("MainWindow", u"Yemen", None))
        self.Country_Comb.setItemText(194, QCoreApplication.translate("MainWindow", u"Zambia", None))
        self.Country_Comb.setItemText(195, QCoreApplication.translate("MainWindow", u"Zimbabwe", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Select Country", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Reg_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Username ...", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Reg_confirm_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Your Password ...", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.Reg_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Password", None))
        self.back2Login_Button.setText(QCoreApplication.translate("MainWindow", u"I'm already register back to login !!", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u" Create a Free Account !", None))
#if QT_CONFIG(tooltip)
        self.Submit_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Laroussi ", None))
#endif // QT_CONFIG(tooltip)
        self.Submit_Btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.Forget_Reg_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Username ...", None))
        self.Forget_Reg_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXXX@Email.com", None))
        self.back2Login_Button_2.setText(QCoreApplication.translate("MainWindow", u"Back To Login !!", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.Confirm_Forget_New_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Your Password ...", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Confirm New Password", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Forget Password !?", None))
        self.Forget_New_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Password", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u" MediaTek Service :", None))
        self.read_info_radioButton.setText(QCoreApplication.translate("MainWindow", u"READ INFO", None))
        self.UL_radioButton.setText(QCoreApplication.translate("MainWindow", u"UNLOCK BOOTLOADER", None))
        self.RL_radioButton.setText(QCoreApplication.translate("MainWindow", u"RELOCK BOOTLOADER", None))
        self.factory_reset_radioButton.setText(QCoreApplication.translate("MainWindow", u"FACTORY RESET", None))
        self.FRP_radioButton.setText(QCoreApplication.translate("MainWindow", u"REMOVE FRP", None))
        self.auth_bypass_radioButton.setText(QCoreApplication.translate("MainWindow", u"AUTH BYPASS", None))
        self.lockbutton.setText(QCoreApplication.translate("MainWindow", u"Lock bootloader", None))
        self.unlockbutton.setText(QCoreApplication.translate("MainWindow", u"Unlock bootloader", None))
        self.Start_BTN.setText(QCoreApplication.translate("MainWindow", u" SART", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"UNIVERSAL", None))
        self.readselectallcheckbox.setText("")
        self.readDumpGPTCheckbox.setText(QCoreApplication.translate("MainWindow", u"Dump GPT", None))
        self.readpartitionsbtn.setText(QCoreApplication.translate("MainWindow", u" Save As", None))
        self.readtitle.setText(QCoreApplication.translate("MainWindow", u"Select partitions to read", None))
        ___qtablewidgetitem = self.readpartitionList.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Partition Name", None));
        ___qtablewidgetitem1 = self.readpartitionList.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Offset", None));
        ___qtablewidgetitem2 = self.readpartitionList.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem3 = self.readpartitionList.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem4 = self.readpartitionList.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        self.Checkpartitionsbtn.setText(QCoreApplication.translate("MainWindow", u"Check Partition(s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.readtab), QCoreApplication.translate("MainWindow", u"Read partition", None))
        self.writepartbtn.setText(QCoreApplication.translate("MainWindow", u" Write Partition(s)", None))
        self.writeselectfromdir.setText(QCoreApplication.translate("MainWindow", u" Select Partition", None))
        self.writetitle.setText(QCoreApplication.translate("MainWindow", u"Select partitions to write", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.writetab), QCoreApplication.translate("MainWindow", u"Write partition", None))
        self.erasepartitionsbtn.setText(QCoreApplication.translate("MainWindow", u" Erase Partition", None))
        self.eraseselectallpartitionscheckbox.setText(QCoreApplication.translate("MainWindow", u"Select all partitions", None))
        self.erasetitle.setText(QCoreApplication.translate("MainWindow", u"Select partitions to erase", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.erasetab), QCoreApplication.translate("MainWindow", u"Erase partition", None))
        self.Stop_BTN.setText(QCoreApplication.translate("MainWindow", u" STOP", None))
        self.logBox.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#dddddd;\">LAROUSSI UNIVERSAL TOOL V1.0</span><span style=\" font-size:12pt; color:#ffaa00;\"> BETA</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffaa00;\">FACEBOOK :</span><span style=\" font-size:10pt;\"> </span><a href=\"https://www.facebook.com/LaroussiGsm\"><span style=\" font-weight:400; text-decoration: underline; color:#0078d4;\">https://www.facebook.com/LaroussiGsm</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffaa00;\">MESSENGER :</span><span style=\" font-size:10pt;\"> </span><a href=\"m.me/103692875775674\"><span style=\" font-weight:400; text-decoration: underline; color:#0078d4;\">m.me/103692875775674</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffaa00;\">WEBSITE :</span><span style=\" font-size:10pt;\"> </span><a href=\"https://laroussigsm.net/\"><span style=\" font-weight:400; text-decoration: underline; color:#0078d4;\">https://laroussigsm.ne"
                        "t/</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffaa00;\">TELEGRAM :</span><span style=\" font-size:10pt;\"> </span><a href=\"https://t.me/UncleAnonymous\"><span style=\" font-weight:400; text-decoration: underline; color:#0078d4;\">https://t.me/UncleAnonymous</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400; text-decoration: underline; color:#0078d4;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#afafaf;\">MAIN CREDIT :</span><span style=\" font-weight:400; color:#afafaf;\"> LAROUSSIGSM.NET</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; "
                        "color:#afafaf;\">PACKED BY LAROUSSI GSM | UNCLE ANONYMOUS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#afafaf;\">LAROUSSI BOULANOUAR | OULED DJELLAL, ALGERIA<br /><br /></span></p></body></html>", None))
        self.Open_Devmgmt.setText(QCoreApplication.translate("MainWindow", u"DEVICE MANAGER", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Huawei Tab", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Qualcomm Tab", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Samsung Tab", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Android Tab", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"About Tab", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"FREE OPEN SOURCE PROJECT", None))
    # retranslateUi