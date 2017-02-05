import sys
from PyQt5.QtWidgets import (QWidget, QInputDialog, QApplication)

class InputNumberDialog(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()


    def init_ui(self):
        self.num, ok = QInputDialog.getInt(self, 'Окно ввода',
            'Введите количество задач:')
        if ok:
            print(self.num)

    def get_number(self):
        return self.num



