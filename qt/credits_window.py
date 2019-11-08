from PyQt5 import QtWidgets, uic

class CreditsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CreditsWindow, self).__init__()
        self._label = QtWidgets.QLabel('Hello, is it me you\'re looking for?')
        self.setCentralWidget(self._label)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = CreditsWindow()
    gui.show()
    app.exec_()