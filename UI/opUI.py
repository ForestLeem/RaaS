import PyQt5.sip
from PyQt5 import QtCore, QtGui, QtWidgets
from UI import dialog_nonfnchar_operation
from UI import nonFnUI
from Resource import Operation


class OPUI(QtCore.QObject):
    signal_change = QtCore.pyqtSignal(list)
    def __init__(self, MainWindow, location, uid, description):
        super(OPUI, self).__init__(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.location = location
        self.widget_op = QtWidgets.QWidget(MainWindow)
        self.widget_op.setGeometry(QtCore.QRect(0, location, 361, 121))
        self.widget_op.setStyleSheet("background-color:rgb(255, 205, 205)")
        self.widget_op.setObjectName("widget_op")

        self.frame_op_nonfn = QtWidgets.QFrame(self.widget_op)
        self.frame_op_nonfn.setGeometry(QtCore.QRect(0, 100, 361, 16))
        self.frame_op_nonfn.setStyleSheet("background-color:rgb(255, 200, 205)")
        self.frame_op_nonfn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_op_nonfn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_op_nonfn.setObjectName("frame_op_nonfn")

        self.btn_op_show_hide = QtWidgets.QPushButton(self.widget_op)
        self.btn_op_show_hide.setGeometry(QtCore.QRect(0, 0, 21, 21))
        self.btn_op_show_hide.setStyleSheet("")
        self.btn_op_show_hide.setText("")
        self.btn_op_show_hide.setIcon(icon)
        self.btn_op_show_hide.setObjectName("btn_op_show_hide")
        self.label_op_name = QtWidgets.QLabel(self.widget_op)
        self.label_op_name.setGeometry(QtCore.QRect(30, 0, 200, 21))
        self.label_op_name.setObjectName("label_op_name")
        self.btn_op_del = QtWidgets.QPushButton(self.widget_op)
        self.btn_op_del.setGeometry(QtCore.QRect(330, 0, 31, 21))
        self.btn_op_del.setObjectName("btn_op_del")
        self.label_op_uid = QtWidgets.QLabel(self.widget_op)
        self.label_op_uid.setGeometry(QtCore.QRect(0, 20, 41, 21))
        self.label_op_uid.setObjectName("label_op_uid")
        self.label_op_uidvalue = QtWidgets.QLabel(self.widget_op)
        self.label_op_uidvalue.setGeometry(QtCore.QRect(50, 20, 271, 21))
        self.label_op_uidvalue.setObjectName("label_op_uidvalue")
        self.label_op_nonfn = QtWidgets.QLabel(self.widget_op)
        self.label_op_nonfn.setGeometry(QtCore.QRect(0, 80, 211, 21))
        self.label_op_nonfn.setStyleSheet("font: 12pt \"Arial\";")
        self.label_op_nonfn.setObjectName("label_op_nonfn")
        self.btn_op_add_nonfn = QtWidgets.QPushButton(self.widget_op)
        self.btn_op_add_nonfn.setGeometry(QtCore.QRect(330, 80, 31, 21))
        self.btn_op_add_nonfn.setObjectName("btn_op_add_nonfn")
        self.label_op_description = QtWidgets.QLabel(self.widget_op)
        self.label_op_description.setGeometry(QtCore.QRect(0, 50, 361, 21))
        self.label_op_description.setObjectName("label_nonfn_description_2")

        self.label_op_name.setText(uid)
        self.btn_op_del.setText("del")
        self.label_op_uid.setText("· uid:")
        self.label_op_uidvalue.setText(uid)
        self.label_op_nonfn.setText("· Non-functional characteristics:")
        self.btn_op_add_nonfn.setText("add")
        self.hide_w = 21
        self.show_w = 0
        self.default_status = "show"

        self.btn_op_show_hide.clicked.connect(self.show_hide)
        self.btn_op_del.clicked.connect(self.safe_delete)
        self.btn_op_add_nonfn.clicked.connect(self.add_non_fnchar)

        self.non_fnchar_frame_height = 16
        self.non_fnchar_frame_location = 100
        self.non_fnchar_UI_height = 111
        self.non_fnchar_list = []

        self.location_frame_nonfnchar = 100

        if description == "":
            self.label_op_description.setText("")
            self.description= description
        else:
            self.label_op_description.setText("· description:" + description)
            self.description = description
        self.widget_op.setVisible(True)

    def get_uid(self):
        return self.label_op_uidvalue.text()

    def get_UI_height(self):
        return self.widget_op.height()

    def show_hide(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if self.default_status == "show":
            self.show_w = self.widget_op.geometry().height()
            self.widget_op.setGeometry(QtCore.QRect(0, self.location, 361, self.hide_w))
            self.widget_op.setVisible(True)
            self.btn_op_show_hide.setIcon(icon)
            self.default_status = "hide"
        else:
            self.widget_op.setGeometry(QtCore.QRect(0, self.location, 361, self.show_w))
            self.widget_op.setVisible(True)
            self.btn_op_show_hide.setIcon(icon2)
            self.default_status = "show"
        self.signal_change.emit(["show_hide", self])

    def change_location(self, location):
        tmp_gemotry_h = self.widget_op.geometry().height()
        self.widget_op.setGeometry(QtCore.QRect(10, location, 361, tmp_gemotry_h))
        self.widget_op.setVisible(True)

    def add_non_fnchar(self):
        dialog1 = QtWidgets.QDialog()
        dialog1.setWindowModality(QtCore.Qt.ApplicationModal)
        nonfn_dia = dialog_nonfnchar_operation.Ui_Dialog(dialog1)
        nonfn_dia.signal1.connect(self.process_add_non_fnchar)
        dialog1.exec_()

    def process_add_non_fnchar(self, list_data):
        if list_data[0]:  # ok
            # add new fnchar
            _name = list_data[1]
            _value = list_data[2]
            _data_type = list_data[3]
            _description = list_data[4]

            new_non_fnchar_interface_UI = nonFnUI.nonFnUI(self.frame_op_nonfn,
                                                          location=self.location_frame_nonfnchar,
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
        pass

    def re_arrange_UI(self):
        frame_nonfnchar_height = 16
        for tmp in self.non_fnchar_list:
            tmp.change_location(frame_nonfnchar_height)
            frame_nonfnchar_height += tmp.get_UI_height()
        self.frame_op_nonfn.setGeometry(QtCore.QRect
                                        (0, self.location_frame_nonfnchar, 361, frame_nonfnchar_height))
        top = self.widget_op.geometry().top()
        self.widget_op.setGeometry(QtCore.QRect
                                   (10, top, 361, self.location_frame_nonfnchar + frame_nonfnchar_height))

    def re_arrange_UI_signal(self, data_list):
        _type = data_list[0]
        _object = data_list[1]
        if _type == "show_hide":
            frame_nonfnchar_height = 16
            for tmp in self.non_fnchar_list:
                tmp.change_location(frame_nonfnchar_height)
                frame_nonfnchar_height += tmp.get_UI_height()
            self.frame_op_nonfn.setGeometry(QtCore.QRect
                                            (0, self.location_frame_nonfnchar, 361, frame_nonfnchar_height))
            top = self.widget_op.geometry().top()
            self.widget_op.setGeometry(QtCore.QRect
                                       (10, top, 361, self.location_frame_nonfnchar + frame_nonfnchar_height))
            self.signal_change.emit(["show_hide", self])

    def process_delete(self, data_list):
        _type = data_list[0]
        _object = data_list[1]
        if _type == "del_non_fnchar":
            for i in range(0, len(self.non_fnchar_list)):
                if _object == self.non_fnchar_list[i]:
                    self.non_fnchar_list.pop(i)
                    break
        self.re_arrange_UI()
        self.signal_change.emit(["show_hide", self])
        return

    def safe_delete(self):
        self.signal_change.emit(["del_operation", self])
        PyQt5.sip.delete(self.widget_op)

    def get_op_class(self):
        result = Operation.Operation()

        # set uid
        result.uid = self.label_op_uidvalue.text()

        # set description
        result.description = self.description

        # add Nonfnchar
        for tmp in self.non_fnchar_list:
            tmp_non_fnchar_class = tmp.get_non_fnchar_class()
            result.add_NonFnChar(tmp_non_fnchar_class)
        return result

