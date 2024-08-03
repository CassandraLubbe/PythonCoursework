import sys
import math
from PyQt6.QtWidgets import QDialog, QApplication
from design import *

class Calculator(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.spinBoxWordCount.setRange(0, 100000)

        self.selected_days = 0
        self.total_days = 0
        self.total_words = 0
        self.ui.pushButtonCalculate.clicked.connect(self.calc_days)

    def work_days(self):
        count = 0

        if self.ui.checkBoxMonday.isChecked():
            count += 1
        if self.ui.checkBoxTuesday.isChecked():
            count += 1
        if self.ui.checkBoxWednesday.isChecked():
            count += 1
        if self.ui.checkBoxThursday.isChecked():
            count += 1
        if self.ui.checkBoxFriday.isChecked():
            count += 1
        if self.ui.checkBoxSaturday.isChecked():
            count += 1
        if self.ui.checkBoxSunday.isChecked():
            count += 1

        print("Count is:" + str(count))

        self.selected_days = count


    def calc_days(self):
        self.work_days()

        word_count = self.ui.spinBoxWordCount.value()
        standard_days = word_count // 1500

        week_count = standard_days // self.selected_days
        rounded_week = math.ceil(week_count)
        self.total_days = rounded_week * 7 + (self.ui.spinBoxHoliday.value())

        self.total_words = word_count // self.total_days

        self.result()

    def result(self):
        self.ui.labelResult.setText(f"Total days to write {self.ui.spinBoxWordCount.value()}: {self.total_days} days." "\n"
                                    f"Average words per day: {self.total_words}")


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.setWindowTitle("Total Days Calculator")
    window.show()

    sys.exit(app.exec())