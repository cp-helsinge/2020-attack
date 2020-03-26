#!/usr/bin/env python3 
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
from PyQt5 import uic, QtCore, QtWidgets, QtGui
import game
import config

config.root_path     = os.path.join(os.path.dirname(__file__))       # Root of this package
config.qt_path       = os.path.join(config.root_path,'qt')           # root of QT application files
config.game_obj_path = os.path.join(config.root_path,'game_objects') # Game program objects
config.html_path     = os.path.join(config.root_path,'qt','html')    # QT HTML pages
config.gfx_path      = os.path.join(config.root_path,'gfx')          # Graphic art and sprites
config.sound_path    = os.path.join(config.root_path,'sound')        # sound effects and music

config.screen_width  = 1000
config.screen_height = 700


# Create a widget, using a HTML file (located in the html_path.
# The  widget can only interpret simple HTML. It uses a subset of HTML 3.2 and 4. And css 2.1
# External links wil be opned in the system browser, where as internal links wil be followed 
# in the document root directory (html_path)
# If you need a comprehensive HTML browser, use the QWebEngine module.
class SimpleHTMLPage:
    def __init__(self, url):
        self.widget = QtWidgets.QTextBrowser()
        # Enable external links to be opened in the system browser
        self.widget.setOpenExternalLinks(True)
        # Load the HTML, markdown or text file
        self.widget.setSource(QtCore.QUrl().fromLocalFile(os.path.join(config.html_path,url)))


class MainPage():
    def __init__(self, navigate):
        # Load a UI resource file
        self.widget = uic.loadUi(os.path.join(config.qt_path,'main_page.ui'))

        # Attach action to buttons
        self.widget.credits_button.clicked.connect(lambda: navigate("credits_page"))
        self.widget.boring_button.clicked.connect(lambda: navigate("boring_page"))
        self.widget.play_button.clicked.connect(lambda: navigate("play"))
        self.widget.exit_button.clicked.connect(lambda: navigate("exit"))


class MainWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Set screen size
        self.resize(1000, 700)

        # Create window and let staged widged contain all the pages used.
        layout = QtWidgets.QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        layout.addWidget(self.stacked_widget)
        
        # Create a back button (on all other pages than manin page)
        self.back_button = QtWidgets.QPushButton(QtGui.QIcon('qt/back.png'),"",self)
        self.back_button.setGeometry(QtCore.QRect(20, 20, 100, 100))
        self.back_button.setIconSize(QtCore.QSize(150, 150))
        self.back_button.clicked.connect(lambda: self.navigate("main_page"))
        self.back_button.hide()

        # Create stack of pages
        self.page = {}
        self.page['main_page'] = self.stacked_widget.addWidget(MainPage(self.navigate).widget)
        self.page['credits_page'] = self.stacked_widget.addWidget(SimpleHTMLPage('credits.html').widget)
        self.page['boring_page'] = self.stacked_widget.addWidget(SimpleHTMLPage('boring.html').widget)

        self.keyPressEvent = self.newOnkeyPressEvent
        self.show()

    # Handle key inputs
    def newOnkeyPressEvent(self,e):
        for page_name, stack_index in self.page.items():
            if stack_index == self.stacked_widget.currentIndex():
                if page_name == 'main_page':
                    if e.key() == QtCore.Qt.Key_Escape:
                        self.navigate('exit')
                    if e.key() == QtCore.Qt.Key_Return:
                        self.navigate('play')
                else:
                    self.navigate('main_page')

    # Navigate
    def navigate(self, page_name):
        #Hide back button, on main page
        if page_name == 'main_page':
            self.back_button.hide()
        else:
            self.back_button.show()

        # Go to page
        if page_name in self.page:
            self.stacked_widget.setCurrentIndex(self.page[page_name])
            # Let simple HTML pages be reloaded to its homepage. (Might have followed a link) 
            if isinstance(self.stacked_widget.currentWidget(), QtWidgets.QTextBrowser):
                self.stacked_widget.currentWidget().home()
                self.stacked_widget.currentWidget().reload()

        # Exit
        elif page_name == 'exit':
            sys.exit(0)

        # Start game
        elif page_name == 'play':
            self.hide()
            current_game = game.Game()
            current_game.start()
            del current_game
            self.show()
            self.back_button.hide()

# Start application
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()

config.window        = window
config.app           = app

app.exec_()


