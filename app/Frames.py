from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QLineEdit
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from utils import functions
from app import Tools, Buttons

class MainFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(810, 210, 360, 660)
        self.setStyleSheet("background-color: black;")
        self.setVisible(True)


class Tooler(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(80, 80, 200, 500)
        self.setStyleSheet("background-color: black;")
        self.setVisible(True)

        # List of frames
        self.frames = [Tools.PluggeR(self), Tools.TaskeR(self), Tools.SupplieR(self)]

        self.current_frame_index = 1
        self.init_ui()

    def init_ui(self):

        # Create the frame label
        self.frames[self.current_frame_index].setVisible(True)
        

        # Create the "Previous" button
        previous_button = QPushButton("<", self)
        previous_button.clicked.connect(self.previous_frame)
        previous_button.setGeometry(0, 450, 15, 15)
        previous_button.setStyleSheet("background-color: black; color: white; border-style: none;") 
        #self.addWidget(previous_button)

        # Create the "Next" button
        next_button = QPushButton(">", self)
        next_button.clicked.connect(self.next_frame)
        next_button.setGeometry(30, 450, 15, 15)
        next_button.setStyleSheet("background-color: black; color: white; border-style: none;") 
        #self.addWidget(next_button)

    def previous_frame(self):
        self.frames[self.current_frame_index].setVisible(False)
        self.current_frame_index -= 1
        if self.current_frame_index < 0:
            self.current_frame_index = len(self.frames) - 1
        self.frames[self.current_frame_index].setVisible(True)
        print (self.current_frame_index)

    def next_frame(self):
        self.frames[self.current_frame_index].setVisible(False)
        self.current_frame_index += 1
        if self.current_frame_index >= len(self.frames):
            self.current_frame_index = 0
        self.frames[self.current_frame_index].setVisible(True)
        print (self.current_frame_index)




