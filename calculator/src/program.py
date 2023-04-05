import sys
from PySide6 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        lista = []    
        def calc(arg):
           if arg == None:
            self.visor.display('')
           else: 
            self.visor.display(arg)
        

        # Conecta os botões aos slots

        self.btn_0.clicked.connect(lambda: calc(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: calc(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: calc(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: calc(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: calc(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: calc(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: calc(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: calc(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: calc(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: calc(self.btn_9.text()))
        self.btn_addition.clicked.connect(lambda: calc(self.btn_addition.text()))
        self.btn_subtraction.clicked.connect(lambda: calc(self.btn_subtraction.text()))
        self.btn_multiplication.clicked.connect(lambda: calc(self.btn_multiplication.text()))
        self.btn_potentiation.clicked.connect(lambda: calc(self.btn_potentiation.text()))
        self.btn_result.clicked.connect(lambda: calc(self.btn_result.text()))
        self.btn_clear.clicked.connect(lambda: calc(self.btn_clear.text()))
        self.btn_delete_2.clicked.connect(lambda: calc(self.btn_delete2.text()))
        self.btn_dot.clicked.connect(lambda: calc(self.btn_dot.text()))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())