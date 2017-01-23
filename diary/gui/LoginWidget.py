# coding: utf-8

from PyQt5.QtWidgets import QWidget
from .ui.Ui_LoginWidget import Ui_Form

class LoginWidget(QWidget, Ui_Form):
    user_name = 'user'
    user_pass = '1234'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
