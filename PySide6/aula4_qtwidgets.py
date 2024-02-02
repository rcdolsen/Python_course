# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets

import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)

button = QPushButton('Texto do botao')
button.setStyleSheet('font-size: 40px; color:red')

button2 = QPushButton('botao 2')
button2.setStyleSheet('font-size: 20px; color:blue')

button3 = QPushButton('botaum 3')
button3.setStyleSheet('font-size: 30px; color:black')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 2, 1, 1, 2)

central_widget.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()  # Loop da aplicacao
