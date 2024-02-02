from PySide6.QtCore import QObject, QThread, QTime, Signal


# create a thread to check and ring the alarm
class WorkercheckerClass(QObject):
    def __init__(self, ui,  parent=None):
        super().__init__(parent)
        self.ui = ui


# create the signals
    started = Signal(str)
    alarm_time_reached = Signal(str)
    sound_stopped = Signal()
    finished = Signal(str)

# check the alarm and ring it if the current time is the same as the set
    def check_alarm(self):
        # Creates a loop to check the alarm every second
        self.ui.set_alarm_btn.setText('Reset alarm')
        finish = self.finished.emit

        while True:
            alarm_set = self.ui.lbl_alarm.text()
            alarm_btn = self.ui.set_alarm_btn.text()  # type:ignore

            self.current_time = QTime.currentTime()
            time_str = self.current_time.toString("hh:mm")
            QThread.msleep(1000)

            print(time_str)
            print(alarm_set)

            # rings the alarm if the current time is the same as the alarm
            if time_str == alarm_set:
                self.alarm_time_reached.emit("It's time")
            # if alarm_btn == 'Set alarm' and "Alarm not set" == alarm_set:
            #     print('acaba')
            #     self.sound_stopped.emit()
            #     finish('Alarm stopped')
            #     break

            if alarm_btn != 'Reset alarm' or alarm_set == 'Alarm off' or alarm_set == "It's time":

                if alarm_set == "It's time":
                    QThread.msleep(60000)
                    finish('Alarm not set')
                    break
                self.sound_stopped.emit()
                if alarm_set == 'Alarm off':
                    finish(alarm_set)
                else:
                    finish('Alarm not set')
                break
