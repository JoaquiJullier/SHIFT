import unittest
from PyQt5.QtWidgets import QApplication
from app.main_window import MainWindow

class TestMainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a single instance of QApplication
        cls.app = QApplication([])

    @classmethod
    def tearDownClass(cls):
        # Clean up after all tests are finished
        cls.app.quit()

    def setUp(self):
        # Create an instance of MainWindow for each test
        self.main_window = MainWindow()

    def tearDown(self):
        # Clean up after each test
        self.main_window.close()

    def test_window_title(self):
        self.assertEqual(self.main_window.windowTitle(), 'Main Window')

    def test_window_size(self):
        expected_size = (800, 600)
        self.assertEqual(self.main_window.size().width(), expected_size[0])
        self.assertEqual(self.main_window.size().height(), expected_size[1])

if __name__ == '__main__':
    unittest.main()
