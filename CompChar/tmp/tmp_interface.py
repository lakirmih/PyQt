import sys
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import (
QApplication, QMainWindow, QWidget,
QLabel, QPushButton, QSpinBox
)

class Course(QObject):
    def get(self):
        return 65

class Converter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initUi(self):
        self.setWindowTitle('Converter')
        self.
