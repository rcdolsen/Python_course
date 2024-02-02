from variables import SMALL_FONT

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget

# from typing import Optional # optional nao e mais usado


class History(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.config_style()

    def config_style(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight |
                          Qt.AlignmentFlag.AlignBottom)
