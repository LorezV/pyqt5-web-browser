from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


class BrowserButton(QPushButton):
    def __init__(self, widget, bText, bSize, bIcon=None, bStylesheet=None, bIconSize=None):
        super().__init__()

        self.bText = bText
        self.bSize = bSize
        self.bIcon = bIcon
        self.bStylesheet = bStylesheet
        self.bIconSize = bIconSize

        self.setupUi()

    def setupUi(self):
        self.setText(self.bText)
        self.setFixedSize(self.bSize)

        if self.bIconSize is not None:
            self.setIconSize(self.bIconSize)

        if self.bStylesheet is not None:
            self.setStyleSheet(self.bStylesheet)

        if self.bIcon is not None:
            self.setIcon(self.bIcon)
