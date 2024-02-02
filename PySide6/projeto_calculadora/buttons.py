import math
from typing import TYPE_CHECKING

from utils import convert_to_int, is_num_or_dot, is_valid_number, isempty
from variables import MEDIUM_FONT

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton

if TYPE_CHECKING:
    from display import Display  # Para resolver erro de circular import
    from history import History
    from main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT)
        # font.setItalic(True)
        # font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(40, 20)
        # self.setCheckable(True)


class ButtonsGrid(QGridLayout):
    def __init__(
            self, display: 'Display', history: 'History', window: 'MainWindow',
            *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '÷'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['neg', '.',  '0', '='],
        ]
        self.display = display
        self.history = history
        self.window = window
        self._equation = ''
        self._equation_initial_value = 'operation'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equation_initial_value
        self._make_grid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.history.setText(value)

    def _make_grid(self):
        self.display.eq_pressed.connect(self._eq)
        self.display.del_pressed.connect(self._backspace)
        self.display.clear_pressed.connect(self._clear)
        self.display.input_Pressed.connect(self._insert_to_display)
        self.display.operator_pressed.connect(self._config_left_op)

        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                # if button_text not in '0123456789.':
                if not is_num_or_dot(button_text) and not isempty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._config_special_button(button)

                self.addWidget(button, i, j)

                slot = self._make_slot(self._insert_to_display, button_text)
                self._connect_button_clicked(button, slot)

    def _connect_button_clicked(self, button, slot):
        button.clicked.connect(slot)

    def _config_special_button(self, button):
        text = button.text()

        if text == 'C':
            self._connect_button_clicked(button, self._clear)
            # button.clicked.connect(self.display.clear)

        if text in '+-÷x^':

            self._connect_button_clicked(
                button,
                self._make_slot(self._config_left_op, text)
            )

        if text == '=':
            self._connect_button_clicked(button, self._eq)

        if text == 'neg':
            self._connect_button_clicked(button, self._invert_number)

        if text == '◀':
            self._connect_button_clicked(button, self.display.backspace)

    @Slot()
    def _make_slot(self, func, *args, **kwargs):
        @ Slot(bool)
        def real_slot():
            func(*args, **kwargs)
        return real_slot

    @Slot()
    def _invert_number(self):
        display_text = self.display.text()

        if not is_valid_number(display_text):
            return

        number = -convert_to_int(display_text)

        self.display.setText(str(number))

    @Slot()
    def _insert_to_display(self, text):
        new_display_value = self.display.text() + text

        if not is_valid_number(new_display_value):
            return

        self.display.insert(text)
        self.display.setFocus()

        # print(123, button.text())

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equation_initial_value
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _config_left_op(self, text):
        display_text = self.display.text()  # Devera ser meu numero _left
        self.display.clear()  # limpa o display

        # se a pessoa clicou no operador sem configurar um numero antes
        if not is_valid_number(display_text) and self._left is None:
            self._show_error('primeiro digite um numero')
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = convert_to_int(display_text)
        # print(button_text)

        self._op = text
        self.equation = f'{self._left} {self._op} ???'
        self.display.setFocus()

    @Slot()
    def _eq(self):
        display_text = self.display.text()

        if not is_valid_number(display_text) or self._left is None:
            self._show_info('operacao invalida')
            return

        self._right = convert_to_int(display_text)

        if self._op == 'x':
            self._op = '*'
        if self._op == '÷':
            self._op = '/'

        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'ERROR'

        try:
            if '^' in self.equation and isinstance(self._left, int | float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._show_error('divisao por zero nao e aceita')
        except OverflowError:
            self._show_error('o numero e muito grande')

        self.display.clear()
        self.history.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == 'ERROR':
            self._left = None

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _make_dialog(self, text):
        msgbox = self.window.make_msg_box()
        msgbox.setText(text)
        return msgbox

    def _show_error(self, text):
        msgbox = self._make_dialog(text)
        # msgbox.setInformativeText(
        #     '''Texto informativo, este texto e muito grande''')
        msgbox.setIcon(msgbox.Icon.Critical)
        msgbox.exec()
        self.display.setFocus()

    def _show_info(self, text):
        msgbox = self._make_dialog(text)
        msgbox.setIcon(msgbox.Icon.Information)
        msgbox.exec()
        self.display.setFocus()

        # msgbox.setStandardButtons(msgbox.StandardButton.Cancel)

        # # Personalisar o texto do botao
        # msgbox.button(msgbox.StandardButton.Cancel).setText('Cancelar')

        # msgbox.setStandardButtons(
        #     msgbox.StandardButton.Ok |
        #     msgbox.StandardButton.Abort |
        #     msgbox.StandardButton.Cancel
        # )

        # result = msgbox.exec()

        # if result == msgbox.StandardButton.Ok:
        #     print('clicou em ok')
        # if result == msgbox.StandardButton.Abort:
        #     print('clicou em abort')
        # if result == msgbox.StandardButton.Cancel:
        #     print('clicou em cancel')
