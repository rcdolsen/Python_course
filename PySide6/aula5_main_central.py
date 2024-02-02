# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec


import sys

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


def slot_example(status_bar):
    status_bar.showMessage('Voce clicou aqui')


# statusbar
status_bar = window.statusBar()
status_bar.showMessage('Mensagem na barra')

# menuBar
menu = window.menuBar()
first_menu = menu.addMenu('Primeiro menu')
first_action = first_menu.addAction('Primeira acao')
first_action.triggered.connect(lambda: slot_example(status_bar))


window.show()
app.exec()  # Loop da aplicacao
