from PyQt5.QtWidgets import QWidget
from .ui.Ui_OptionList import Ui_optionList

class OptionList(QWidget, Ui_optionList):
    option_list = [int for i in range(0,5)]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.okBtn.clicked.connect(self.get_option_list)

    def get_option_list(self):
        self.option_list[0] = (self.GlobalOption.checkState())
        self.option_list[1] = (self.ControlSurfacesOption.checkState())
        self.option_list[2] = (self.RowEffOption.checkState())
        self.option_list[3] = (self.StageEffOption.checkState())
        self.option_list[4] = (self.ProgrEffOption.checkState())

