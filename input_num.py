# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import(
    QApplication, QWidget, QMainWindow,
    QLabel, QSpinBox, QPushButton,
    QVBoxLayout
    )

class InputNumber(QMainWindow):
    def __init__(self, *args, **kwargs):
        self.num = 1
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initLayout()

    def initUi(self):
        self.setWindowTitle('ГД анализ компрессоров')
        self.numLabel = QLabel('Количество задач:', self)
        self.numInput = QSpinBox(self)
        self.numInput.setMinimum(1)
        self.okBtn = QPushButton('OK', self)
        self.okBtn.clicked.connect(self.getNumber)

    def getNumber(self):
        self.num = self.numInput.value()
        self.close()
        
        
    def initLayout(self):
        self.w = QWidget()
        self.mainLayout = QVBoxLayout(self.w)
        self.mainLayout.addWidget(self.numLabel)
        self.mainLayout.addWidget(self.numInput)
        self.mainLayout.addWidget(self.okBtn)
        self.setCentralWidget(self.w)
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    input_num = InputNumber()
    input_num.show()
    task_num = input_num.num
    print(input_num.num)
    sys.exit(app.exec_())
    

