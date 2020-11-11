from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from modules import StyleSheethHelper
from modules.ActionButton import ActionButton, ActionAddTabButton
from modules.WindowButton import WindowButton, WindowButtonClose, WindowButtonMinimize, WindowButtonMaximize
from modules.MainButton import MainButton
from modules.HistoryWidget import HistoryWidget
from modules.DownloadButton import DownloadButton
import sqlite3


class Ui_BackgroundForm(object):
    def setupUi(self, BackgroundForm):
        # region Montserrat init
        QFontDatabase.addApplicationFont("./static/fonts/Montserrat-Regular.ttf")
        fontMontserrat = QFont()
        fontMontserrat.setFamily("Montserrat")
        fontMontserrat.setPixelSize(12)
        fontMontserrat.setBold(True)
        fontMontserrat.setUnderline(False)
        fontMontserrat.setWeight(75)
        fontMontserrat.setStrikeOut(False)
        fontMontserrat.setKerning(True)
        # endregion

        # region Creating forms ...
        # region Creating background form
        BackgroundForm.setWindowFlags(Qt.FramelessWindowHint)
        BackgroundForm.setObjectName("BackgroundForm")
        BackgroundForm.resize(1074, 782)
        BackgroundForm.setMouseTracking(True)
        BackgroundForm.setAttribute(Qt.WA_TranslucentBackground, True);
        # endregion
        # region Creating form
        self.Form = QWidget(BackgroundForm)
        self.Form.setMouseTracking(False)
        self.Form.setStyleSheet(StyleSheethHelper.formFormStyleSheet_normal)
        self.Form.setObjectName("Form")
        # endregion
        # endregion
        # region Creating layouts ...
        # region Creating background layout
        self.backgroundFormLayout = QGridLayout(BackgroundForm)
        self.backgroundFormLayout.setContentsMargins(0, 0, 0, 0)
        self.backgroundFormLayout.setSpacing(3)
        self.backgroundFormLayout.setObjectName("backgroundFormLayout")
        # endregion
        # region Creating form layout
        self.formLayout = QGridLayout(self.Form)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        # endregion
        # region Creating header layout
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName("headerLayout")
        self.tabsLayout = QHBoxLayout()
        # endregion
        # region Creating layout for header buttons "close, maximize, minimize"
        self.closeMinMaxLayout = QHBoxLayout()
        self.closeMinMaxLayout.setContentsMargins(5, 0, 5, -1)
        self.closeMinMaxLayout.setSpacing(10)
        self.closeMinMaxLayout.setObjectName("closeMinMaxLayout")
        # endregion
        # region Creating search area layout
        self.searchLayout = QHBoxLayout()
        self.searchLayout.setObjectName("searchLayout")
        self.searchLayout.setContentsMargins(0, 0, 0, 6)
        self.searchLayout.setSpacing(0)
        # endregion
        # region Creating search area layout
        self.goBackForwardLayout = QHBoxLayout()
        self.goBackForwardLayout.setObjectName("goBackForwardLayout")
        self.goBackForwardLayout.setContentsMargins(0, 0, 0, 0)
        self.goBackForwardLayout.setSpacing(0)
        # endregion
        # endregion
        self.db = sqlite3.connect("qtbrowser.db")
        self.cur = self.db.cursor()
        # region Creating widgets ...
        self.webview = QWebEngineView(self.Form)
        self.webview.show()
        self.historyWidget = HistoryWidget(BackgroundForm, self.webview, self.tabsLayout)
        # region Creating main menu button
        self.btnQtMenu = MainButton(BackgroundForm, fontMontserrat)
        # endregion
        self.btnGoBack = ActionButton(BackgroundForm, "", QIcon("./static/images/arrow-left.png"),
                                      StyleSheethHelper.actionButtonStyleSheet_normal)
        self.btnReload = ActionButton(BackgroundForm, "", QIcon("./static/images/arrow-left.png"),
                                      StyleSheethHelper.actionButtonStyleSheet_normal)
        self.searchButton = ActionButton(BackgroundForm, "", QIcon("./static/images/search.png"),
                                         StyleSheethHelper.actionButtonStyleSheet_normal)
        self.btnGoForward = ActionButton(BackgroundForm, "", QIcon("./static/images/arrow-right.png"),
                                         StyleSheethHelper.actionButtonStyleSheet_normal)

        self.btnMinimize = WindowButtonMinimize(BackgroundForm, "", QIcon("./static/images/minus.png"),
                                                StyleSheethHelper.btnMinimizeStyleSheet_normal)
        self.btnMaximize = WindowButtonMaximize(BackgroundForm, "", QIcon("./static/images/maximize.png"),
                                                StyleSheethHelper.btnMaximizeStyleSheet_normal)
        self.btnClose = WindowButtonClose(BackgroundForm, "", QIcon("./static/images/close.png"),
                                          StyleSheethHelper.btnCloseStyleSheet_normal)
        self.btnAddTab = ActionAddTabButton(BackgroundForm, "", QIcon("./static/images/add.png"),
                                            StyleSheethHelper.actionButtonStyleSheet_normal)
        self.btnDownload = DownloadButton(BackgroundForm)
        # region Creating search line
        self.searchField = QLineEdit(self.Form)
        self.searchField.setFixedHeight(30)
        self.searchField.setFont(fontMontserrat)
        self.searchField.setStyleSheet(StyleSheethHelper.searchFieldStyleSheet_normal)
        # endregion
        # endregion


        # region Adding items to layouts
        self.backgroundFormLayout.addWidget(self.Form, 0, 0, 1, 1)
        self.formLayout.addLayout(self.headerLayout, 0, 0, 1, 1)
        self.formLayout.addLayout(self.searchLayout, 1, 0, 1, 1)
        self.formLayout.addWidget(self.webview, 2, 0, 1, 1)
        self.headerLayout.addWidget(self.btnQtMenu)
        self.headerLayout.addLayout(self.tabsLayout)
        self.headerLayout.addWidget(self.btnAddTab)
        self.headerLayout.addWidget(self.btnDownload)
        self.headerLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.headerLayout.addLayout(self.closeMinMaxLayout)
        self.closeMinMaxLayout.addWidget(self.btnMinimize)
        self.closeMinMaxLayout.addWidget(self.btnMaximize)
        self.closeMinMaxLayout.addWidget(self.btnClose)
        self.searchLayout.addLayout(self.goBackForwardLayout)
        self.searchLayout.addWidget(self.searchField)
        self.searchLayout.addWidget(self.searchButton)
        self.goBackForwardLayout.addWidget(self.btnGoBack)
        self.goBackForwardLayout.addWidget(self.btnGoForward)
        self.goBackForwardLayout.addWidget(self.btnReload)
        # endregion

        self.retranslateUi(BackgroundForm)
        QMetaObject.connectSlotsByName(BackgroundForm)

    def retranslateUi(self, BackgroundForm):
        _translate = QCoreApplication.translate
        BackgroundForm.setWindowTitle(_translate("BackgroundForm", "QtBrowser"))
