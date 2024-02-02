# O básico sobre Signal e Slots (eventos e documentação)

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela feia')

button1 = QPushButton('Texto do botao')
button1.setStyleSheet('font-size: 40px; color:red')

button2 = QPushButton('botao 2')
button2.setStyleSheet('font-size: 20px; color:blue')

button3 = QPushButton('botaum 3')
button3.setStyleSheet('font-size: 30px; color:black')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button1, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 2, 1, 1, 2)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O slot foi executado')
    return inner


@Slot()
def other_slot(checked):
    if checked:
        print('segunda acao ativada')
    else:
        print('segunda acao desativada')


@Slot()
def third_slot(action):
    def inner():
        other_slot(action.isChecked())
    return inner


# statusbar
status_bar = window.statusBar()
status_bar.showMessage('Mensagem na barra')

# menuBar
menu = window.menuBar()
first_menu = menu.addMenu('Primeiro menu')
first_action = first_menu.addAction('Primeira acao')
# first_action.triggered.connect(lambda: slot_example(status_bar))
first_action.triggered.connect(slot_example(status_bar))

second_action = first_menu.addAction('Segunda acao')
second_action.setCheckable(True)
second_action.toggled.connect(other_slot)
second_action.hovered.connect(third_slot(second_action))

button1.clicked.connect(third_slot(second_action))

window.show()
app.exec()  # Loop da aplicacao
