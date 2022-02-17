from .src import Handler
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Handler()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


main()
