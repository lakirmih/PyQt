# coding: utf-8

from PyQt5.QtWidgets import QMainWindow

from .ui.Ui_MainWindow import Ui_MainWindow

from .NotesWidget import NotesWidget
from .LoginWidget import LoginWidget

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # для python3: super().__init__(*args, **kwargs)
        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.setupUi(self)

        self.loginWidget = LoginWidget(self)
        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.setCurrentWidget(self.loginWidget)
        self.notesWidget = NotesWidget(self)
        self.stackedWidget.addWidget(self.notesWidget)
        #self.stackedWidget.setCurrentWidget(self.notesWidget) ####
        # loginWidget - при открытии, логин и пароль строго из приложения

    def init_signals(self):
        self.loginWidget.okBtn.clicked.connect(self.checkLogin)

    def checkLogin(self):
        if (self.loginWidget.loginEdit.text() == self.loginWidget.user_name and
            self.loginWidget.passwordEdit.text() == self.loginWidget.user_pass):
            
            self.stackedWidget.setCurrentWidget(self.notesWidget)
        else:
            self.loginWidget.passwordEdit.clear()
            self.loginWidget.loginEdit.clear()

    
