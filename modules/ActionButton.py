from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from modules.BrowserTab import BrowserTab


class ActionButton(QPushButton):
    def __init__(self, widget, b_text, b_icon, b_stylesheet):
        super().__init__(widget)

        self.widget = widget
        self.bText = b_text
        self.bIcon = b_icon
        self.bStylesheet = b_stylesheet

        self.setup_ui()

    def setup_ui(self):
        self.setText(self.bText)
        self.setIcon(self.bIcon)
        self.setFixedSize(QSize(30, 30))
        self.setIconSize(QSize(15, 15))
        self.setStyleSheet(self.bStylesheet)


class ActionAddTabButton(ActionButton):
    def __init__(self, widget, b_text, b_icon, b_stylesheet):
        super().__init__(widget, b_text, b_icon, b_stylesheet)
        self.clicked.connect(self.create_tab)

    def create_tab(self):
        try:
            BrowserTab(self.widget, self.widget.webview, self.widget.tabsLayout).set_tab()
        except AssertionError:
            print("Максимальное кол-во вкладок!")
