# coding: utf-8

from PyQt5.QtWidgets import QMainWindow
from .ui.Ui_MainWindow import Ui_MainWindow
from .InputNumberDialog import InputNumberDialog
from .InputFileDialog import InputFileDialog
from .OptionListWidget import OptionList

class MainWindow(QMainWindow, Ui_MainWindow):
    file_names = []
    option_list = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_main()
        self.init_widgets()

    def init_main(self):
        self.setupUi(self)

    def init_widgets(self):
        self.init_task_number()
        self.init_file_names()
        self.init_options()


    def init_task_number(self):
        self.taskNumberWidget = InputNumberDialog(self)
        self.stackedWidget.addWidget(self.taskNumberWidget)
        self.stackedWidget.setCurrentWidget(self.taskNumberWidget)
        self.num = self.taskNumberWidget.get_number()
        print(self.num)

    def init_file_names(self):
        for i in range(0, self.num):
            self.inputFileName = InputFileDialog(self)
            self.stackedWidget.addWidget(self.inputFileName)
            self.stackedWidget.setCurrentWidget(self.inputFileName)
            file_name = self.inputFileName.get_name()
            self.stackedWidget.removeWidget(self.inputFileName)
            print(file_name)
            self.file_names.append(file_name)
        print(self.file_names)

    def init_options(self):
        self.optionList = OptionList()
        self.stackedWidget.addWidget(self.optionList)
        self.stackedWidget.setCurrentWidget(self.optionList)
