# importing libraries
from UI import Res_main
from PyQt5 import QtCore, QtGui, QtWidgets
from UI import RtoA
from UI import AtoS


if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Res_main.Ui_MainWindow()
    R_A_ui = RtoA.Ui_MainWindow()
    A_S_ui = AtoS.Ui_MainWindow()
    ui.setup_UI(MainWindow, ui, R_A_ui, A_S_ui)
    MainWindow.show()
    sys.exit(app.exec_())
