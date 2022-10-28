import sys
import enum

import PyQt6
from PyQt6 import QtCore
from PyQt6.QtWidgets import \
    QApplication, QMainWindow


class mainWindowGeometryConstants(enum.IntEnum):
    WINDOW_X, WINDOW_Y = 0, 0
    WINDOW_WIDTH, WINDOW_HEIGHT = 430, 450


# главное окно приложения 'менеджера паролей'
class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        # настройка параметров окна:
        self.setWindowTitle("password manager")
        self.setGeometry(
            mainWindowGeometryConstants.WINDOW_X,
            mainWindowGeometryConstants.WINDOW_Y,
            mainWindowGeometryConstants.WINDOW_WIDTH,
            mainWindowGeometryConstants.WINDOW_HEIGHT)


def runApplication():
    """
    запускает приложение 'менеджер паролей'.
    """

    passwordManagerApplication = QApplication(sys.argv)

    window = mainWindow()
    window.show()

    sys.exit(passwordManagerApplication.exec())