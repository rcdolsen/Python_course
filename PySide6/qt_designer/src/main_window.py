import sys
from typing import cast

from window import Ui_MainWindow

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.ButtonSend.clicked.connect(self.changeLabelResult)

        self.lineEdit.installEventFilter(self)

    def changeLabelResult(self):
        text = self.lineEdit.text()
        self.bigLabel.setText(text)
        self.lineEdit.clear()

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:

        if event.type() == QEvent.Type.KeyPress:
            # Tenho certeza que o type e Keypress
            event = cast(QKeyEvent, event)
            text = self.lineEdit.text()
            self.bigLabel.setText(text + event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec()
