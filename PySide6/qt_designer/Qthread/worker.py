# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worker.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(775, 552)
        font = QFont()
        font.setPointSize(25)
        Form.setFont(font)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.l1 = QLabel(Form)
        self.l1.setObjectName(u"l1")

        self.gridLayout.addWidget(self.l1, 0, 0, 1, 1)

        self.l2 = QLabel(Form)
        self.l2.setObjectName(u"l2")

        self.gridLayout.addWidget(self.l2, 0, 1, 1, 1)

        self.b1 = QPushButton(Form)
        self.b1.setObjectName(u"b1")

        self.gridLayout.addWidget(self.b1, 1, 0, 1, 1)

        self.b2 = QPushButton(Form)
        self.b2.setObjectName(u"b2")

        self.gridLayout.addWidget(self.b2, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.l1.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.l2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.b1.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.b2.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

