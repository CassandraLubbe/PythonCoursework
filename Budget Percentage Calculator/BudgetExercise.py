import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication
from budgetDemo import *

class BudgetForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonCalculate.clicked.connect(self.calculate_budget)
        self.show()

    def calculate_budget(self):
        amount_text = self.ui.lineEditAmount.text()
        amount = float(amount_text)

        need_amount = amount * 0.5
        want_amount = amount * 0.3
        saving_amount = amount * 0.2

        self.ui.labelNeedAmount.setText(str(need_amount))
        self.ui.labelWantAmount.setText(str(want_amount))
        self.ui.labelSavingAmount.setText(str(saving_amount))

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = BudgetForm()
    win.show()

    sys.exit(app.exec())