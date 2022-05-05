# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'R-A.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(0, 40, 481, 541))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 40, 471, 541))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuResEditor = QtWidgets.QMenu(self.menubar)
        self.menuResEditor.setObjectName("menuResEditor")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionR_A_projection = QtWidgets.QAction(MainWindow)
        self.actionR_A_projection.setObjectName("actionR_A_projection")
        self.actionA_S_projection = QtWidgets.QAction(MainWindow)
        self.actionA_S_projection.setObjectName("actionA_S_projection")
        self.actionResEditor = QtWidgets.QAction(MainWindow)
        self.actionResEditor.setObjectName("actionResEditor")
        self.menuResEditor.addAction(self.actionResEditor)
        self.menuResEditor.addAction(self.actionR_A_projection)
        self.menuResEditor.addAction(self.actionA_S_projection)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuResEditor.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "R-A projection"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuResEditor.setTitle(_translate("MainWindow", "Mode"))
        self.actionR_A_projection.setText(_translate("MainWindow", "R-A projection"))
        self.actionA_S_projection.setText(_translate("MainWindow", "A-S projection"))
        self.actionResEditor.setText(_translate("MainWindow", "ResEditor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
