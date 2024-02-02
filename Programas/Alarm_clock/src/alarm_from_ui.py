# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_set_alarm.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_dialog_set_alarm(object):
    def setupUi(self, dialog_set_alarm):
        if not dialog_set_alarm.objectName():
            dialog_set_alarm.setObjectName(u"dialog_set_alarm")
        dialog_set_alarm.resize(344, 165)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_set_alarm.sizePolicy().hasHeightForWidth())
        dialog_set_alarm.setSizePolicy(sizePolicy)
        dialog_set_alarm.setMaximumSize(QSize(344, 400))
        dialog_set_alarm.setLayoutDirection(Qt.LeftToRight)
        dialog_set_alarm.setLocale(QLocale(QLocale.Portuguese, QLocale.Portugal))
        self.verticalLayout = QVBoxLayout(dialog_set_alarm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 5, 0)
        self.frame_set_time_alarm = QFrame(dialog_set_alarm)
        self.frame_set_time_alarm.setObjectName(u"frame_set_time_alarm")
        self.frame_set_time_alarm.setMaximumSize(QSize(16777215, 50))
        self.frame_set_time_alarm.setFrameShape(QFrame.StyledPanel)
        self.frame_set_time_alarm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_set_time_alarm)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.alarm_edit = QTimeEdit(self.frame_set_time_alarm)
        self.alarm_edit.setObjectName(u"alarm_edit")
        self.alarm_edit.setMaximumSize(QSize(70, 16777215))
        self.alarm_edit.setLayoutDirection(Qt.LeftToRight)
        self.alarm_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.alarm_edit)


        self.verticalLayout.addWidget(self.frame_set_time_alarm)

        self.dialog_btn_alarm = QFrame(dialog_set_alarm)
        self.dialog_btn_alarm.setObjectName(u"dialog_btn_alarm")
        self.dialog_btn_alarm.setMaximumSize(QSize(16777215, 50))
        self.dialog_btn_alarm.setFrameShape(QFrame.StyledPanel)
        self.dialog_btn_alarm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.dialog_btn_alarm)
        self.horizontalLayout.setSpacing(160)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cancel_alarm = QPushButton(self.dialog_btn_alarm)
        self.btn_cancel_alarm.setObjectName(u"btn_cancel_alarm")

        self.horizontalLayout.addWidget(self.btn_cancel_alarm)

        self.btn_ok_alarm = QPushButton(self.dialog_btn_alarm)
        self.btn_ok_alarm.setObjectName(u"btn_ok_alarm")

        self.horizontalLayout.addWidget(self.btn_ok_alarm)


        self.verticalLayout.addWidget(self.dialog_btn_alarm)


        self.retranslateUi(dialog_set_alarm)

        QMetaObject.connectSlotsByName(dialog_set_alarm)
    # setupUi

    def retranslateUi(self, dialog_set_alarm):
        dialog_set_alarm.setWindowTitle(QCoreApplication.translate("dialog_set_alarm", u"Dialog", None))
        self.btn_cancel_alarm.setText(QCoreApplication.translate("dialog_set_alarm", u"Cancel", None))
        self.btn_ok_alarm.setText(QCoreApplication.translate("dialog_set_alarm", u"OK", None))
    # retranslateUi

