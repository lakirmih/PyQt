# 1. Двусторонняя конвертация - 1
# 2. Блокировка перевода при неккоректных значениях - 1
# 3. Кнопка очистки - 0.5
# 4.* Конвертация по нажатию Enter

import sys

from PyQt5.QtCore import QObject

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QDoubleSpinBox,
    QVBoxLayout
    )

class Course(QObject):
    def get(self):
        return 65

class Converter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initSignals()
        self.initLayouts()
        self.initActive()

    def initUi(self):
        self.setWindowTitle('Конвертер валют')
        self.ruLabel = QLabel('Сумма в рублях', self)
        self.dLabel = QLabel('Сумма в долларах', self)

        self.ruAmount = QDoubleSpinBox(self)
        self.ruAmount.setMaximum(999999999)
        self.dAmount = QDoubleSpinBox(self)
        self.dAmount.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевод', self)
        self.clearBtn = QPushButton('Очистить', self)

        self.ruAmount.valueChanged.connect(self.initActive)
        self.dAmount.valueChanged.connect(self.initActive)
        
    def initActive(self):
        if ((self.ruAmount.value() == 0 and self.dAmount.value() == 0) or
            (self.ruAmount.value() != 0 and self.dAmount.value() != 0)):
            self.convertBtn.setDisabled(True)
        else:
            self.convertBtn.setDisabled(False)

    def initSignals(self):
        self.convertBtn.clicked.connect(self.onClick)
        self.clearBtn.clicked.connect(self.onClear)

    def initLayouts(self):
        self.w = QWidget()

        self.mainLayout = QVBoxLayout(self.w)

        self.mainLayout.addWidget(self.ruLabel)
        self.mainLayout.addWidget(self.ruAmount)
        self.mainLayout.addWidget(self.dLabel)
        self.mainLayout.addWidget(self.dAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.clearBtn)
        

        self.setCentralWidget(self.w)

    def onClick(self):
        ruValue = self.ruAmount.value()
        dValue = self.dAmount.value()
        if ruValue != 0 and dValue == 0:
            self.dAmount.setValue(ruValue / Course().get())
        elif ruValue == 0 and dValue != 0:
            self.ruAmount.setValue(dValue * Course().get())
            
    def onClear(self):
        self.ruAmount.setValue(0.0)
        self.dAmount.setValue(0.0)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = Converter()
    converter.show()

    sys.exit(app.exec_())


