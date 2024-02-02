# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_alarm_clock.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(785, 317)
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout = QVBoxLayout(self.main_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_clock = QFrame(self.main_widget)
        self.frame_clock.setObjectName(u"frame_clock")
        self.frame_clock.setMaximumSize(QSize(16777215, 140))
        self.frame_clock.setFrameShape(QFrame.StyledPanel)
        self.frame_clock.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_clock)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(7, -1, -1, 9)
        self.lbl_clock = QLabel(self.frame_clock)
        self.lbl_clock.setObjectName(u"lbl_clock")
        self.lbl_clock.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_clock.sizePolicy().hasHeightForWidth())
        self.lbl_clock.setSizePolicy(sizePolicy)
        self.lbl_clock.setMinimumSize(QSize(749, 100))
        self.lbl_clock.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(50)
        self.lbl_clock.setFont(font)
        self.lbl_clock.setStyleSheet(u"	background-color: #ffffff; /* Cor de fundo branca */\n"
"    border-radius: 50px; \n"
"    border: 2px solid #2980b9; /* Estilo da borda, cor da borda, etc. */")
        self.lbl_clock.setFrameShape(QFrame.NoFrame)
        self.lbl_clock.setLineWidth(1)
        self.lbl_clock.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lbl_clock)


        self.verticalLayout.addWidget(self.frame_clock)

        self.Frame_sleep_alarm = QFrame(self.main_widget)
        self.Frame_sleep_alarm.setObjectName(u"Frame_sleep_alarm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Frame_sleep_alarm.sizePolicy().hasHeightForWidth())
        self.Frame_sleep_alarm.setSizePolicy(sizePolicy1)
        self.Frame_sleep_alarm.setMaximumSize(QSize(16777215, 100))
        self.Frame_sleep_alarm.setStyleSheet(u"QLabel {\n"
"	background-color: #ffffff; /* Cor de fundo branca */\n"
"    border-radius: 36px; \n"
"    border: 1px solid #2980b9; /* Estilo da borda, cor da borda, etc. */\n"
"}")
        self.Frame_sleep_alarm.setFrameShape(QFrame.StyledPanel)
        self.Frame_sleep_alarm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_sleep_alarm)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 9)
        self.lbl_alarm = QLabel(self.Frame_sleep_alarm)
        self.lbl_alarm.setObjectName(u"lbl_alarm")
        self.lbl_alarm.setMaximumSize(QSize(16777215, 72))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(False)
        self.lbl_alarm.setFont(font1)
        self.lbl_alarm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_alarm)

        self.lbl_sleep = QLabel(self.Frame_sleep_alarm)
        self.lbl_sleep.setObjectName(u"lbl_sleep")
        sizePolicy.setHeightForWidth(self.lbl_sleep.sizePolicy().hasHeightForWidth())
        self.lbl_sleep.setSizePolicy(sizePolicy)
        self.lbl_sleep.setMinimumSize(QSize(0, 72))
        self.lbl_sleep.setMaximumSize(QSize(16777215, 72))
        font2 = QFont()
        font2.setPointSize(25)
        self.lbl_sleep.setFont(font2)
        self.lbl_sleep.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_sleep)


        self.verticalLayout.addWidget(self.Frame_sleep_alarm)

        self.btn_widget = QWidget(self.main_widget)
        self.btn_widget.setObjectName(u"btn_widget")
        self.btn_widget.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.btn_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_btn_alarm = QFrame(self.btn_widget)
        self.frame_btn_alarm.setObjectName(u"frame_btn_alarm")
        self.frame_btn_alarm.setMaximumSize(QSize(16777215, 70))
        self.frame_btn_alarm.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_alarm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btn_alarm)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.alarm_on_off_btn = QToolButton(self.frame_btn_alarm)
        self.alarm_on_off_btn.setObjectName(u"alarm_on_off_btn")
        self.alarm_on_off_btn.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.alarm_on_off_btn)

        self.set_alarm_btn = QPushButton(self.frame_btn_alarm)
        self.set_alarm_btn.setObjectName(u"set_alarm_btn")
        self.set_alarm_btn.setMinimumSize(QSize(0, 35))
        self.set_alarm_btn.setAutoDefault(False)
        self.set_alarm_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.set_alarm_btn)


        self.horizontalLayout_2.addWidget(self.frame_btn_alarm)

        self.frame_btn_sleep = QFrame(self.btn_widget)
        self.frame_btn_sleep.setObjectName(u"frame_btn_sleep")
        self.frame_btn_sleep.setMaximumSize(QSize(16777215, 70))
        self.frame_btn_sleep.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_sleep.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_btn_sleep)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.set_sleep_btn = QPushButton(self.frame_btn_sleep)
        self.set_sleep_btn.setObjectName(u"set_sleep_btn")
        self.set_sleep_btn.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_4.addWidget(self.set_sleep_btn)

        self.sleep_on_off_btn = QToolButton(self.frame_btn_sleep)
        self.sleep_on_off_btn.setObjectName(u"sleep_on_off_btn")
        self.sleep_on_off_btn.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_4.addWidget(self.sleep_on_off_btn)


        self.horizontalLayout_2.addWidget(self.frame_btn_sleep)


        self.verticalLayout.addWidget(self.btn_widget)

        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)

        self.set_alarm_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_clock.setText("")
        self.lbl_alarm.setText(QCoreApplication.translate("MainWindow", u"Alarm not set", None))
        self.lbl_sleep.setText(QCoreApplication.translate("MainWindow", u"Sleep Time", None))
        self.alarm_on_off_btn.setText(QCoreApplication.translate("MainWindow", u"Turn alarm off", None))
        self.set_alarm_btn.setText(QCoreApplication.translate("MainWindow", u"set alarm", None))
        self.set_sleep_btn.setText(QCoreApplication.translate("MainWindow", u"set sleep", None))
        self.sleep_on_off_btn.setText(QCoreApplication.translate("MainWindow", u"Turn Sleep Off", None))
    # retranslateUi

