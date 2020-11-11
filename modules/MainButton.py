from PyQt5.QtWidgets import QMenu, QMenuBar, QAction
from modules import StyleSheethHelper
from modules.BrowserTab import BrowserTab


class MainButton(QMenuBar):
    def __init__(self, widget, font):
        super().__init__()
        self.font = font
        self.widget = widget

        self.MenuQtBrowser = QMenu(self)
        self.addMenu(self.MenuQtBrowser)

        self.newTabAction = QAction('&Новая вкладка', self.widget)
        self.newTabAction.triggered.connect(self.create_tab)
        self.MenuQtBrowser.addAction(self.newTabAction)

        self.historyAction = QAction("&История", self.widget)
        self.historyAction.triggered.connect(widget.historyWidget.open)
        self.MenuQtBrowser.addAction(self.historyAction)

        self.setupUi()

    def setupUi(self):
        self.MenuQtBrowser.setTitle("QtBrowser")
        self.setStyleSheet(StyleSheethHelper.btnQtMenuStyleSheet_normal)
        self.setFixedSize(150, 30)
        self.setFont(self.font)
        self.newTabAction.setFont(self.font)
        self.historyAction.setFont(self.font)

    def create_tab(self):
        try:
            BrowserTab(self.widget, self.widget.webview, self.widget.tabsLayout).set_tab()
        except AssertionError:
            print("Максимальное кол-во вкладок!")