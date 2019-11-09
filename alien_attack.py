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

from PyQt5 import uic, QtCore, QtWebEngineWidgets
from PyQt5.QtWidgets import (QWidget, QListWidget, QStackedWidget, QApplication,
                             QHBoxLayout, QListWidgetItem, QLabel)

from game_objects import game_play
from game_objects import globals


class MainPage():
    def __init__(self, navigate):
        self.widget = uic.loadUi(os.path.join(qt_path,'main_page.ui'))

        self.widget.credits_button.clicked.connect(lambda: navigate("credits_page"))
        self.widget.boring_button.clicked.connect(lambda: navigate("boring_page"))
        self.widget.play_button.clicked.connect(lambda: navigate("play"))
        self.widget.exit_button.clicked.connect(lambda: navigate("exit"))

class CreditsPage():
    def __init__(self, navigate):
        self.widget = uic.loadUi(os.path.join(qt_path,'credits_page.ui'))
        with open( os.path.join(html_path,'credits.html'), 'r' ) as html_file:
            self.widget.text.setText( html_file.read() ) 

        self.widget.back_button.clicked.connect(lambda: navigate("main_page"))

class BoringPage():
    def __init__(self, navigate):
        self.widget = uic.loadUi(os.path.join(qt_path,'boring_page.ui'))
        with open( os.path.join(html_path,'boring.html'), 'r' ) as html_file:
            self.widget.text_1.setText( html_file.read() ) 
        self.widget.text_2.setText(boring_text) 
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
        self.page['boring_page'] = self.stacked_widget.addWidget(BoringPage(self.navigate).widget)

        self.show()

    def navigate(self, page_name):
        if page_name in self.page:
            self.stacked_widget.setCurrentIndex(self.page[page_name])

        elif page_name == 'exit':
            sys.exit(0)

        elif page_name == 'play':
            globals.game = game_play.Game()
            globals.game.next_level(1)
            globals.game.loop()
            del globals.game


app = QApplication(sys.argv)
# app.setStyleSheet(Stylesheet)

globals.root_path = root_path = os.path.join(os.path.dirname(__file__))
globals.qt_path   = qt_path   = os.path.join(root_path,'qt')
globals.game_path = game_path = os.path.join(root_path,'game_objects')
globals.html_path = html_path = os.path.join(root_path,'qt','html')
globals.gfx_path  = gfx_path  = os.path.join(root_path,'gfx')

boring_text = """
<div style="  display: inline-block; vertical-align: middle;">
    Developed by Martin Kristensen @ Coding Pirates 2020 <img src="qt/coding_pirates.png">
</div>
<div style="  display: inline-block; vertical-align: middle;">
Original design by Simon Rigét @ Coding Pirates 2019 <img src="qt/coding_pirates.png">
</div>
"""

window = MainWindow()
window.app = app
app.exec_()

