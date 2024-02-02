# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_image_generator.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(666, 820)
        MainWindow.setStyleSheet(u"background-color: rgb(11, 11, 11);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.title_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.title_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"QFrame {\n"
"\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QLabel {\n"
"	\n"
"	background-color: rgb(179, 179, 179);\n"
"	border: 1.4px solid white;\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.main_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_btn = QPushButton(self.frame)
        self.left_btn.setObjectName(u"left_btn")
        font = QFont()
        font.setPointSize(10)
        self.left_btn.setFont(font)
        self.left_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.left_btn, 0, Qt.AlignLeft)

        self.right_btn = QPushButton(self.frame)
        self.right_btn.setObjectName(u"right_btn")
        self.right_btn.setFont(font)
        self.right_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.right_btn, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame)

        self.img_lbl = QLabel(self.main_frame)
        self.img_lbl.setObjectName(u"img_lbl")
        self.img_lbl.setMinimumSize(QSize(512, 512))

        self.verticalLayout_2.addWidget(self.img_lbl)


        self.verticalLayout.addWidget(self.main_frame)

        self.main_conteiner = QFrame(self.centralwidget)
        self.main_conteiner.setObjectName(u"main_conteiner")
        self.main_conteiner.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: solid 0px;\n"
"	font: 75 12px \"Segoe Print\";\n"
"	border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(56, 116, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.main_conteiner.setFrameShape(QFrame.StyledPanel)
        self.main_conteiner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_conteiner)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txt_description = QLineEdit(self.main_conteiner)
        self.txt_description.setObjectName(u"txt_description")
        self.txt_description.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(13)
        self.txt_description.setFont(font1)
        self.txt_description.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.txt_description)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_name_file = QLineEdit(self.main_conteiner)
        self.txt_name_file.setObjectName(u"txt_name_file")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setUnderline(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.txt_name_file.setFont(font2)
        self.txt_name_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_name_file)

        self.btn_generate = QPushButton(self.main_conteiner)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.btn_generate)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.main_conteiner)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Gerador de imagens IA</span></p></body></html>", None))
        self.left_btn.setText(QCoreApplication.translate("MainWindow", u"<--", None))
        self.right_btn.setText(QCoreApplication.translate("MainWindow", u"-->", None))
        self.img_lbl.setText("")
        self.txt_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Inform the text in english to generate the image", None))
        self.txt_name_file.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

