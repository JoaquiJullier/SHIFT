import sys
from app import Frames, Buttons, Tools

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt


'''

UPDATES

1 - Como almacenar variables constantes
2 - Crear sistema de coordenadas 


IDEAS

1 - Implementar cambio de color segun horario del dial

'''

class Main(QWidget):
    def __init__(self, app, screen):
        super().__init__()

        #WINDOW IMPLEMENTATION
        #new parameters generated
        self.darkmode = True
        self.screen_size = screen
        #parameter configuration
        self.setGeometry(0, 0, self.screen_size[0], self.screen_size[1])
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # MAIN FRAME IMPLEMENTATION
        # Generate main frame
        self.main_frame = Frames.MainFrame(self)
        # Add button to close de app
        self.close_app_button = Buttons.XButton(self.main_frame, app)
        # Add button to change light mode
        self.change_lightmode_button = Buttons.OButton(self.main_frame)
        # Add tooler
        self.plugger = Frames.Tooler(self.main_frame)