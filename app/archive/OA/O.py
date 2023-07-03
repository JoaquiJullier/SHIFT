import sys
from data import DataBase
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFrame, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont, QIcon, QPainter
from PyQt5.QtCore import Qt, QPoint



        




class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.darkmode = True


        screen_size = [1980, 1080]
        window_size = [1980, 1080]
        frame1_size = [int(1980/3), int(1080/3)]

        self.setWindowTitle('OI')
        self.setGeometry(0, 0, window_size[0], window_size[1])
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.tasker = QFrame(self)
        self.tasker.setGeometry(810, 210, 360, 660)
        self.tasker.setStyleSheet("background-color: black;")
        self.tasker.setVisible(True)

        self.botonera = QFrame(self.tasker)
        self.botonera.setGeometry(50, 500, 130, 15)
        self.botonera.setStyleSheet("background-color: black;")
        self.botonera.setVisible(True)
        self.Tbutton = QPushButton('+', self.botonera)
        self.Tbutton.setGeometry(0, 0, 15, 15)
        self.Tbutton.clicked.connect(lambda: self.press_TButton())
        self.Tbutton.setStyleSheet("background-color: black; color: white; border-style: none;")
        self.Obutton = QPushButton('O', self.botonera)
        self.Obutton.setGeometry(30, 0, 15, 15)
        self.Obutton.clicked.connect(lambda: self.press_OButton())
        self.Obutton.setStyleSheet("background-color: black; color: white; border-style: none;")
        self.Xbutton = QPushButton('X', self.botonera)
        self.Xbutton.setGeometry(60, 0, 15, 15)
        self.Xbutton.clicked.connect(lambda: self.press_XButton())
        self.Xbutton.setStyleSheet("background-color: black; color: white; border-style: none;")
        self.Ibutton = QPushButton('I', self.botonera)
        self.Ibutton.setGeometry(90, 0, 15, 15)
        self.Ibutton.clicked.connect(lambda: self.press_IButton())
        self.Ibutton.setStyleSheet("background-color: black; color: white; border-style: none;")

        self.list = QLabel(self.tasker)
        self.list.setGeometry(50, 60, 175, 200)
        self.list.setText("L i n k   O I   w i t h   S Q L  \n\nC r e a t e   s i m p l e   d a t a b a s e ")
        self.list.setStyleSheet("background-color: black; font-weight: light; color: white")
        
        self.prompter = QLineEdit(self.tasker)
        self.prompter.setGeometry(50, 550, 200, 30)
        self.prompter.setStyleSheet("background-color: black; color: white; border-radius: 5px; border: none;")
        self.prompter.setFocus()
        self.prompter.displayText()

    




    def press_TButton(self):
        print('TButton')
        self.add_task()

    def press_OButton(self):
        print('OButton')
        self.delete_first_task()

    def press_XButton(self):
        print('XButton')
        self.close_app()

    def press_IButton(self):
        print('IButton')
        self.switch_light_mode()








    def add_task(self):
        new_task = self.prompter.text()
        DataBase.add_task(new_task)
        self.prompter.clear()
        self.prompter.setFocus()

    def switch_light_mode(self):
        if self.darkmode == True:
            self.tasker.setStyleSheet("background-color: white;")
            self.list.setStyleSheet("background-color: white; font-weight: light; color: black")
            self.botonera.setStyleSheet("background-color: white;")
            self.Tbutton.setStyleSheet("background-color: white; color: black; border-style: none;")
            self.Obutton.setStyleSheet("background-color: white; color: black; border-style: none;")
            self.Xbutton.setStyleSheet("background-color: white; color: black; border-style: none;")
            self.Ibutton.setStyleSheet("background-color: white; color: black; border-style: none;")
            self.prompter.setStyleSheet("background-color: white; font-weight: light; color: black; border: none;")
            self.prompter.setFocus()
            self.darkmode = False
            print('SWITCHED TO DAY MODE')
        else:
            self.tasker.setStyleSheet("background-color: black;")
            self.list.setStyleSheet("background-color: black; font-weight: light; color: white; border: none;")
            self.botonera.setStyleSheet("background-color: black;")
            self.Tbutton.setStyleSheet("background-color: black; color: white; border-style: none;")
            self.Obutton.setStyleSheet("background-color: black; color: white; border-style: none;")
            self.Xbutton.setStyleSheet("background-color: black; color: white; border-style: none;")
            self.Ibutton.setStyleSheet("background-color: black; color: white; border-style: none;")
            self.prompter.setStyleSheet("background-color: black; font-weight: light; color: white; border: none;")
            self.prompter.setFocus()
            self.darkmode = True
            print('SWITCHED TO NIGHT MODE')


    def delete_first_task(self):
        DataBase.delete_first_task()


    def close_app(self):
        QApplication.instance().quit()
        print('APP CLOSED')











if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())