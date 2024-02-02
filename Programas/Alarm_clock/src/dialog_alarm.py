from alarm_from_ui import Ui_dialog_set_alarm

from PySide6.QtWidgets import QDialog


# define DialogAlarm class inheriting from QDialog
class DialogAlarm(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_dialog_set_alarm()
        self.ui.setupUi(self)
# connects the cancel button to close the dialog
# connects the ok button with the alarm_setter slot to set the alarm
        self.ui.btn_cancel_alarm.clicked.connect(self.close)
        self.ui.btn_ok_alarm.clicked.connect(self.alarm_setter)

# defines a method to pass the content set in the time edit of the alarm
# Dialog to the alarm label in the main Window
    def alarm_setter(self):
        alarm_edited = self.ui.alarm_edit.time()
        if hasattr(self.parent(), 'update_alarm_label'):
            self.parent().update_alarm_label(alarm_edited)  # type: ignore
        self.accept()
