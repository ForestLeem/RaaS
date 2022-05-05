# importing libraries
from UI import Res_main
from PyQt5 import QtCore, QtGui, QtWidgets

a = {"@123":"123"}
a["@twst"]  =1
print(a)
if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Res_main.Ui_MainWindow(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

