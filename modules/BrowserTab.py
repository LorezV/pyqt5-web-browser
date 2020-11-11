from PyQt5.QtWidgets import QPushButton


class BrowserTap(QPushButton):
    def __init__(self, webview, container_layout):
        super().__init__()
        self.setupUi()
        
        container_layout.addWidget(self)

    def setupUi(self):
        self.setMinimumHeight(30)
