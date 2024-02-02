# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from buttons import Button  # Para resolver erro de circular import

from utils import is_num_or_dot, isempty
from variables import BIG_FONT, MINIMUM_WIDTH, TEXT_MARGIN

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit

# button: 'Button' # Para resolver erro de circular import


class Display(QLineEdit):
    eq_pressed = Signal()  # antes do init
    del_pressed = Signal()
    clear_pressed = Signal()
    input_Pressed = Signal(str)
    operator_pressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_display_style()

        # self.setReadOnly(True) # faz que nao seja possivel digitar no display
        # Os operadores ainda funcionam por causa do metodo keypressed

    def config_display_style(self):
        self.setStyleSheet(f'font-size: {BIG_FONT}px;')
        self.setMinimumHeight(BIG_FONT * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for i in range(4)])

    def keyPressEvent(self, event: QKeyEvent) -> None:
        # print(event.text())  # printa o que foi digitado
        # key_ = print(event.key()) # printa valores do sistema para cada tecla
        text = event.text().strip()
        key_ = event.key()
        KEYS = Qt.Key

        is_enter = key_ in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        is_delete = key_ in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_C]
        is_esc = key_ in [KEYS.Key_Escape]
        is_operator = key_ in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_X,
            KEYS.Key_Asterisk, KEYS.Key_P
        ]

        if is_enter:
            self.eq_pressed.emit()
            return event.ignore()  # nao vai fazer nada no display

        if is_delete:
            self.del_pressed.emit()
            return event.ignore()

        if is_esc:
            self.clear_pressed.emit()
            return event.ignore()

        if is_operator:
            if text.lower == 'p':
                text = '^'
            if text.lower == 'x':
                text = '*'
            self.operator_pressed.emit(text)
            # return event.ignore()

        # return super().keyPressEvent(event)  # se retirar esse return nenhuma
        # tecla do teclado funciona mais,
        # somente as configuradas no event.key()

        # Não passar daqui se não tiver texto
        if isempty(text):
            return event.ignore()

        if is_num_or_dot(text):
            self.input_Pressed.emit(text)
            return event.ignore()
