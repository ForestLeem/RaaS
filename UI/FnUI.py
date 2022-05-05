import PyQt5.sip
from PyQt5 import QtCore, QtGui, QtWidgets
from Resource import Resource as Res
from Resource import Func_Char



class FnUI(QtCore.QObject):
    signal_change = QtCore.pyqtSignal(list)

    def __init__(self, MainWindow, location, name, description):
        super(FnUI, self).__init__(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.widget_fnchar = QtWidgets.QWidget(MainWindow)
        self.widget_fnchar.setGeometry(QtCore.QRect(10, location, 361, 81))
        self.widget_fnchar.setStyleSheet("background-color:rgb(231, 255, 248)")
        self.widget_fnchar.setObjectName("widget_fnchar")
        self.btn_fnchar_del = QtWidgets.QPushButton(self.widget_fnchar)
        self.btn_fnchar_del.setGeometry(QtCore.QRect(330, 0, 31, 21))
        self.btn_fnchar_del.setObjectName("btn_fnchar_del")
        self.btn_fnchar_show_hide = QtWidgets.QPushButton(self.widget_fnchar)
        self.btn_fnchar_show_hide.setGeometry(QtCore.QRect(0, 0, 21, 21))
        self.btn_fnchar_show_hide.setStyleSheet("")
        self.btn_fnchar_show_hide.setText("")
        self.btn_fnchar_show_hide.setIcon(icon2)
        self.btn_fnchar_show_hide.setObjectName("btn_fnchar_show_hide")
        self.label__fnchar_key = QtWidgets.QLabel(self.widget_fnchar)
        self.label__fnchar_key.setGeometry(QtCore.QRect(0, 30, 61, 21))
        self.label__fnchar_key.setObjectName("label__fnchar_key")
        self.label_fnchar_name = QtWidgets.QLabel(self.widget_fnchar)
        self.label_fnchar_name.setGeometry(QtCore.QRect(30, 0, 81, 21))
        self.label_fnchar_name.setObjectName("label_fnchar_name")
        self.label_fnchar_value = QtWidgets.QLabel(self.widget_fnchar)
        self.label_fnchar_value.setGeometry(QtCore.QRect(70, 30, 291, 21))
        self.label_fnchar_value.setObjectName("label_fnchar_value")
        self.label_fnchar_description = QtWidgets.QLabel(self.widget_fnchar)
        self.label_fnchar_description.setGeometry(QtCore.QRect(0, 60, 361, 21))
        self.label_fnchar_description.setObjectName("label_fnchar_description")

        self.height = location
        self.btn_fnchar_show_hide.clicked.connect(self.show_hide)
        self.btn_fnchar_del.clicked.connect(self.safe_delete)
        self.default_status = "show"
        self.show_w = 81
        self.hide_w = 25
        self.btn_fnchar_del.setText("del")
        self.label__fnchar_key.setText("· f_type:")
        self.label_fnchar_name.setText(name)
        self.label_fnchar_value.setText(name)
        if description == "":
            self.label_fnchar_description.setText("")
            self.description = description
        else:
            self.label_fnchar_description.setText("· description:" + description)
            self.description = description
        self.widget_fnchar.setVisible(True)

    def show_hide(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if self.default_status == "show":
            self.widget_fnchar.setGeometry(QtCore.QRect(10, self.height, 361, self.hide_w))
            self.widget_fnchar.setVisible(True)
            self.btn_fnchar_show_hide.setIcon(icon)
            self.default_status = "hige"
        else:
            self.widget_fnchar.setGeometry(QtCore.QRect(10, self.height, 361, self.show_w))
            self.widget_fnchar.setVisible(True)
            self.btn_fnchar_show_hide.setIcon(icon2)
            self.default_status = "show"
        self.signal_change.emit(["show_hide", self])

    def change_location(self, height):
        tmp_geometry_h = self.widget_fnchar.geometry().height()
        self.widget_fnchar.setGeometry(QtCore.QRect(10, height, 361, tmp_geometry_h))
        self.widget_fnchar.setVisible(True)

    def get_f_type(self):
        return self.label_fnchar_value.text()

    def get_UI_height(self):
        return self.widget_fnchar.height()

    def get_FnChar_class(self):
        # get fnchar class
        result = Func_Char.FnChar()
        result.f_type = self.label_fnchar_value.text()
        result.description = self.description
        return result

    def safe_delete(self):
        self.signal_change.emit(["del_fnchar", self])
        PyQt5.sip.delete(self.widget_fnchar)


