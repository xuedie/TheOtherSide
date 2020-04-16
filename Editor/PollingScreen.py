import datetime
import json
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
# class for pollingScreen UI
from PyQt5.QtWidgets import QMessageBox


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class PollingScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def is_file_empty(self, file_path):
        """ Check if file is empty by confirming if its size is 0 bytes"""
        # Check if file exist and it is empty
        return os.path.exists(file_path) and os.stat(file_path).st_size == 0

    def readFromJsonFile(self):
        for filename in os.listdir(resource_path('TemplateJsonInstance/SimplePollingInstance/')):
            with open(os.path.join(resource_path('TemplateJsonInstance/SimplePollingInstance/'), filename), 'r') as json_file:
                data = json.load(json_file)
                self.listWidget.addItem(data['name'])

    def save(self):
        # check if string is empty
        if self.Question.toPlainText() != "" and self.Option1.toPlainText() != "" and self.Option2.toPlainText() != "" and self.Option3.toPlainText() != "" and self.Option4.toPlainText() != "" and self.EntryName.toPlainText() != "":

            if self.listWidget.count() == 0:
                PollingSystemRecord = {
                    "name": self.EntryName.toPlainText(),
                    "type": "simplePolling",
                    "question": self.Question.toPlainText(),
                    "createdOn": datetime.datetime.now().timestamp(),
                    "lastUpdated": datetime.datetime.now().timestamp(),
                    "options": [
                        self.Option1.toPlainText(),
                        self.Option2.toPlainText(),
                        self.Option3.toPlainText(),
                        self.Option4.toPlainText()
                    ]

                }

                file = open(os.path.join(resource_path('TemplateJsonInstance/SimplePollingInstance/'), self.EntryName.toPlainText() + ".json"),
                            'w')
                with file as json_file:
                    json.dump(PollingSystemRecord, json_file)
                    self.listWidget.addItem(self.EntryName.toPlainText())

            # check if this list item has already been added:  remove duplicates
            else:

                items = self.listWidget.findItems(self.EntryName.toPlainText(), Qt.MatchFixedString)
            if items.__len__() == 0:
                PollingSystemRecord = {
                    "name": self.EntryName.toPlainText(),
                    "type": "simplePolling",
                    "question": self.Question.toPlainText(),
                    "createdOn": datetime.datetime.now().timestamp(),
                    "lastUpdated": datetime.datetime.now().timestamp(),
                    "options": [
                        self.Option1.toPlainText(),
                        self.Option2.toPlainText(),
                        self.Option3.toPlainText(),
                        self.Option4.toPlainText()
                    ]

                }

                file = open(os.path.join(resource_path('TemplateJsonInstance/SimplePollingInstance/'), self.EntryName.toPlainText() + ".json"),
                            'w')
                with file as json_file:
                    json.dump(PollingSystemRecord, json_file)
                    self.listWidget.addItem(self.EntryName.toPlainText())

            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("The Entry Name " + self.EntryName.toPlainText() + " already exists!")
                msgBox.setWindowTitle("Error")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                x = msgBox.exec_()

        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Fields cannot be left blank")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1576, 964)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path('Images/The Other Side_logo.png')), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 60, 1291, 920))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(resource_path('Images/PollingScreen.png')))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setIndent(21)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.Question = QtWidgets.QTextBrowser(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(1070, 260, 371, 95))
        self.Question.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Question.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Question.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Question.setFont(font)
        self.Question.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Question.setObjectName("Question")
        self.Option1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option1.setGeometry(QtCore.QRect(700, 540, 151, 55))
        self.Option1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option1.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option1.setFont(font)
        self.Option1.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option1.setObjectName("Option1")
        self.Option2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option2.setGeometry(QtCore.QRect(840, 780, 201, 65))
        self.Option2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option2.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option2.setFont(font)
        self.Option2.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option2.setObjectName("Option2")
        self.Option3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option3.setGeometry(QtCore.QRect(1340, 680, 151, 65))
        self.Option3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option3.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option3.setFont(font)
        self.Option3.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option3.setObjectName("Option3")
        self.Option4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option4.setGeometry(QtCore.QRect(310, 600, 201, 71))
        self.Option4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option4.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option4.setFont(font)
        self.Option4.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option4.setObjectName("Option4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1430, 10, 121, 41))
        self.pushButton.setObjectName("pushButton")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 110, 281, 851))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignVCenter)
        self.listWidget.setObjectName("listWidget")
        # this function reads the previous records in the json file
        self.readFromJsonFile()

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 860, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1290, 10, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 10, 41, 41))
        self.commandLinkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path('Images/directional-chevron-back-512.ico')), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(35, 35))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.EntryName = QtWidgets.QTextBrowser(self.centralwidget)
        self.EntryName.setGeometry(QtCore.QRect(240, 10, 961, 41))
        self.EntryName.setAutoFillBackground(True)
        self.EntryName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EntryName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EntryName.setLineWidth(2)
        self.EntryName.setObjectName("Entry Name")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.EntryName.setFont(font)

        self.EntryName.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.EntryName.setReadOnly(False)
        self.EntryName.setOverwriteMode(True)
        self.EntryName.setObjectName("textEdit")
        self.commandLinkButton.raise_()
        self.label.raise_()
        self.Question.raise_()
        self.Option1.raise_()
        self.Option2.raise_()
        self.Option3.raise_()
        self.Option4.raise_()
        self.pushButton.raise_()
        self.listWidget.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.line.raise_()
        self.EntryName.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.save)
        self.pushButton_3.clicked.connect(self.Question.clear)
        self.pushButton_3.clicked.connect(self.Option1.clear)
        self.pushButton_3.clicked.connect(self.Option2.clear)
        self.pushButton_3.clicked.connect(self.Option3.clear)
        self.pushButton_3.clicked.connect(self.Option4.clear)
        self.pushButton_2.clicked.connect(self.deleteItem)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.populateTextForEdit)
        # self.commandLinkButton.clicked.connect()  #back functionality
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def deleteItem(self):
        items = self.listWidget.selectedItems()
        for item in items:
            # delete the file
            for fileName in os.listdir(resource_path('TemplateJsonInstance/SimplePollingInstance/')):
                if fileName == self.listWidget.currentItem().text() + ".json":
                    os.remove( os.path.join(resource_path('TemplateJsonInstance/SimplePollingInstance/'), fileName))

            self.listWidget.takeItem(self.listWidget.row(item))

            # delete confirmation
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Field Deleted")
            msgBox.setWindowTitle("Success")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()

    def populateTextForEdit(self):
        text = self.listWidget.currentItem().text()
        self.EntryName.setPlainText(text)
        # find the file corresponding to the entry name
        for fileName in os.listdir(resource_path('TemplateJsonInstance/SimplePollingInstance/')):
            # get the record from json for edit
            if fileName == text + ".json":
                with open(os.path.join(resource_path('TemplateJsonInstance/SimplePollingInstance/'), fileName), 'r') as json_file:
                    data = json.load(json_file)
                    self.Question.setPlainText(data['question'])
                    self.Option1.setPlainText(data['options'][0])
                    self.Option2.setPlainText(data['options'][1])
                    self.Option3.setPlainText(data['options'][2])
                    self.Option4.setPlainText(data['options'][3])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.Question.setPlaceholderText(_translate("MainWindow", "Question"))
        self.Option1.setPlaceholderText(_translate("MainWindow", "Option1"))
        self.Option2.setPlaceholderText(_translate("MainWindow", "Option2"))
        self.Option3.setPlaceholderText(_translate("MainWindow", "Option3"))
        self.Option4.setPlaceholderText(_translate("MainWindow", "Option4"))
        self.EntryName.setPlaceholderText(_translate("MainWindow", "Entry Name"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.label_2.setText(_translate("MainWindow", "Content List"))


