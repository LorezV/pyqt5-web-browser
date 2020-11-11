from PyQt5.QtWidgets import QHBoxLayout, QPushButton
from PyQt5.QtCore import QUrl
from modules import StyleSheethHelper
from modules.WebPage import WebPage


class BrowserTab(QHBoxLayout):
    listOfTabs = list()
    chosenTab = None

    def __init__(self, widget, webview, container_layout):
        #if len(BrowserTab.listOfTabs) >= 100:
        #    del self
        #    assert False
        super().__init__()
        self.recentPages = list()
        self.positionInList = -1

        self.widget = widget
        self.container_layout = container_layout
        self.webview = webview
        BrowserTab.listOfTabs.append(self)

        self.webpage = WebPage()
        self.btnInfo = QPushButton(self.widget)
        self.btnCloseTab = QPushButton(self.widget)

        self.setupUi()

    def setupUi(self):
        self.btnInfo.clicked.connect(self.info_clicked_hook)
        self.webpage.loadFinished.connect(self.page_loadfinished_hook)
        self.btnCloseTab.clicked.connect(self.page_close)
        self.webpage.urlChanged.connect(self.page_urlchanged_hook)

        self.webpage.load(QUrl("https://ya.ru"))

        self.btnInfo.setMaximumSize(150, 30)
        self.btnInfo.setStyleSheet(StyleSheethHelper.browserTabStyleSheet)
        self.btnCloseTab.setFixedSize(30, 30)
        self.btnCloseTab.setStyleSheet(
            StyleSheethHelper.browserTabStyleSheet + StyleSheethHelper.browserCloseTabStyleSheet)

        self.addWidget(self.btnInfo)
        self.addWidget(self.btnCloseTab)
        self.container_layout.addLayout(self)

    def info_clicked_hook(self):
        if BrowserTab.chosenTab is not self:
            self.set_tab()

    def page_urlchanged_hook(self):
        self.recentPages.append(self.webpage.url())
        self.positionInList += 1

    def page_loadfinished_hook(self):
        self.btnInfo.setText(self.webpage.title())

    def set_tab(self):
        BrowserTab.chosenTab.btnInfo.setStyleSheet(StyleSheethHelper.browserTabStyleSheet)
        BrowserTab.chosenTab.btnCloseTab.setStyleSheet(
            StyleSheethHelper.browserTabStyleSheet + StyleSheethHelper.browserCloseTabStyleSheet)
        BrowserTab.chosenTab = self
        self.btnInfo.setStyleSheet(StyleSheethHelper.browserTabStyleSheet_chosen)
        self.btnCloseTab.setStyleSheet(
            StyleSheethHelper.browserTabStyleSheet_chosen + StyleSheethHelper.browserCloseTabStyleSheet)
        self.webview.setPage(self.webpage)

    def page_close(self):
        BrowserTab.listOfTabs.remove(self)
        if BrowserTab.chosenTab == self:
            if len(BrowserTab.listOfTabs) >= 1:
                BrowserTab.listOfTabs[-1].set_tab()
            else:
                BrowserTab(self.widget, self.widget.webview, self.widget.tabsLayout).set_tab()
        self.btnInfo.deleteLater()
        self.btnCloseTab.deleteLater()
        self.webpage.deleteLater()
        self.deleteLater()
        del self
