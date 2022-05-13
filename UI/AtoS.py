# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RtoA.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.sip
import json
from AssetToService import AaaS
from ODRL import Party
from ODRL import Asset
from ODRL import Action
from ODRL import Constraint
from ODRL import Policy
from ODRL import Rule
from Resource import Provider
from Resource import Resource as Res
from Resource import Interface
from Resource import Func_Char
from Resource import Non_Func_Char
from Resource import Operation


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

    def setup_UI(self, MainWindow, ResEditor_UI, RtoA_UI, AtoS_UI):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 620)

        self.MainWindow = MainWindow
        self.ResEditor_UI = ResEditor_UI
        self.RtoA_UI = RtoA_UI

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_A = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_A.setWidgetResizable(True)
        self.scrollArea_A.setObjectName("scrollArea_A")
        self.scrollAreaWidgetContents_A = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_A.setGeometry(QtCore.QRect(0, 0, 480, 570))
        self.scrollAreaWidgetContents_A.setObjectName("scrollAreaWidgetContents_A")
        self.txt_Asset = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_A)
        self.txt_Asset.setGeometry(QtCore.QRect(0, 20, 411, 541))
        self.txt_Asset.setObjectName("txt_Asset")
        self.btn_A2S = QtWidgets.QPushButton(self.scrollAreaWidgetContents_A)
        self.btn_A2S.setGeometry(QtCore.QRect(410, 220, 61, 81))
        self.btn_A2S.setObjectName("btn_A2S")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_A)
        self.label.setGeometry(QtCore.QRect(0, 0, 411, 16))
        self.label.setObjectName("label")
        self.scrollArea_A.setWidget(self.scrollAreaWidgetContents_A)
        self.gridLayout.addWidget(self.scrollArea_A, 0, 0, 1, 1)
        self.scrollArea_S = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_S.setWidgetResizable(True)
        self.scrollArea_S.setObjectName("scrollArea_S")
        self.scrollAreaWidgetContents_S = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_S.setGeometry(QtCore.QRect(0, 0, 480, 570))
        self.scrollAreaWidgetContents_S.setObjectName("scrollAreaWidgetContents_S")
        self.txt_Service = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_S)
        self.txt_Service.setGeometry(QtCore.QRect(0, 20, 471, 501))
        self.txt_Service.setObjectName("txt_Service")
        self.btn_sava = QtWidgets.QPushButton(self.scrollAreaWidgetContents_S)
        self.btn_sava.setGeometry(QtCore.QRect(370, 520, 101, 31))
        self.btn_sava.setObjectName("btn_sava")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_S)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 411, 16))
        self.label_2.setObjectName("label_2")
        self.scrollArea_S.setWidget(self.scrollAreaWidgetContents_S)
        self.gridLayout.addWidget(self.scrollArea_S, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionResEditor = QtWidgets.QAction(MainWindow)
        self.actionResEditor.setObjectName("actionResEditor")
        self.actionR_A_projection = QtWidgets.QAction(MainWindow)
        self.actionR_A_projection.setObjectName("actionR_A_projection")
        self.actionA_S_projection = QtWidgets.QAction(MainWindow)
        self.actionA_S_projection.setObjectName("actionA_S_projection")
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionOpen)
        self.menuMode.addAction(self.actionResEditor)
        self.menuMode.addAction(self.actionR_A_projection)
        self.menuMode.addAction(self.actionA_S_projection)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.actionA_S_projection.setCheckable(True)
        self.actionA_S_projection.setChecked(True)
        self.retranslateUi(MainWindow)
        self.bind_function()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "A-S projection"))
        self.btn_A2S.setText(_translate("MainWindow", "Asset \n"
"to \n"
" Service"))
        self.label.setText(_translate("MainWindow", "Asset"))
        self.btn_sava.setText(_translate("MainWindow", "Save"))
        self.label_2.setText(_translate("MainWindow", "Service"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.actionClear.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionResEditor.setText(_translate("MainWindow", "ResEditor"))
        self.actionR_A_projection.setText(_translate("MainWindow", "R-A projection"))
        self.actionA_S_projection.setText(_translate("MainWindow", "A-S projection"))

    def bind_function(self):
        self.actionResEditor.triggered.connect(self.change_to_ResEditor_UI)
        self.actionR_A_projection.triggered.connect(self.change_to_R_A_UI)
        self.actionA_S_projection.triggered.connect(self.change_to_A_S_UI)
        self.actionClear.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_asset)
        self.btn_A2S.clicked.connect(self.Asset_To_Service)

    # menubar function BEGIN
    def change_to_A_S_UI(self):
        self.actionA_S_projection.setChecked(True)

    def change_to_ResEditor_UI(self):
        reply = QtWidgets.QMessageBox.question(None, "Warning", "Are you sure to change to MODE ResEditor?\n "
                                                                "(make sure you have save your file!)",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            PyQt5.sip.delete(self.centralwidget)
            self.ResEditor_UI.setup_UI(self.MainWindow, self.ResEditor_UI, self.RtoA_UI, self)
        else:
            pass

    def change_to_R_A_UI(self):
        reply = QtWidgets.QMessageBox.question(None, "Warning", "Are you sure to change to MODE R-A projection?\n "
                                                                "(make sure you have save your file!)",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            PyQt5.sip.delete(self.centralwidget)
            self.RtoA_UI.setup_UI(self.MainWindow, self.ResEditor_UI, self.RtoA_UI, self)
        else:
            pass

    def new_file(self):
        reply = QtWidgets.QMessageBox.question(None, "new file",
                                                     "Do you want to start new A-S projection \n"
                                                     "(Please make sure you have saved your file.)",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            tmpMainWindow = self.MainWindow
            PyQt5.sip.delete(self.centralwidget)
            self.setup_UI(tmpMainWindow, self.ResEditor_UI, self.RtoA_UI, self)
        else:
            return

    def open_asset(self):
        openfile, ok = QtWidgets.QFileDialog.getOpenFileName(None, "open", "/", "json(*.json)")

        try:
            with open(openfile, "r") as f:
                tmp_json = json.load(f)
                tmp_str = json.dumps(tmp_json, indent=1)
                self.txt_Asset.setText(tmp_str)
        except Exception as e:
            print(e)

    def Asset_To_Service(self):
        #   Asset to Service
        if self.txt_Asset.toPlainText() == "":
            return
        try:
            tmp_dict_data = json.loads(self.txt_Asset.toPlainText())
            tmp_policy = Policy.Policy("Agreement", "tmp")
            tmp_policy.to_policy(tmp_dict_data)
            tmp_service = AaaS.Asset2Service(tmp_policy)
            tmp_str = ""
            for i in tmp_service:
                tmp_str += json.dumps(i.to_dict(), indent=1)
                tmp_str += "\n"
            self.txt_Service.setText(tmp_str)
        except Exception as e:
            print(e)


    # menubar function END

# if __name__ == "__main__":
#     import sys
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow, 1,1,1)
#     MainWindow.show()
#     sys.exit(app.exec_())