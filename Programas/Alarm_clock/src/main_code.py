import os
import platform
import sys
from pathlib import Path

from dialog_alarm import DialogAlarm
from dialog_sleep import DialogSleep
from main_from_ui import Ui_MainWindow
from worker import WorkercheckerClass

from PySide6.QtCore import QThread, QTime, QTimer, QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QApplication, QMainWindow

PROGRAM_PATH = Path(__file__).parent.parent
SOUND_PATH = PROGRAM_PATH/"misc"


# defines the main class
class PyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.alarm_set = self.ui.lbl_alarm.text
        self.alarm_time_set = False

# ensures that the show_dialog slot is called only when the button
# is clicked
        self.ui.set_alarm_btn.clicked.connect(
            lambda: self.show_dialog(DialogAlarm(self)))
        self.ui.set_sleep_btn.clicked.connect(
            lambda: self.show_dialog(DialogSleep(self)))

# sets the timer and calls the update_clock_lbl slot every second
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.update_clock_lbl)
        self._timer.start(1000)

# sets the sound and volume to play when the alarm rings
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile(
            SOUND_PATH/"mixkit-retro-game-emergency-alarm-1000.wav"))
        self.sound_effect.setVolume(3)

        self.ui.alarm_on_off_btn.setCheckable(True)
        self.ui.alarm_on_off_btn.toggled.connect(self.alarm_on_off_toggle)

# defines the slot to show the dialogs when the button is clicked
    def show_dialog(self, dialog):
        if self.ui.set_alarm_btn.text() == 'Reset alarm':
            self.ui.set_alarm_btn.setText('Set alarm')
            self.ui.lbl_alarm.setText('Alarm not set')
            self.alarm_time_set = False
        else:
            dialog_window = dialog
            dialog_window.exec()

# defines the slot to update the clock in the UI with the current time
    def update_clock_lbl(self):
        self.current_time = QTime.currentTime()
        time_str = self.current_time.toString("hh:mm:ss")
        self.ui.lbl_clock.setText(time_str)

# updates the alarm label with the time set in the alarm dialog
    def update_alarm_label(self, alarm_edited):

        # if self.alarm_time_set:
        #     self.ui.set_alarm_btn.setText('Set alarm')
        #     self.ui.lbl_alarm.setText('Alarm not set')
        #     self.alarm_time_set = False
        #     return
        # else:
        self.alarm_set_to_str = alarm_edited.toString("hh:mm")
        self.ui.lbl_alarm.setText(self.alarm_set_to_str)
        self.worker_method()
        self.alarm_time_set = True

    def alarm_on_off_toggle(self, checked):
        if checked:
            self.ui.alarm_on_off_btn.setText('Turn alarm on')
            self.alarm_set = self.ui.lbl_alarm.text()
            self.ui.lbl_alarm.setText('Alarm off')
            self.ui.set_alarm_btn.setDisabled(True)
        else:
            self.ui.alarm_on_off_btn.setText('Turn alarm off')
            self.ui.set_alarm_btn.setDisabled(False)

            self.ui.lbl_alarm.setText(self.alarm_set)  # type: ignore
            if self.alarm_set != 'Alarm not set':
                self.worker_method()

    def update_sleep_lbl(self, sleep_setted):
        sleep_countdown = self.ui.lbl_sleep.setNum

        # while sleep_setted != 0:
        #     sleep_countdown(sleep_setted)
        #     sleep_setted -= 1
        #     QThread.msleep(1000)

        # Check the operating system
        # if platform.system() == 'Windows':
        #     os.system('shutdown /s /t')  # windows shutdown command
        # elif platform.system() == 'Linux':
        #     os.system('sudo shutdown now')  # Linux shutdown command
        # elif platform.system() == 'Darwin':
        #     os.system('sudo shutdown now')  # macOS shutdown command
        # else:
        #     print("sleep mode not implemented for this operating system")

# connects with the thread to check and ring the alarm

    def worker_method(self):
        self._worker_alarm_checker = WorkercheckerClass(self.ui)
        self._thread_alarm_checker = QThread()
        worker_alarm_checker = self._worker_alarm_checker
        thread_alarm_checker = self._thread_alarm_checker

# moves the task to the thread and starts it
        worker_alarm_checker.moveToThread(thread_alarm_checker)

        thread_alarm_checker.started.connect(
            worker_alarm_checker.check_alarm)

# quits and clean the system when the thread is finished
        worker_alarm_checker.finished.connect(thread_alarm_checker.quit)
        thread_alarm_checker.finished.connect(thread_alarm_checker.deleteLater)
        worker_alarm_checker.finished.connect(thread_alarm_checker.deleteLater)

# connects to the signals in the thread
        worker_alarm_checker.alarm_time_reached.connect(self.ring_alarm)
        worker_alarm_checker.sound_stopped.connect(self.stop_sound)
        worker_alarm_checker.finished.connect(self.alarm_finish)

# starts the thread
        thread_alarm_checker.start()

# plays the sound to ring the alarm
    def ring_alarm(self, msg):
        self.sound_effect.play()
        self.ui.lbl_alarm.setText(msg)

    def stop_sound(self):
        self.sound_effect.stop()

    def alarm_finish(self, msg):
        self.ui.lbl_alarm.setText(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PyMainWindow()
    window.show()
    app.exec()
