import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Carousel Example")
        self.setGeometry(100, 100, 400, 300)

        #self.carousel_widget = QStackedWidget(self)
        #self.carousel_widget.setGeometry(50, 50, 300, 200)

        self.page_labels = []  # List to store the labels/pages of the carousel

        # Create and add pages to the carousel
        for i in range(5):
            page_label = QLabel(f"Page {i + 1}", self)
            page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.carousel_widget.addWidget(page_label)
            self.page_labels.append(page_label)

        # Timer to switch pages automatically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_page)
        self.timer.start(2000)  # Switch pages every 2 seconds

    def change_page(self):
        current_index = self.carousel_widget.currentIndex()
        next_index = (current_index + 1) % self.carousel_widget.count()
        self.carousel_widget.setCurrentIndex(next_index)

# Create the application
app = QApplication(sys.argv)

# Create the main window
main_window = MainWindow()

# Show the main window
main_window.show()

# Run the event loop
sys.exit(app.exec())
