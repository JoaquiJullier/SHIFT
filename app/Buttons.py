from PyQt5.QtWidgets import QPushButton
import PyQt5
from utils import functions

class LButton(PyQt5.QtWidgets.QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText("<")
        self.setGeometry(0, 450, 15, 15)
        self.clicked.connect(functions.go_left(parent))
        self.setStyleSheet("background-color: black; color: white; border-style: none;")

class RButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText(">")
        self.setGeometry(185, 450, 15, 15)
        self.clicked.connect(functions.go_right(parent))
        self.setStyleSheet("background-color: black; color: white; border-style: none;")   
        
class XButton(QPushButton):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.setText("X")
        self.setGeometry(325, 20, 15, 15)
        self.clicked.connect(lambda: functions.close_app(app))
        self.setStyleSheet("background-color: black; color: white; border-style: none;")

class OButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText("O")
        self.setGeometry(20, 20, 15, 15)
        self.clicked.connect(functions.switch_light_mode)
        self.setStyleSheet("background-color: black; color: white; border-style: none;")