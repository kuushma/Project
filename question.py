# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_Prompt(object):
    def setupUi(self, Prompt):
        Prompt.setObjectName("Prompt")
        Prompt.setFixedSize(519, 207)
        self.centralwidget = QtWidgets.QWidget(Prompt)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(495, 138))
        self.textBrowser.setMaximumSize(QtCore.QSize(495, 138))
        self.textBrowser.setBaseSize(QtCore.QSize(495, 138))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        Prompt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Prompt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 24))
        self.menubar.setObjectName("menubar")
        Prompt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Prompt)
        self.statusbar.setObjectName("statusbar")
        Prompt.setStatusBar(self.statusbar)

        self.retranslateUi(Prompt)
        QtCore.QMetaObject.connectSlotsByName(Prompt)

    def retranslateUi(self, Prompt):
        _translate = QtCore.QCoreApplication.translate
        Prompt.setWindowTitle(_translate("Prompt", "MainWindow"))
        self.textBrowser.setHtml(_translate("Prompt", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Нажмите на нужную </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">вам кнопку!</span></p></body></html>"))


class Qestion(QMainWindow, Ui_Prompt):
    def __init__(self):
        super().__init__()
        self.setupUi(self)