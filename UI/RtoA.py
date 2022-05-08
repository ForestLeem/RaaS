# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RtoA.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import PyQt5.sip
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

    def setup_UI(self, MainWindow, ResEditor, RtoAUI):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 620)

        self.MainWindow = MainWindow
        self.ResEditor = ResEditor

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_R = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_R.setWidgetResizable(True)
        self.scrollArea_R.setObjectName("scrollArea_R")
        self.scrollAreaWidgetContents_R = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_R.setGeometry(QtCore.QRect(0, 0, 470, 570))
        self.scrollAreaWidgetContents_R.setObjectName("scrollAreaWidgetContents_R")
        self.txt_Res = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_R)
        self.txt_Res.setGeometry(QtCore.QRect(0, 0, 411, 561))
        self.txt_Res.setObjectName("txt_Res")
        self.btn_R2A = QtWidgets.QPushButton(self.scrollAreaWidgetContents_R)
        self.btn_R2A.setGeometry(QtCore.QRect(410, 220, 65, 81))
        self.btn_R2A.setObjectName("btn_R2A")
        self.scrollArea_R.setWidget(self.scrollAreaWidgetContents_R)
        self.gridLayout.addWidget(self.scrollArea_R, 0, 0, 1, 1)
        self.scrollArea_A = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_A.setWidgetResizable(True)
        self.scrollArea_A.setObjectName("scrollArea_A")
        self.scrollAreaWidgetContents_A = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_A.setGeometry(QtCore.QRect(0, 0, 470, 570))
        self.scrollAreaWidgetContents_A.setObjectName("scrollAreaWidgetContents_A")
        self.txt_Asset = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_A)
        self.txt_Asset.setGeometry(QtCore.QRect(0, 0, 471, 521))
        self.txt_Asset.setObjectName("txt_Asset")
        self.btn_previous = QtWidgets.QPushButton(self.scrollAreaWidgetContents_A)
        self.btn_previous.setGeometry(QtCore.QRect(60, 520, 101, 31))
        self.btn_previous.setObjectName("btn_previous")
        self.btn_next = QtWidgets.QPushButton(self.scrollAreaWidgetContents_A)
        self.btn_next.setGeometry(QtCore.QRect(210, 520, 101, 31))
        self.btn_next.setObjectName("btn_next")
        self.page = QtWidgets.QLabel(self.scrollAreaWidgetContents_A)
        self.page.setGeometry(QtCore.QRect(160, 520, 51, 31))
        self.page.setObjectName("page")
        self.btn_sava = QtWidgets.QPushButton(self.scrollAreaWidgetContents_A)
        self.btn_sava.setGeometry(QtCore.QRect(370, 520, 101, 31))
        self.btn_sava.setObjectName("btn_sava")
        self.scrollArea_A.setWidget(self.scrollAreaWidgetContents_A)
        self.gridLayout.addWidget(self.scrollArea_A, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 18))
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

        self.actionResEditor.setCheckable(True)
        self.actionA_S_projection.setCheckable(True)
        self.actionR_A_projection.setCheckable(True)
        self.actionR_A_projection.setChecked(True)                      # default
        self.bind_function()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "R-A projection"))
        self.btn_R2A.setText(_translate("MainWindow", "Res \n"
"to \n"
" Asset"))
        self.btn_previous.setText(_translate("MainWindow", "<previous asset"))
        self.btn_next.setText(_translate("MainWindow", "<next asset"))
        self.page.setText(_translate("MainWindow", "  0/0"))
        self.btn_sava.setText(_translate("MainWindow", "Save"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.actionClear.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionResEditor.setText(_translate("MainWindow", "ResEditor"))
        self.actionR_A_projection.setText(_translate("MainWindow", "R-A projection"))
        self.actionA_S_projection.setText(_translate("MainWindow", "A-S projection"))

    def bind_function(self):
        self.btn_R2A.clicked.connect(self.ResToAsset)
        self.actionR_A_projection.triggered.connect(self.change_to_R_A_UI)
        self.actionResEditor.triggered.connect(self.change_to_ResEditor_UI)
        self.actionA_S_projection.triggered.connect(self.change_to_A_S_UI)
        self.actionClear.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_resource)

    # menubar function
    def change_to_R_A_UI(self):
        self.actionR_A_projection.setChecked(True)

    def change_to_ResEditor_UI(self):
        reply = QtWidgets.QMessageBox.question(None, "Warning", "Are you sure to change to MODE ResEditor?\n "
                                                                "(make sure you have save your file!)",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.ResEditor.setup_UI(self.MainWindow, self.ResEditor, self)
        else:
            self.actionResEditor.setChecked(False)

    def change_to_A_S_UI(self):
        reply = QtWidgets.QMessageBox.question(None, "Warning", "Are you sure to change to MODE ResEditor?\n "
                                                                "(make sure you have save your file!)",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.ResEditor.setup_UI(self.MainWindow, self.ResEditor, self)
        else:
            self.actionA_S_projection.setChecked(False)

    def new_file(self):
        reply = QtWidgets.QMessageBox.question(None, "new file",
                                                     "Do you want to start new R-A projection \n"
                                                     "(Please make sure you have saved your file.)",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            tmpMainWindow = self.MainWindow
            tmpRes = self.ResEditor
            PyQt5.sip.delete(self.centralwidget)
            self.setup_UI(tmpMainWindow, tmpRes, self)
        else:
            return

    def open_resource(self):
        tmp = QtWidgets.QFileDialog.getOpenFileName(None, "open", "/", "json(*.json)")
        print(tmp)

    # menubar function

    def ResToAsset(self):
        return






if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_UI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())