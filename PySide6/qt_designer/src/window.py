# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(774, 526)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.bigLabel = QLabel(self.centralwidget)
        self.bigLabel.setObjectName(u"bigLabel")
        font = QFont()
        font.setFamilies([u"Roman"])
        font.setUnderline(True)
        self.bigLabel.setFont(font)
        self.bigLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.bigLabel, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setPointSize(15)
        self.lineEdit.setFont(font1)

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Roboto Slab SemiBold"])
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.label.setFont(font2)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.ButtonSend = QPushButton(self.centralwidget)
        self.ButtonSend.setObjectName(u"ButtonSend")
        self.ButtonSend.setFont(font1)

        self.gridLayout_2.addWidget(self.ButtonSend, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 774, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bigLabel.setText(QCoreApplication.translate("MainWindow", u"TEIXTU", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.ButtonSend.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

