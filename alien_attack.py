#from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
import sys
import os
from game_objects import globals

globals.root_path = os.path.join(os.path.dirname(__file__))

# Windows
from qt_windows import main_window
from qt_windows import credits_window

app = QtWidgets.QApplication(sys.argv)
print(app)
window = main_window.MainWindow()
app.exec_()
