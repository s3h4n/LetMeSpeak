from .src import Handler
from .packages import ConnectionHelper
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def main():
    if not ConnectionHelper.is_active():
        print("NetworkError: Internet Connection Is Required!")
        sys.exit()

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Handler()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
