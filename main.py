import sys
from view.estoque import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication


class MainWindow:
    def __init__(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == '__main__':
    app = QApplication()

    win = MainWindow()

    sys.exit(app.exec())