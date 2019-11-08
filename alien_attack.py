#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""============================================================================

    Alien Attack

    This purpose of this game setup, is to teach and demonstrate techniques, 
    for making applications and games in a collaborating team.

    The intention is to set up a framework, for building a game, in a relatively 
    short time, without the hassle of writing a game from scratch each time, 
    but maintaining a loose understanding of how things work.
    Originally designed for Coding Pirates - Helsinge Denmark, 
    By Simon Rigét 2019
    ----------------------------------------------------------------------------
    Requires pygame, Qt5 and PyQtWebEngine libraries to be installed.

    ----------------------------------------------------------------------------

    The game it self, is wrapped in a Qt application, with a few pages, for 
    managing the game and setup etc.
    ----------------------------------------------------------------------------

============================================================================"""
import sys
import os

from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QListWidget, QStackedWidget, QApplication,
                             QHBoxLayout, QListWidgetItem, QLabel)

from game_objects import game_play


class MainPage():
    def __init__(self, navigate):
        self.widget = uic.loadUi(os.path.join(qt_path,'main_page.ui'))

        self.widget.credits_button.clicked.connect(lambda: navigate("credits_page"))
        self.widget.play_button.clicked.connect(lambda: navigate("play"))
        self.widget.exit_button.clicked.connect(lambda: navigate("exit"))

class CreditsPage():
    def __init__(self, navigate):
        self.widget = uic.loadUi(os.path.join(qt_path,'credits_page.ui'))

        self.widget.back_button.clicked.connect(lambda: navigate("main_page"))


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.resize(1000, 700)

        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.stacked_widget = QStackedWidget(self)
        layout.addWidget(self.stacked_widget)

        self.page = {}
        self.page['main_page'] = self.stacked_widget.addWidget(MainPage(self.navigate).widget)
        self.page['credits_page'] = self.stacked_widget.addWidget(CreditsPage(self.navigate).widget)

        self.show()

    def navigate(self, lable):
        print(lable)
        if lable in self.page:
            self.stacked_widget.setCurrentIndex(self.page[lable])

        elif lable == 'exit':
            sys.exit(0)

        elif lable == 'play':
            app.game = game_play.Game()

            
app = QApplication(sys.argv)
# app.setStyleSheet(Stylesheet)

root_path = os.path.join(os.path.dirname(__file__))
root_path = root_path
qt_path   = os.path.join(root_path,'qt')
game_path = os.path.join(root_path,'pame_play')
html_path = os.path.join(root_path,'qt','html')


app.globals = {
    'root_path' : root_path,
    'qt_path'   : os.path.join(root_path,'qt'),
    'game_path' : os.path.join(root_path,'pame_play'),
    'html_path' : os.path.join(root_path,'qt','html'),

    'game'      : game_play,
}

window = MainWindow()
window.app = app
app.exec_()

