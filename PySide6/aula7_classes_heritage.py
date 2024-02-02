# Trabalhando com classes e herança no PySide6

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela feia')

        # Buttons
        self.button1 = self.make_button('Texto do botao')
        self.button1.clicked.connect(self.other_slot)

        self.button2 = self.make_button('botao 2')

        self.button3 = self.make_button('botaum 3')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.button1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.button3, 2, 1, 1, 2)

        # statusbar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('Primeiro menu')
        self.first_action = self.first_menu.addAction('Primeira acao')
        self.first_action.triggered.connect(self.slot_example)

        self.second_action = self.first_menu.addAction('Segunda acao')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.other_slot)
        self.second_action.hovered.connect(self.other_slot)

    @Slot()
    def slot_example(self):
        self.status_bar.showMessage('O slot foi executado')

    @Slot()
    def other_slot(self):
        if self.second_action.isChecked():
            print('segunda acao ativada')
        else:
            print('segunda acao desativada')

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 30px;')
        return btn


window = MyWindow()
window.show()
app.exec()  # Loop da aplicacao
