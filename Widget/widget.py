from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainterPath, QRegion, QColor, QPainter, QPen
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transparent Window")
        self.setGeometry(100, 100, 100, 100)

        # Set window attributes for transparency and frameless window
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        '''button = QPushButton("O", self)
        button.setGeometry(50, 50, 100, 100)'''

        # Create a custom circular shape for the window
        self.custom_shape = QPainterPath()
        self.custom_shape.addEllipse(0, 0, self.width(), self.height())
        region = QRegion(self.custom_shape.toFillPolygon().toPolygon())
        self.setMask(region)

    def paintEvent(self, event):
        painter = QPainter(self)
        # Enable antialiasing and smooth pixmap transformation
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        # Set the window background color with transparency
        painter.setBrush(QColor(255, 255, 255, 150))
        
        # Set the window outline color and width
        painter.setPen(QPen(Qt.white, 5))
        
        # Draw the window outline with the same shape as the window
        painter.drawPath(self.custom_shape)

        
        



if __name__ == "__main__":
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
