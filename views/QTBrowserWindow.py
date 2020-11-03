from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from views import StyleSheethHelper


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
        # endregion

        # region Creating widgets ...
        # region Creating main menu button
        self.btnQtMenu = QPushButton(self.Form)
        self.btnQtMenu.setMinimumSize(QSize(150, 30))
        self.btnQtMenu.setMaximumSize(QSize(150, 30))
        self.btnQtMenu.setFont(fontMontserrat)
        self.btnQtMenu.setStyleSheet(StyleSheethHelper.btnQtMenuStyleSheet_normal)
        self.btnQtMenu.setIcon(QIcon("./static/images/menu.png"))
        self.btnQtMenu.setObjectName("btnQtMenu")
        # endregion
        # region Creating minimize button
        self.btnMinimize = QPushButton(self.Form)
        self.btnMinimize.setMaximumSize(QSize(15, 15))
        self.btnMinimize.setStyleSheet(StyleSheethHelper.btnMinimizeStyleSheet_normal)
        self.btnMinimize.setText("")
        self.btnMinimize.setObjectName("btnMinimize")
        # endregion
        # region Creating maximize button
        self.btnMaximize = QPushButton(self.Form)
        self.btnMaximize.setMinimumSize(QSize(15, 15))
        self.btnMaximize.setMaximumSize(QSize(15, 15))
        self.btnMaximize.setStyleSheet(StyleSheethHelper.btnMaximizeStyleSheet_normal)
        self.btnMaximize.setIcon(QIcon("./static/images/maximize.png"))
        self.btnMaximize.setIconSize(QSize(15, 15))
        self.btnMinimize.setIcon(QIcon("./static/images/minus.png"))
        self.btnMinimize.setIconSize(QSize(15, 15))
        self.btnMaximize.setText("")
        self.btnMaximize.setObjectName("btnMaximize")
        # endregion
        # region Creating close button
        self.btnClose = QPushButton(self.Form)
        self.btnClose.setMinimumSize(QSize(15, 15))
        self.btnClose.setMaximumSize(QSize(15, 15))
        self.btnClose.setAccessibleDescription("")
        self.btnClose.setStyleSheet(StyleSheethHelper.btnCloseStyleSheet_normal)
        self.btnClose.setText("")
        self.btnClose.setIcon(QIcon("./static/images/close.png"))
        self.btnClose.setIconSize(QSize(15, 15))
        self.btnClose.setObjectName("btnClose")
        # endregion
        # region Creating search line
        # region Creating search text field
        self.searchField =  QLineEdit(self.Form)
        self.searchField.setFixedHeight(30)
        self.searchField.setFont(fontMontserrat)
        self.searchField.setStyleSheet(StyleSheethHelper.searchFieldStyleSheet_normal)
        # endregion
        # region Create search button
        self.searchButton = QPushButton(self.Form)
        self.searchButton.resize(30, 30)
        self.searchButton.setStyleSheet(StyleSheethHelper.searchButtonStyleSheet_normal)
        self.searchButton.setIcon(QIcon("./static/images/search.png"))
        self.searchButton.setFixedSize(QSize(30, 30))
        # endregion
        # endregion
        # endregion

        # region Creating Web View
        self.webview = QWebEngineView(self.Form)
        self.webview.setObjectName("webview")
        self.webview.show()
        # endregion

        # region Adding items to layouts
        self.backgroundFormLayout.addWidget(self.Form, 0, 0, 1, 1)
        self.formLayout.addLayout(self.headerLayout, 0, 0, 1, 1)
        self.formLayout.addLayout(self.searchLayout, 1, 0, 1, 1)
        self.formLayout.addWidget(self.webview, 2, 0, 1, 1)
        self.headerLayout.addWidget(self.btnQtMenu)
        self.headerLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.headerLayout.addLayout(self.closeMinMaxLayout)
        self.closeMinMaxLayout.addWidget(self.btnMinimize)
        self.closeMinMaxLayout.addWidget(self.btnMaximize)
        self.closeMinMaxLayout.addWidget(self.btnClose)
        self.searchLayout.addWidget(self.searchField)
        self.searchLayout.addWidget(self.searchButton)
        # endregion

        self.retranslateUi(BackgroundForm)
        QMetaObject.connectSlotsByName(BackgroundForm)

    def retranslateUi(self, BackgroundForm):
        _translate = QCoreApplication.translate
        BackgroundForm.setWindowTitle(_translate("BackgroundForm", "QtBrowser"))
        self.btnQtMenu.setText(_translate("BackgroundForm", "QtBrowser"))
