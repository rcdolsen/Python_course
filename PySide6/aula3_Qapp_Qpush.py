# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

button = QPushButton('Texto do botao')
button.setStyleSheet('font-size: 40px; color:red')
button.show()  # Adicionar widget na hierarquia e exibe a janela

# button2 = QPushButton('Texto do botao')
# button2.show()

app.exec()  # Loop da aplicacao
