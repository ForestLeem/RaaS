from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.sip
from UI import nonFnUI
from UI import opUI
from UI import dialog_nonfnchar_interface
from UI import dialog_operation
from Resource import Interface


class InterfaceUI(QtCore.QObject):
    signal_change = QtCore.pyqtSignal(list)

    def __init__(self, MainWindow, height, uid, description):
        super(InterfaceUI, self).__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.height = height
        self.widget_interface = QtWidgets.QWidget(MainWindow)
        self.widget_interface.setGeometry(QtCore.QRect(0, height, 381, 161))
        self.widget_interface.setStyleSheet("background-color:rgb(220, 255, 248)")
        self.widget_interface.setObjectName("widget_interface")

        self.frame_interface_op = QtWidgets.QFrame(self.widget_interface)
        self.frame_interface_op.setGeometry(QtCore.QRect(0, 100, 381, 16))
        self.frame_interface_op.setStyleSheet("background-color:rgb(220, 255, 248)")
        self.frame_interface_op.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_interface_op.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_interface_op.setObjectName("frame_interface_op")
        self.frame_interface_nonfn = QtWidgets.QFrame(self.widget_interface)
        self.frame_interface_nonfn.setGeometry(QtCore.QRect(0, 140, 381, 16))
        self.frame_interface_nonfn.setStyleSheet("background-color:rgb(220, 255, 248)")
        self.frame_interface_nonfn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_interface_nonfn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_interface_nonfn.setObjectName("frame_interface_nonfn")

        self.btn_interface_show_hide = QtWidgets.QPushButton(self.widget_interface)
        self.btn_interface_show_hide.setGeometry(QtCore.QRect(0, 0, 21, 21))
        self.btn_interface_show_hide.setStyleSheet("")
        self.btn_interface_show_hide.setText("")
        self.btn_interface_show_hide.setIcon(icon)
        self.btn_interface_show_hide.setObjectName("btn_interface_show_hide")
        self.label_interface_name = QtWidgets.QLabel(self.widget_interface)
        self.label_interface_name.setGeometry(QtCore.QRect(30, 0, 230, 21))
        self.label_interface_name.setStyleSheet("font: 12pt \"Arial\";")
        self.label_interface_name.setObjectName("label_interface_name")
        self.btn_interface_del = QtWidgets.QPushButton(self.widget_interface)
        self.btn_interface_del.setGeometry(QtCore.QRect(350, 0, 31, 21))
        self.btn_interface_del.setObjectName("btn_interface_del")
        self.label_interface_uid = QtWidgets.QLabel(self.widget_interface)
        self.label_interface_uid.setGeometry(QtCore.QRect(0, 20, 41, 21))
        self.label_interface_uid.setObjectName("label_interface_uid")
        self.label_interface_uidvalue = QtWidgets.QLabel(self.widget_interface)
        self.label_interface_uidvalue.setGeometry(QtCore.QRect(50, 20, 271, 21))
        self.label_interface_uidvalue.setObjectName("label_interface_uidvalue")
        self.label_interface_op = QtWidgets.QLabel(self.widget_interface)
        self.label_interface_op.setGeometry(QtCore.QRect(0, 80, 211, 21))
        self.label_interface_op.setStyleSheet("font: 12pt \"Arial\";")
        self.label_interface_op.setObjectName("label_interface_op")
        self.btn_interface_add_op = QtWidgets.QPushButton(self.widget_interface)
        self.btn_interface_add_op.setGeometry(QtCore.QRect(350, 80, 31, 21))
        self.btn_interface_add_op.setObjectName("btn_interface_add_op")
        self.label_interface_nonfn = QtWidgets.QLabel(self.widget_interface)
        self.label_interface_nonfn.setGeometry(QtCore.QRect(0, 120, 211, 21))
        self.label_interface_nonfn.setStyleSheet("font: 12pt \"Arial\";")
        self.label_interface_nonfn.setObjectName("label_interface_nonfn")
        self.btn_interface_add_nonfn = QtWidgets.QPushButton(self.widget_interface)
        self.btn_interface_add_nonfn.setGeometry(QtCore.QRect(350, 120, 31, 21))
        self.btn_interface_add_nonfn.setObjectName("btn_interface_add_nonfn")
        self.label_interface_description = QtWidgets.QLabel(self.widget_interface)
        self.label_interface_description.setGeometry(QtCore.QRect(0, 50, 381, 21))
        self.label_interface_description.setObjectName("label_interface_description")

        self.label_interface_name.setText(uid)
        self.btn_interface_del.setText("del")
        self.label_interface_uid.setText("· uid:")
        self.label_interface_uidvalue.setText(uid)
        self.label_interface_op.setText("* Operation  :")
        self.btn_interface_add_op.setText("add")
        self.label_interface_nonfn.setText("· Non-functional characteristics:")
        self.btn_interface_add_nonfn.setText("add")
        if description == "":
            self.label_interface_description.setText("")
            self.description = description
        else:
            self.label_interface_description.setText("· description:" + description)
            self.description = description

        self.hide_w = 25
        self.show_w = 151
        self.default_status = "show"
        self.widget_interface.setVisible(True)
        self.btn_interface_del.clicked.connect(self.safe_delete)
        self.btn_interface_show_hide.clicked.connect(self.show_hide)
        self.btn_interface_add_nonfn.clicked.connect(self.add_non_fnchar)
        self.btn_interface_add_op.clicked.connect(self.add_op)

        self.operation_frame_height = 16
        self.operation_frame_location = 100
        self.operation_UI_height = 121
        self.operation_list = []

        self.non_fnchar_frame_height = 16
        self.non_fnchar_frame_location = 140
        self.non_fnchar_UI_height = 111
        self.non_fnchar_list = []

        # record the beginning location of each component
        self.location_frame_nonfnchar = 140
        self.location_label_btn_nonfnchar = 120
        self.location_frame_operation = 100
        self.location_label_btn_operation = 80

    def show_hide(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if self.default_status == "show":
            self.show_w = self.widget_interface.geometry().height()
            self.widget_interface.setGeometry(QtCore.QRect(0, self.height, 381, self.hide_w))
            self.widget_interface.setVisible(True)
            self.btn_interface_show_hide.setIcon(icon)
            self.default_status = "hige"
        else:
            self.widget_interface.setGeometry(QtCore.QRect(0, self.height, 381, self.show_w))
            self.widget_interface.setVisible(True)
            self.btn_interface_show_hide.setIcon(icon2)
            self.default_status = "show"
        self.signal_change.emit(["show_hide", self])

    def add_non_fnchar(self):
        dialog1 = QtWidgets.QDialog()
        dialog1.setWindowModality(QtCore.Qt.ApplicationModal)
        nonfn_dia = dialog_nonfnchar_interface.Ui_Dialog(dialog1)
        nonfn_dia.signal1.connect(self.process_add_non_fnchar)
        dialog1.exec_()

    def process_add_non_fnchar(self, list_data):
        if list_data[0]:   # ok
            # add new fnchar
            _name = list_data[1]
            _value = list_data[2]
            _data_type = list_data[3]
            _description = list_data[4]

            new_non_fnchar_interface_UI = nonFnUI.nonFnUI(self.frame_interface_nonfn, location=self.non_fnchar_frame_height,
                                                          name=_name, value=_value, data_type=_data_type,
                                                          description=_description)
            new_non_fnchar_interface_UI.signal_change.connect(self.re_arrange_UI_signal)
            new_non_fnchar_interface_UI.signal_change.connect(self.process_delete)
            self.non_fnchar_list.append(new_non_fnchar_interface_UI)
            self.re_arrange_UI()
            self.signal_change.emit(["show_hide", self])

        else:
            # don't  add
            return

    def add_op(self):
        # ask for adding operation
        dialog1 = QtWidgets.QDialog()
        dialog1.setWindowModality(QtCore.Qt.ApplicationModal)
        op_dia = dialog_operation.Ui_Dialog(dialog1)
        op_dia.signal1.connect(self.process_add_op)
        # fnchar_dia.signal1.connect(self.process_add_fnchar)
        dialog1.exec_()

    def process_add_op(self, list_data):
        if list_data[0]:
            # add new operation
            _uid = list_data[1]
            _description = list_data[2]

            # check operation's uid
            for tmp_op in self.operation_list:
                if tmp_op.get_uid() == _uid:
                    msg_box = QtWidgets.QMessageBox.information(None, "Warning", "operation UID:" +
                                                                _uid + " exists. Don't add again.")
                    return
            new_op_UI = opUI.OPUI(self.frame_interface_op, self.operation_frame_height, _uid, _description)
            new_op_UI.signal_change.connect(self.re_arrange_UI_signal)
            new_op_UI.signal_change.connect(self.process_delete)
            self.operation_list.append(new_op_UI)
            self.re_arrange_UI()
            self.signal_change.emit(["show_hide", self])

    def change_location(self, location):
        tmp_geometry_h = self.widget_interface.geometry().height()
        self.widget_interface.setGeometry(QtCore.QRect(0, location, 381, tmp_geometry_h))
        self.widget_interface.setVisible(True)

    def get_uid(self):
        return self.label_interface_uidvalue.text()

    def get_UI_height(self):
        return self.widget_interface.height()

    def re_arrange_UI(self):
        frame_op_height = 16
        # arrange operation_UI
        for tmp in self.operation_list:
            tmp.change_location(frame_op_height)
            frame_op_height += tmp.get_UI_height()
        self.frame_interface_op.setGeometry(QtCore.QRect
                                            (0, self.location_frame_operation, 381, frame_op_height))
        self.label_interface_nonfn.setGeometry(QtCore.QRect
                                               (0, self.location_label_btn_nonfnchar + frame_op_height - 16, 211, 21))
        self.btn_interface_add_nonfn.setGeometry(QtCore.QRect
                                                 (350, self.location_label_btn_nonfnchar + frame_op_height - 16, 31, 21))
        top = self.widget_interface.geometry().top()

        # arrange nonfnchar_UI
        frame_nonfnchar_height = 16
        for tmp in self.non_fnchar_list:
            tmp.change_location(frame_nonfnchar_height)
            frame_nonfnchar_height += tmp.get_UI_height()

        self.frame_interface_nonfn.setGeometry(QtCore.QRect
                                               (0, self.location_frame_nonfnchar + frame_op_height - 16,
                                                381, frame_nonfnchar_height))
        self.widget_interface.setGeometry(QtCore.
                                          QRect(0, top, 381, self.location_frame_nonfnchar +
                                                frame_op_height + self.frame_interface_nonfn.height()))

    def re_arrange_UI_signal(self, data_list):
        _type = data_list[0]
        _object = data_list[1]
        if _type == "show_hide":
            frame_op_height = 16
            # arrange operation_UI
            for tmp in self.operation_list:
                tmp.change_location(frame_op_height)
                frame_op_height += tmp.get_UI_height()
            self.frame_interface_op.setGeometry(QtCore.QRect
                                                (0, self.location_frame_operation, 381, frame_op_height))
            self.label_interface_nonfn.setGeometry(QtCore.QRect
                                                   (0, self.location_label_btn_nonfnchar + frame_op_height - 16, 211, 21))
            self.btn_interface_add_nonfn.setGeometry(QtCore.QRect
                                                     (350, self.location_label_btn_nonfnchar + frame_op_height - 16, 31, 21))
            top = self.widget_interface.geometry().top()

            # arrange nonfnchar_UI
            frame_nonfnchar_height = 16
            for tmp in self.non_fnchar_list:
                tmp.change_location(frame_nonfnchar_height)
                frame_nonfnchar_height += tmp.get_UI_height()

            self.frame_interface_nonfn.setGeometry(QtCore.QRect
                                                   (0, self.location_frame_nonfnchar + frame_op_height - 16,
                                                    381, frame_nonfnchar_height))
            self.widget_interface.setGeometry(QtCore.
                                              QRect(0, top, 381, self.location_frame_nonfnchar +
                                                    frame_op_height + self.frame_interface_nonfn.height()))

    def process_delete(self, data_list):
        _type = data_list[0]
        _object = data_list[1]
        if _type == "del_non_fnchar":
            for i in range(0, len(self.non_fnchar_list)):
                if _object == self.non_fnchar_list[i]:
                    self.non_fnchar_list.pop(i)
                    break
        if _type == "del_operation":
            for i in range(0, len(self.operation_list)):
                if _object == self.operation_list[i]:
                    self.operation_list.pop(i)
                    break
        self.re_arrange_UI()
        self.signal_change.emit(["show_hide", self])

    def safe_delete(self):
        self.signal_change.emit(["del_interface", self])
        PyQt5.sip.delete(self.widget_interface)

    def get_interface_class(self):
        result = Interface.Interface()
        # set uid
        result.uid = self.label_interface_uidvalue.text()
        # set description
        result.description = self.description

        # add operation
        for tmp in self.operation_list:
            tmp_op_class = tmp.get_op_class()
            result.add_operation(tmp_op_class)

        # add NonFnChar
        for tmp in self.non_fnchar_list:
            tmp_non_fnchar_class = tmp.get_non_fnchar_class()
            result.add_NonFnChar(tmp_non_fnchar_class)

        return result
