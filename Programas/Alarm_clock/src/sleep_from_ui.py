# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_set_sleep.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_dialog_set_sleep(object):
    def setupUi(self, dialog_set_sleep):
        if not dialog_set_sleep.objectName():
            dialog_set_sleep.setObjectName(u"dialog_set_sleep")
        dialog_set_sleep.resize(344, 165)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_set_sleep.sizePolicy().hasHeightForWidth())
        dialog_set_sleep.setSizePolicy(sizePolicy)
        dialog_set_sleep.setMaximumSize(QSize(344, 400))
        dialog_set_sleep.setLayoutDirection(Qt.LeftToRight)
        dialog_set_sleep.setLocale(QLocale(QLocale.Portuguese, QLocale.Portugal))
        self.verticalLayout = QVBoxLayout(dialog_set_sleep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 5, 0)
        self.frame_set_sleep = QFrame(dialog_set_sleep)
        self.frame_set_sleep.setObjectName(u"frame_set_sleep")
        self.frame_set_sleep.setMaximumSize(QSize(16777215, 50))
        self.frame_set_sleep.setFrameShape(QFrame.StyledPanel)
        self.frame_set_sleep.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_set_sleep)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sleep_edit = QSpinBox(self.frame_set_sleep)
        self.sleep_edit.setObjectName(u"sleep_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sleep_edit.sizePolicy().hasHeightForWidth())
        self.sleep_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.sleep_edit)


        self.verticalLayout.addWidget(self.frame_set_sleep)

        self.dialog_btn_sleep = QFrame(dialog_set_sleep)
        self.dialog_btn_sleep.setObjectName(u"dialog_btn_sleep")
        self.dialog_btn_sleep.setMaximumSize(QSize(16777215, 50))
        self.dialog_btn_sleep.setFrameShape(QFrame.StyledPanel)
        self.dialog_btn_sleep.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.dialog_btn_sleep)
        self.horizontalLayout.setSpacing(160)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cancel_sleep = QPushButton(self.dialog_btn_sleep)
        self.btn_cancel_sleep.setObjectName(u"btn_cancel_sleep")

        self.horizontalLayout.addWidget(self.btn_cancel_sleep)

        self.btn_ok_sleep = QPushButton(self.dialog_btn_sleep)
        self.btn_ok_sleep.setObjectName(u"btn_ok_sleep")

        self.horizontalLayout.addWidget(self.btn_ok_sleep)


        self.verticalLayout.addWidget(self.dialog_btn_sleep)


        self.retranslateUi(dialog_set_sleep)

        QMetaObject.connectSlotsByName(dialog_set_sleep)
    # setupUi

    def retranslateUi(self, dialog_set_sleep):
        dialog_set_sleep.setWindowTitle(QCoreApplication.translate("dialog_set_sleep", u"Dialog", None))
        self.btn_cancel_sleep.setText(QCoreApplication.translate("dialog_set_sleep", u"Cancel", None))
        self.btn_ok_sleep.setText(QCoreApplication.translate("dialog_set_sleep", u"OK", None))
    # retranslateUi

