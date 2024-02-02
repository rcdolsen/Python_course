import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel

from buttons import ButtonsGrid
from display import Display
from history import History
from main_window import MainWindow
from styles import setup_theme
from variables import BIG_FONT, MEDIUM_FONT, WINDOW_ICON_PATH


def temp_label(text):
    label = QLabel(text)
    label.setStyleSheet(f'font-size: {MEDIUM_FONT}px;')
    return label


def temp_display(text):
    display = Display(text)
    display.setStyleSheet(f'font-size: {BIG_FONT}px;')
    return display


# def make_buttons(text, row, col, row_spam, col_spam):
#     buttons_grid.addWidget(Button(text), row, col, row_spam, col_spam)


if __name__ == '__main__':
    # cria a aplicacao
    app = QApplication(sys.argv)
    window = MainWindow()
    setup_theme()

    # label temporario para teste
    # window.addWidgetToLayout(temp_label('Text0'))
    # window.addWidgetToLayout(temp_label('Text1'))

    # display temnporario para teste
    # window.addWidgetToLayout(temp_display('Text0'))
    # window.addWidgetToLayout(temp_display('Text1'))

    # configura placeholder

    # define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    # definir em window e app para funcionar em windows e mac
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # history
    history = History('operation')
    window.addWidgetToLayout(history)

    # display
    display = Display()
    display.setPlaceholderText('Calculator Project')
    window.addWidgetToLayout(display)

    # Grid
    buttons_grid = ButtonsGrid(display, history, window)
    window.v_layout.addLayout(buttons_grid)

    # buttons

    # make_buttons('7', 0, 0, 1, 1)
    # make_buttons('8', 0, 1, 1, 1)
    # make_buttons('9', 0, 2, 1, 1)
    # make_buttons('÷', 0, 3, 1, 1)

    # make_buttons('4', 1, 0, 1, 1)
    # make_buttons('5', 1, 1, 1, 1)
    # make_buttons('6', 1, 2, 1, 1)
    # make_buttons('x', 1, 3, 1, 1)

    # make_buttons('1', 2, 0, 1, 1)
    # make_buttons('2', 2, 1, 1, 1)
    # make_buttons('3', 2, 2, 1, 1)
    # make_buttons('-', 2, 3, 1, 1)

    # make_buttons('0', 3, 1, 1, 1)
    # make_buttons(',', 3, 0, 1, 1)
    # make_buttons('=', 3, 2, 1, 1)
    # make_buttons('+', 3, 3, 1, 1)

    # button2 = Button('8')
    # buttons_grid.addWidget(button2, 0, 1)

    # button2 = Button('9')
    # buttons_grid.addWidget(button2, 0, 2)

    # button2 = Button('4')
    # buttons_grid.addWidget(button2, 1, 0)

    # button2 = Button('5')
    # buttons_grid.addWidget(button2, 1, 1)

    # button2 = Button('6')
    # buttons_grid.addWidget(button2, 2, 1)

    # button2 = Button('1')
    # buttons_grid.addWidget(button2, 2, 1)

    # button2 = Button('2')
    # buttons_grid.addWidget(button2, 2, 1)

    # button2 = Button('3')
    # buttons_grid.addWidget(button2, 2, 1)

    # executa tudo
    window.adjust_fixed_size()
    window.show()
    app.exec()
