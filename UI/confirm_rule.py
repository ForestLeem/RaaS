# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comfirm_rule.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtCore.QObject):
    signal1 = QtCore.pyqtSignal(list)

    def __init__(self, Dialog):
        super(Ui_Dialog, self).__init__(Dialog)
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 240)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 451, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 441, 41))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(330, 160, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 70, 301, 121))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "confirm rule"))
        self.label.setText(_translate("Dialog", "Please tell us the following rule belong to which class. \n"
"      Permission, Prohibition or Obligation?"))
        self.comboBox.setItemText(0, _translate("Dialog", "permission"))
        self.comboBox.setItemText(1, _translate("Dialog", "prohibition"))
        self.comboBox.setItemText(2, _translate("Dialog", "obligation"))

    def get_result(self, result):
        if result:
            return [self.comboBox.currentText(), self.textEdit.toPlainText()]
