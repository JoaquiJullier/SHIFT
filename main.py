import PyQt5
from PyQt5.QtWidgets import QApplication, QDesktopWidget

from app import Windows

def main():

    app = PyQt5.QtWidgets.QApplication([])
    
    screen = QDesktopWidget().screenGeometry()
    screen = (screen.width(), screen.height())
    
    main_window = Windows.Main(app, screen)
    main_window.show()
    
    app.exec_()


if __name__ == '__main__':
    main()


