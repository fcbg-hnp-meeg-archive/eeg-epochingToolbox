from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QIcon
import sys
import os

print('CURRENT DIRECTORY FOLDER : ', os.getcwd())

from app.epoching import EpochingWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = EpochingWindow()
    main.show()
    sys.exit(app.exec_())
