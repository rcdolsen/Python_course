from sleep_from_ui import Ui_dialog_set_sleep

from PySide6.QtWidgets import QDialog


class DialogSleep(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_dialog_set_sleep()
        self.ui.setupUi(self)

        self.ui.btn_cancel_sleep.clicked.connect(self.close)
        self.ui.btn_ok_sleep.clicked.connect(self.sleep_setter)

    def sleep_setter(self):
        sleep_setted = self.ui.sleep_edit.value()
        if hasattr(self.parent(), 'update_sleep_lbl'):
            self.parent().update_sleep_lbl(sleep_setted)  # type: ignore
        self.accept()
