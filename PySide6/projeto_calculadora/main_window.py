
from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWiget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # configura o layout
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # titulo da janela
        self.setWindowTitle('Calculator')

    def adjust_fixed_size(self):
        # ultimo a ser feito
        self.adjustSize()  # ajusta o texto a janela
        self.setFixedSize(self.width(), self.height())
        # self.v_layout.setSpacing(0)

    def addWidgetToLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
        # self.adjust_fixed_size()

    def make_msg_box(self):
        return QMessageBox(self)
