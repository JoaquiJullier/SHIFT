import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFrame, QLineEdit
from PyQt5.QtGui import QFont, QIcon, QPainter
from PyQt5.QtCore import Qt, QPoint

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('OA')
        self.setGeometry(0, 0, 1000, 1000)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.frame1 = QFrame(self)
        self.frame1.setGeometry(50, 50, 50, 50)
        self.frame1.setStyleSheet("background-color: white; border-radius: 15px;")
        self.button1 = QPushButton('+', self)
        self.button1.setGeometry(50, 50, 50, 50)
        self.button1.clicked.connect(lambda: self.show_or_hide_frame(self.frame2))
        self.button1.setStyleSheet("background-color: yellow; border-radius: 5px;")

        self.frame2 = QFrame(self)
        self.frame2.setGeometry(110, 50, 200, 200)
        self.frame2.setStyleSheet("background-color: white; border-radius: 15px;")
        self.frame2.setVisible(False)
        self.label = QLabel(self.frame2)
        self.label.setGeometry(15, 15, 130, 30)
        self.label.setText("  TO DO LIST:")
        self.label.setStyleSheet("background-color: white; font-weight: bold;")
        self.label = QLabel(self.frame2)
        self.label.setGeometry(15, 55, 130, 30)
        self.label.setText("-")
        self.label.setStyleSheet("background-color: yellow; font-weight: bold;")
        self.button2 = QPushButton('+', self.frame2)
        self.button2.setGeometry(100, 15, 30, 30)
        self.button2.setStyleSheet("background-color: yellow; border-radius: 15px;")
        self.button2.clicked.connect(lambda: self.show_or_hide_frame(self.frame3))

        self.task_input = QLineEdit(self.frame2)
        self.task_input.setGeometry(15, 155, 140, 30)
        self.task_input.setStyleSheet("background-color: yellow; border-radius: 5px;")
        self.task_input.returnPressed.connect(self.get_input_text)
        self.task_input.displayText()

        self.button3 = QPushButton('+', self.frame2)
        self.button3.setGeometry(160, 155, 30, 30)
        self.button3.setStyleSheet("background-color: yellow; border-radius: 15px;")
        self.button3.clicked.connect(lambda: self.add_to_database(self.task_input))

        self.frame3 = QFrame(self)
        self.frame3.setGeometry(270, 50, 400, 400)
        self.frame3.setStyleSheet("background-color: white; border-radius: 15px;")
        self.frame3.setVisible(False)


    def show_or_hide_frame(self, frame):
        if frame.isVisible():
            frame.setVisible(False)
        else:
            frame.setVisible(True)    

    def get_input_text(self):
        text = self.task_input.text()
        print("Input Text:", text)

    def add_to_database(self, text):
        print(text.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())