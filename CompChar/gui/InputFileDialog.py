from PyQt5.QtWidgets import QWidget, QFileDialog

class InputFileDialog(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выбор MF-файла')
        self.file_name = file_name[0]

    def get_name(self):
        return  self.file_name

