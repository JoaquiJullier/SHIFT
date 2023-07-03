import PyQt5

class Prompter(PyQt5.QtWidgets.QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(80, 550, 200, 30)
        self.setStyleSheet("background-color: black; color: white; border: none;")
        self.setFocus()
        self.displayText()