from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QLineEdit
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt
from utils import functions
from app import Tools


class PluggeR(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(0, 0, (360-90*2), (660-180*2))
        self.setStyleSheet("background-color: black;")
        self.setVisible(False)
        self.init_ui()

    def init_ui(self):
        # Create the label to display the stopwatch time
        self.time_label = QLabel("00:00:00", self)
        self.time_label.setGeometry(0, 0, 200, 15)
        self.time_label.setStyleSheet("background-color: black; font-weight: light; color: white; font-size: 12px;")
        #main_layout.addWidget(self.time_label)



        # Initialize the stopwatch variables
        self.elapsed_time = QTime(0, 0)
        self.is_running = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_stopwatch)

        self.start_button = QPushButton(">", self)
        self.start_button.setGeometry(0, 220, 15, 15)
        self.start_button.setStyleSheet("background-color: black; font-weight: light; color: white; font-size: 12px;")
        self.start_button.clicked.connect(self.start_cronometer)

        self.pause_button = QPushButton("H", self)
        self.pause_button.setGeometry(0, 250, 15, 15)
        self.pause_button.setStyleSheet("background-color: black; font-weight: light; color: white; font-size: 12px;")
        self.pause_button.clicked.connect(self.pause_cronometer)

        self.stop_button = QPushButton("A", self)
        self.stop_button.setGeometry(0, 290, 15, 15)
        self.stop_button.setStyleSheet("background-color: black; font-weight: light; color: white; font-size: 12px;")
        self.stop_button.clicked.connect(self.stop_cronometer)


    def start_cronometer(self):
        if not self.is_running:
            self.timer.start(1000)  # Update every second (1000 milliseconds)
            self.is_running = True

    def pause_cronometer(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False

    def stop_cronometer(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
        else:
            self.timer.stop()
            self.is_running = False
            self.elapsed_time = QTime(0, 0)
            self.time_label.setText("00:00:00")

    def update_stopwatch(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        time_text = self.elapsed_time.toString("hh:mm:ss")
        self.time_label.setText(time_text)


class TaskeR(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(0, 0, 200, 400)
        self.setStyleSheet("background-color: black;")
        self.setVisible(False)

        # Generating list connected to db
        self.list = QLabel(self)
        self.list.setGeometry(0, 0, 175, 200)
        self.list.setText("L i n k   O I   w i t h   S Q L  \n\nC r e a t e   s i m p l e   d a t a b a s e ")
        self.list.setStyleSheet("background-color: black; font-weight: light; color: white")
        # Generating shortcut buttons frame
        self.botonera = QFrame(self)
        self.botonera.setGeometry(0, 385, 130, 15)
        self.botonera.setStyleSheet("background-color: black;")
        self.botonera.setVisible(True)
        # Generating buttons
        self.Tbutton = QPushButton('+', self.botonera)
        self.Tbutton.setGeometry(0, 0, 15, 15)
        self.Tbutton.clicked.connect(functions.press_TButton)
        self.Tbutton.setStyleSheet("background-color: black; color: white; border-style: none;")
        self.Obutton = QPushButton('O', self.botonera)
        self.Obutton.setGeometry(30, 0, 15, 15)
        self.Obutton.clicked.connect(functions.press_OButton)
        self.Obutton.setStyleSheet("background-color: black; color: white; border-style: none;")




class SupplieR(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(0, 0, 200, 400)
        self.setStyleSheet("background-color: black;")
        self.setVisible(False)