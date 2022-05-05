from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.sip
from Resource import Non_Func_Char


class nonFnUI(QtCore.QObject):
    signal_change = QtCore.pyqtSignal(list)

    def __init__(self, MainWindow, location, name, value, data_type, description):
        super(nonFnUI, self).__init__(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.location = location
        self.widget_nonfn = QtWidgets.QWidget(MainWindow)
        self.widget_nonfn.setGeometry(QtCore.QRect(10, location, 341, 111))
        self.widget_nonfn.setStyleSheet("background-color:rgb(255, 205, 205)")
        self.widget_nonfn.setObjectName("widget_nonfn")
        self.btn_nonfn_show_hide = QtWidgets.QPushButton(self.widget_nonfn)
        self.btn_nonfn_show_hide.setGeometry(QtCore.QRect(0, 0, 21, 21))
        self.btn_nonfn_show_hide.setStyleSheet("")
        self.btn_nonfn_show_hide.setText("")
        self.btn_nonfn_show_hide.setIcon(icon)
        self.btn_nonfn_show_hide.setObjectName("btn_nonfn_show_hide")
        self.label_nonfn_name = QtWidgets.QLabel(self.widget_nonfn)
        self.label_nonfn_name.setGeometry(QtCore.QRect(30, 0, 200, 21))
        self.label_nonfn_name.setObjectName("label_nonfn_name")
        self.btn_nonfn_del = QtWidgets.QPushButton(self.widget_nonfn)
        self.btn_nonfn_del.setGeometry(QtCore.QRect(310, 0, 31, 21))
        self.btn_nonfn_del.setObjectName("btn_nonfn_del")
        self.label_nonfn_name_key = QtWidgets.QLabel(self.widget_nonfn)
        self.label_nonfn_name_key.setGeometry(QtCore.QRect(0, 20, 71, 21))
        self.label_nonfn_name_key.setObjectName("label_nonfn_name_key")
        self.label_nonfn_name_val = QtWidgets.QLabel(self.widget_nonfn)
        self.label_nonfn_name_val.setGeometry(QtCore.QRect(80, 20, 241, 21))
        self.label_nonfn_name_val.setObjectName("label_nonfn_name_val")
        self.label_nonfn_value_key = QtWidgets.QLabel(self.widget_nonfn)
        self.label_nonfn_value_key.setGeometry(QtCore.QRect(0, 40, 71, 21))
        self.label_nonfn_value_key.setObjectName("label_nonfn_value_key")
        self.label_nonfn_DT_key = QtWidgets.QLabel(self.widget_nonfn)
        self.label_nonfn_DT_key.setGeometry(QtCore.QRect(0, 60, 80, 21))
        self.label_nonfn_DT_key.setObjectName("label_nonfn_DT_key")
        self.label_nonfn_value_val = QtWidgets.QLabel(self.widget_nonfn)
        self.label_nonfn_value_val.setGeometry(QtCore.QRect(80, 40, 241, 21))
        self.label_nonfn_value_val.setObjectName("label_nonfn_value_val")
        self.label_nonfn_DT_val = QtWidgets.QLabel(self.widget_nonfn)
        self.label_nonfn_DT_val.setGeometry(QtCore.QRect(80, 60, 241, 21))
        self.label_nonfn_DT_val.setObjectName("label_nonfn_DT_val")
        self.label_nonfn_description = QtWidgets.QLabel(self.widget_nonfn)
        self.label_nonfn_description.setGeometry(QtCore.QRect(0, 80, 341, 21))
        self.label_nonfn_description.setObjectName("label_nonfn_description")
        self.label_nonfn_name.setText(name)
        self.btn_nonfn_del.setText("del")
        self.label_nonfn_name_key.setText("·name:")
        self.label_nonfn_name_val.setText(name)
        self.label_nonfn_value_key.setText("·value:")
        self.label_nonfn_DT_key.setText("·dataType:")
        self.label_nonfn_value_val.setText(value)
        self.label_nonfn_DT_val.setText(data_type)

        self.hide_w = 21
        self.show_w = 0
        self.default_status = "show"
        self.btn_nonfn_show_hide.clicked.connect(self.show_hide)
        self.btn_nonfn_del.clicked.connect(self.safe_delete)

        if description == "":
            self.label_nonfn_description.setText("")
            self.description = description
        else:
            self.label_nonfn_description.setText("·description:" + description)
            self.description = description
        self.widget_nonfn.setVisible(True)

    def get_name(self):
        return self.label_nonfn_name_val.text()

    def get_UI_height(self):
        return self.widget_nonfn.height()

    def change_location(self, location):
        tmp_gemotry_h = self.widget_nonfn.geometry().height()
        self.widget_nonfn.setGeometry(QtCore.QRect(10, location, 361, tmp_gemotry_h))
        self.widget_nonfn.setVisible(True)

    def show_hide(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if self.default_status == "show":
            self.show_w = self.widget_nonfn.geometry().height()
            self.widget_nonfn.setGeometry(QtCore.QRect(10, self.location, 361, self.hide_w))
            self.widget_nonfn.setVisible(True)
            self.btn_nonfn_show_hide.setIcon(icon)
            self.default_status = "hide"
        else:
            self.widget_nonfn.setGeometry(QtCore.QRect(10, self.location, 361, self.show_w))
            self.widget_nonfn.setVisible(True)
            self.btn_nonfn_show_hide.setIcon(icon2)
            self.default_status = "show"
        self.signal_change.emit(["show_hide", self])

    def safe_delete(self):
        self.signal_change.emit(["del_non_fnchar", self])
        PyQt5.sip.delete(self.widget_nonfn)

    def get_non_fnchar_class(self):
        result = Non_Func_Char.NonFnChar()
        result.name = self.label_nonfn_name_val.text()
        result.value = self.label_nonfn_value_val.text()
        result.dataType = self.label_nonfn_DT_val.text()
        result.description = self.description
        return result

