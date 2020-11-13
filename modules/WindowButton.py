from modules.ActionButton import ActionButton
from PyQt5.QtCore import QSize


class WindowButton(ActionButton):
    def __init__(self, widget, b_text, b_icon, b_stylesheet):
        super().__init__(widget, b_text, b_icon, b_stylesheet)

        self.widget = widget
        self.bText = b_text
        self.bIcon = b_icon
        self.bStylesheet = b_stylesheet
        self.setup_ui()

    def setup_ui(self):
        super().setup_ui()
        self.setFixedSize(QSize(15, 15))
        self.setIconSize(QSize(13, 13))


class WindowButtonMaximize(WindowButton):
    def __init__(self, widget, b_text, b_icon, b_stylesheet):
        super().__init__(widget, b_text, b_icon, b_stylesheet)
        self.clicked.connect(self.widget.changeWindowState)


class WindowButtonMinimize(WindowButton):
    def __init__(self, widget, b_text, b_icon, b_stylesheet):
        super().__init__(widget, b_text, b_icon, b_stylesheet)
        self.clicked.connect(self.widget.showMinimized)


class WindowButtonClose(WindowButton):
    def __init__(self, widget, b_text, b_icon, b_stylesheet):
        super().__init__(widget, b_text, b_icon, b_stylesheet)

        self.clicked.connect(self.close)

    def close(self):
        self.widget.db.close()
        self.widget.close()
