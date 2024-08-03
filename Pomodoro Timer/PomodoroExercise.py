import sys
from PyQt6.QtWidgets import QDialog, QApplication, QLCDNumber
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import QTimer, QTime, Qt
from pomodoroDemo import *
class PomoTimer(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer_working = True  # Initialize timer_working
        self.setup_LCD()

        font = self.ui.labelName.font()
        font.setPointSize(20)
        self.ui.labelName.setFont(font)
        self.ui.labelName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.labelName.setText("Let's Get Started!")

        self.ui.pushButtonStart.setStyleSheet("background-color: green")
        self.ui.pushButtonReset.setStyleSheet("background-color: red")

    def setup_LCD(self):
        self.work_time = 25 * 60 * 1000
        self.break_time = 5 * 60 * 1000
        self.current_time = self.work_time

        self.ui.lcdNumber.setDigitCount(5)
        self.ui.lcdNumber.display(self.format_time(self.current_time))

        self.ui.pushButtonStart.clicked.connect(self.start_timer)
        self.ui.pushButtonReset.clicked.connect(self.reset_timer)

    def start_timer(self):
        self.ui.labelName.setText("Time to Work!")
        if not self.timer.isActive():
            self.timer.timeout.connect(self.update_timer)
            self.timer.start(1000)

    def reset_timer(self):
        self.timer.stop()
        self.timer.timeout.disconnect(self.update_timer)
        self.ui.lcdNumber.display(self.format_time())  # Removed milliseconds argument
        self.current_time = self.work_time
        self.timer_working = True  # Reset timer_working

    def update_timer(self):
        self.current_time -= 1000

        if self.current_time <= 0:
            self.timer.stop()
            self.ui.lcdNumber.display("00:00")
            if self.timer_working:
                self.ui.labelName.setText("Break Time!")
                self.current_time = self.break_time
            else:
                self.ui.labelName.setText("Work Time!")
                self.current_time = self.work_time
            self.timer_working = not self.timer_working
        else:
            minutes = self.current_time // 60000
            seconds = (self.current_time % 60000) // 1000
            time_display = "{:02}:{:02}".format(minutes, seconds)
            self.ui.lcdNumber.display(time_display)

    def format_time(self, milliseconds=None):  # Added default argument
        if milliseconds is None:  # Check if milliseconds argument is provided
            milliseconds = self.work_time  # Use work_time if no argument provided
        minutes = milliseconds // 60000
        seconds = (milliseconds % 60000) // 1000
        return "{:02}:{:02}".format(minutes, seconds)


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = PomoTimer()
    window.show()

    sys.exit(app.exec())