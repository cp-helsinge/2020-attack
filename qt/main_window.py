"""
from random import randint
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui  import QIcon
from PyQt5.QtWidgets import (QWidget, QListWidget, QStackedWidget, 
                             QHBoxLayout, QListWidgetItem, QLabel)
from PyQt5 import QtWidgets, uic
"""
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui  import QIcon
from PyQt5.QtWidgets import (QWidget, QListWidget, QStackedWidget, 
                             QHBoxLayout, QListWidgetItem, QLabel)
from PyQt5 import uic

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.page = {}

        self.stackedWidget = QStackedWidget(self)

        self.page['main_page'] = self.stackedWidget.addWidget(uic.loadUi('qt_windows/main_page.ui') )

        self.show()

   