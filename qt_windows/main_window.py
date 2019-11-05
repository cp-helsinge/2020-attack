#from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic

# Sub Windows
from qt_windows import credits_window
from game_objects import game

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('qt_windows/main_window.ui', self)
        self.show()
        self._credits_window = None
        
        self.button_play = self.findChild(QtWidgets.QPushButton, 'play')
        self.button_play.clicked.connect(self.on_button_play)
        self.button_credits = self.findChild(QtWidgets.QPushButton, 'credits')
        self.button_credits.clicked.connect(self.on_button_credits)

    def on_button_play(self):
        game = game_objects.Game()
        game.loop()
        del game

    def on_button_credits(self):
        self._credits_window = credits_window.CreditsWindow()
        self._credits_window.show()



