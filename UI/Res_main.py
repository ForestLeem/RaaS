# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Res.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import PyQt5
import PyQt5.sip
from PyQt5 import QtCore, QtGui, QtWidgets
from UI import FnUI
from UI import InterfaceUI
from UI import dialog_fnchar
from UI import dialog_interface
from UI import RtoA
from UI import AtoS
from Resource import Resource as Res
from Resource import Provider as Provider
from Resource import Func_Char as Func_Char
from Resource import Interface as Interface
from Resource import Operation as Operation
import json


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

    def setup_UI(self, MainWindow, ResEditor_UI, RtoA_UI, AtoS_UI):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 620)

        self.MainWindow = MainWindow

        self.RtoA_UI = RtoA_UI
        self.AtoS_UI = AtoS_UI

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 451, 581))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 436, 566))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(10, 0, 401, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_resource = QtWidgets.QLabel(self.frame)
        self.label_resource.setGeometry(QtCore.QRect(0, 30, 81, 21))
        self.label_resource.setObjectName("label_resource")
        self.lineEdit_resource = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_resource.setGeometry(QtCore.QRect(80, 30, 311, 21))
        self.lineEdit_resource.setObjectName("lineEdit_resource")
        self.label_provider = QtWidgets.QLabel(self.frame)
        self.label_provider.setGeometry(QtCore.QRect(0, 50, 81, 21))
        self.label_provider.setObjectName("label_provider")
        self.lineEdit_provider = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_provider.setGeometry(QtCore.QRect(80, 50, 311, 21))
        self.lineEdit_provider.setObjectName("lineEdit_provider")
        self.label_context = QtWidgets.QLabel(self.frame)
        self.label_context.setGeometry(QtCore.QRect(0, 10, 371, 21))
        self.label_context.setObjectName("label_context")
        self.label_fnchar = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_fnchar.setGeometry(QtCore.QRect(10, 80, 261, 21))
        self.label_fnchar.setStyleSheet("font: 12pt \"Arial\";")
        self.label_fnchar.setObjectName("label_fnchar")
        self.frame_fn_char = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_fn_char.setGeometry(QtCore.QRect(30, 100, 381, 21))
        self.frame_fn_char.setStyleSheet("background-color:rgb(231, 255, 248)")
        self.frame_fn_char.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_fn_char.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fn_char.setObjectName("frame_fn_char")
        self.label_interface = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_interface.setGeometry(QtCore.QRect(10, 130, 211, 21))
        self.label_interface.setStyleSheet("font: 12pt \"Arial\";")
        self.label_interface.setObjectName("label_interface")
        self.btn_add_fnchar = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_add_fnchar.setGeometry(QtCore.QRect(380, 80, 31, 21))
        self.btn_add_fnchar.setObjectName("btn_add_fnchar")
        self.btn_add_interface = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_add_interface.setGeometry(QtCore.QRect(380, 130, 31, 21))
        self.btn_add_interface.setObjectName("btn_add_interface")
        self.frame_interface = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_interface.setGeometry(QtCore.QRect(30, 150, 381, 21))
        self.frame_interface.setStyleSheet("background-color:rgb(231, 255, 248)")
        self.frame_interface.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_interface.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_interface.setObjectName("frame_interface")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        # menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionResource = QtWidgets.QAction(MainWindow)
        self.actionResource.setObjectName("actionResource")
        self.actionResource.setCheckable(True)
        self.actionResource.setChecked(True)                 # default
        self.actionResToAsset = QtWidgets.QAction(MainWindow)
        self.actionResToAsset.setObjectName("actionResToAsset")
        self.actionResToAsset.setCheckable(True)
        self.actionAssetToService = QtWidgets.QAction(MainWindow)
        self.actionAssetToService.setObjectName("actionAssetToService")
        self.actionAssetToService.setCheckable(True)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuMode.addAction(self.actionResource)
        self.menuMode.addAction(self.actionResToAsset)
        self.menuMode.addAction(self.actionAssetToService)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        # menu bar

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.retranslateUi(MainWindow)
        self.bind_function()

        self.fnchar_frame_height = 21
        self.fnchar_UI_height = 81
        self.fnchar_list = []

        self.interface_frame_h = 21
        self.interface_UI_height = 161
        self.interface_list = []

        self.location_frame_fnchar = 100
        self.location_label_btn_fnchar = 80
        self.location_frame_interface = 150
        self.location_label_btn_interface = 130

        self.resource_class = Res.Resource()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ResEditor"))
        self.label_resource.setText(_translate("MainWindow", "Resource_uid:"))
        self.label_provider.setText(_translate("MainWindow", "Provider_uid:"))
        self.label_context.setText(_translate("MainWindow", "@context    http://www.w3.org/ns/resource.jsonld"))
        self.label_fnchar.setText(_translate("MainWindow", "* Functional_Characteristic:"))
        self.label_interface.setText(_translate("MainWindow", "* Interface :"))
        self.btn_add_fnchar.setText(_translate("MainWindow", "add"))
        self.btn_add_interface.setText(_translate("MainWindow", "add"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

        self.actionResource.setText(_translate("MainWindow", "ResEditor"))
        self.actionResToAsset.setText(_translate("MainWindow", "R-A projection"))
        self.actionAssetToService.setText(_translate("MainWindow", "A-S projection"))


    def bind_function(self):
        self.btn_add_fnchar.clicked.connect(self.add_fnchar)
        self.btn_add_interface.clicked.connect(self.add_interface)
        self.actionNew.triggered.connect(self.new_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionResource.triggered.connect(self.change_to_ResEditor_UI)
        self.actionResToAsset.triggered.connect(self.change_to_R_A_UI)
        self.actionAssetToService.triggered.connect(self.change_to_A_S_UI)

    def add_fnchar(self):
        dialog1 = QtWidgets.QDialog()
        dialog1.setWindowModality(QtCore.Qt.ApplicationModal)
        fnchar_dia = dialog_fnchar.Ui_Dialog(dialog1)
        fnchar_dia.signal1.connect(self.process_add_fnchar)
        dialog1.exec_()

    def add_interface(self):
        dialog1 = QtWidgets.QDialog()
        dialog1.setWindowModality(QtCore.Qt.ApplicationModal)
        interface_dia = dialog_interface.Ui_Dialog(dialog1)
        interface_dia.signal1.connect(self.process_add_interface)
        dialog1.exec_()

    def process_add_fnchar(self, list_data):
        if list_data[0]:   # ok
            # add new fnchar
            f_type = list_data[1]
            description = list_data[2]

            # check f_type
            for tmp_fnchar in self.fnchar_list:
                if tmp_fnchar.get_f_type() == f_type:
                    msg_box = QtWidgets.QMessageBox.information(None, "Warning", "Functional_Characteristic f_type:" +
                                                                f_type + " exist. Don't add again.")
                    return
            new_fnchar_UI = FnUI.FnUI(self.frame_fn_char, self.fnchar_frame_height, f_type, description)
            new_fnchar_UI.signal_change.connect(self.re_arrange_UI_signal)
            new_fnchar_UI.signal_change.connect(self.process_delete)
            self.fnchar_list.append(new_fnchar_UI)
            self.re_arrange_UI()
            self.generate_resource(["generate"])

        else:
            # don't  add
            return

    def process_add_interface(self, list_data):
        if list_data[0]:      # ok
            # add new interface
            uid = list_data[1]
            description = list_data[2]

            # check uid
            for tmp_interface in self.interface_list:
                if tmp_interface.get_uid() == uid:
                    msg_box = QtWidgets.QMessageBox.information(None, "Warning", "Interface uid:" + uid +
                                                                " exist. Don't add again.")
                    return

            new_interface_UI = InterfaceUI.InterfaceUI(self.frame_interface, self.interface_frame_h, uid, description)
            new_interface_UI.signal_change.connect(self.re_arrange_UI_signal)
            new_interface_UI.signal_change.connect(self.process_delete)
            self.interface_list.append(new_interface_UI)
            self.re_arrange_UI()
            self.generate_resource(["generate"])

            # self.interface_frame_h = self.interface_frame_h + self.interface_UI_height
            # self.frame_interface.setGeometry(QtCore.QRect(30, self.interface_frame_location, 381, self.interface_frame_h))
            # self.scrollAreaWidgetContents.setMinimumSize(450, self.interface_frame_location + self.interface_frame_h)
        else:
            return

    def re_arrange_UI(self):
        frame_fnchar_height = 21

        # arrange fnchar_UI
        for tmp in self.fnchar_list:
            tmp.change_location(frame_fnchar_height)
            frame_fnchar_height += tmp.get_UI_height()
        self.frame_fn_char.setGeometry(QtCore.QRect
                                       (30, self.location_frame_fnchar, 381, frame_fnchar_height))
        self.label_interface.setGeometry(QtCore.QRect
                                         (10, self.location_label_btn_interface + frame_fnchar_height - 21, 211, 21))
        self.btn_add_interface.setGeometry(QtCore.QRect
                                           (380, self.location_label_btn_interface + frame_fnchar_height - 21, 31, 21))

        # arrange interface_UI
        frame_interface_height = 21
        for tmp in self.interface_list:
            tmp.change_location(frame_interface_height)
            frame_interface_height += tmp.get_UI_height()

        self.frame_interface.setGeometry(QtCore.QRect
                                         (30, self.location_frame_interface + frame_fnchar_height - 21
                                          , 381, frame_interface_height))
        self.scrollAreaWidgetContents.setMinimumSize(450, self.location_frame_interface + frame_fnchar_height
                                                     + self.frame_interface.height())
        self.generate_resource(["generate"])

    def re_arrange_UI_signal(self, data_list):
        _type = data_list[0]
        _object = data_list[1]
        if _type == "show_hide":
            frame_fnchar_height = 21
            for tmp in self.fnchar_list:
                tmp.change_location(frame_fnchar_height)
                frame_fnchar_height += tmp.get_UI_height()
            self.frame_fn_char.setGeometry(QtCore.QRect(30, self.location_frame_fnchar, 381, frame_fnchar_height))
            self.label_interface.setGeometry(QtCore.QRect
                                             (10, self.location_label_btn_interface + frame_fnchar_height - 21, 211, 21))
            self.btn_add_interface.setGeometry(QtCore.QRect
                                               (380, self.location_label_btn_interface + frame_fnchar_height - 21, 31, 21))
            tmp_height = self.frame_interface.height()
            self.frame_interface.setGeometry(QtCore.QRect
                                             (30, self.location_frame_interface + frame_fnchar_height - 21, 381, tmp_height))
            self.scrollAreaWidgetContents.setMinimumSize(450, self.location_frame_interface + frame_fnchar_height
                                                         + self.frame_interface.height())
        self.generate_resource(["generate"])

    def process_delete(self, data_list):
        # receive a delete signal, to delete fnchar or interface
        _type = data_list[0]
        _object = data_list[1]
        if _type == "del_fnchar":
            for i in range(0, len(self.fnchar_list)):
                if _object == self.fnchar_list[i]:
                    self.fnchar_list.pop(i)
                    break

        elif _type == "del_interface":
            for i in range(0, len(self.interface_list)):
                if _object == self.interface_list[i]:
                    self.interface_list.pop(i)
                    break
        self.re_arrange_UI()

    def generate_resource(self, data_list):

        # new resource class
        tmp_res = Res.Resource()
        tmp_res.uid = self.lineEdit_resource.text()

        # add provider
        tmp_provider = Provider.Provider()
        tmp_provider.uid = self.lineEdit_provider.text()
        tmp_res.provider = tmp_provider

        # add functional characteristic
        for tmp in self.fnchar_list:
            tmp_fn_char = tmp.get_FnChar_class()
            tmp_res.add_FnChar(tmp_fn_char)

        # add interface
        for tmp in self.interface_list:
            tmp_interface = tmp.get_interface_class()
            tmp_res.add_interface(tmp_interface)

        res_str = json.dumps(tmp_res.to_dict(), indent=2)
        self.textEdit.setText(res_str)
        return

    #  menu bar function begin
    def open_file(self):
        openfile, ok = QtWidgets.QFileDialog.getOpenFileName(None, "open", "/", "json(*.json)")

        try:
            with open(openfile, "r") as f:
                tmp_res = json.load(f)
                self.lineEdit_resource.setText(tmp_res["uid"])
                self.lineEdit_provider.setText(tmp_res["provider"])

                # add Functional_Characteristic
                tmp_fnchar_list = tmp_res["Functional_Characteristic"]
                for tmp_fnchar in tmp_fnchar_list:
                    data_list = [1, tmp_fnchar["f_type"]]
                    if "description" in tmp_fnchar.keys():
                        data_list.append(tmp_fnchar["description"])
                    else:
                        data_list.append("")
                    self.process_add_fnchar(data_list)

                # add interface
                tmp_interface_list = tmp_res["interface"]
                i = 0
                for tmp_interface in tmp_interface_list:
                    data_list = [1, tmp_interface["uid"]]
                    if "description" in tmp_interface.keys():
                        data_list.append(tmp_interface["description"])
                    else:
                        data_list.append("")
                    self.process_add_interface(data_list)
                    interface_UI = self.interface_list[i]
                    i += 1

                    # add operation
                    j = 0
                    for tmp_operation in tmp_interface["operation"]:
                        data_list = [1, tmp_operation["uid"]]
                        if "description" in tmp_operation.keys():
                            data_list.append(tmp_operation["description"])
                        else:
                            data_list.append("")
                        interface_UI.process_add_op(data_list)
                        op_UI = interface_UI.operation_list[j]
                        j += 1

                        # add non_fnchar in operation
                        for tmp_non_fnchar in tmp_operation["Non_Functional_Characteristic"]:
                            data_list = [1, tmp_non_fnchar["name"], tmp_non_fnchar["value"],
                                         tmp_non_fnchar["dataType"]]
                            if "description" in tmp_non_fnchar.keys():
                                data_list.append(tmp_non_fnchar["description"])
                            else:
                                data_list.append("")
                            op_UI.process_add_non_fnchar(data_list)

                    # add non_fnchar in interface
                    for tmp_non_fnchar in tmp_interface["Non_Functional_Characteristic"]:
                        data_list = [1, tmp_non_fnchar["name"], tmp_non_fnchar["value"],
                                     tmp_non_fnchar["dataType"]]
                        if "description" in tmp_non_fnchar.keys():
                            data_list.append(tmp_non_fnchar["description"])
                        else:
                            data_list.append("")
                        interface_UI.process_add_non_fnchar(data_list)

        except Exception as e:
            print(e)

        return

    def save_file(self):
        save_path, ok = QtWidgets.QFileDialog.getSaveFileName(None, "save", "/", "json(*.json)")

        if ok:
            self.generate_resource(["generate"])
            with open(save_path, "w") as file:
                file.write(self.textEdit.toPlainText())
        return

    def new_file(self):
        reply = PyQt5.QtWidgets.QMessageBox.question(None, "new file",
                                                     "Do you want to create a new file? \n(Please make sure you have saved your file.)",
                                                     PyQt5.QtWidgets.QMessageBox.Yes | PyQt5.QtWidgets.QMessageBox.No,
                                                     PyQt5.QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:

            self.lineEdit_resource.setText("")
            self.lineEdit_provider.setText("")
            for tmp in self.interface_list:
                tmp.safe_delete()
            for tmp in self.fnchar_list:
                tmp.safe_delete()
            self.textEdit.clear()
            PyQt5.sip.delete(self.centralwidget)
            self.setup_UI(self.MainWindow, self, self.RtoA_UI, self.AtoS_UI)

    def change_to_R_A_UI(self):
        reply = QtWidgets.QMessageBox.question(None, "Warning", "Are you sure to change to MODE R-A projection?\n "
                                                                "(make sure you have save your file!)",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            PyQt5.sip.delete(self.centralwidget)
            self.RtoA_UI.setup_UI(self.MainWindow, self, self.RtoA_UI, self.AtoS_UI)
        else:
            self.actionResToAsset.setChecked(False)

    def change_to_A_S_UI(self):
        reply = QtWidgets.QMessageBox.question(None, "Warning", "Are you sure to change to MODE A-S projection?\n "
                                                                "(make sure you have save your file!)",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            PyQt5.sip.delete(self.centralwidget)
            self.AtoS_UI.setup_UI(self.MainWindow, self, self.RtoA_UI, self.AtoS_UI)
        else:
            self.actionAssetToService.setChecked(False)

    def change_to_ResEditor_UI(self):
        self.actionResource.setChecked(True)

    #  menu bar function  end

# test
if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    R_A_ui = RtoA.Ui_MainWindow()
    A_S_ui = AtoS.Ui_MainWindow()
    ui.setup_UI(MainWindow, ui, R_A_ui, A_S_ui)
    MainWindow.show()
    sys.exit(app.exec_())
