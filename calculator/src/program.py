import sys
from PySide6 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        def calc(arg):
           if arg == None:
            self.visor.display('')
           else: 
            self.visor.display(arg)
        

        # Conecta os botões aos slots

        self.pushButton_0.clicked.connect(self.adicionar_numero)
        self.pushButton_1.clicked.connect(self.adicionar_numero)
        self.pushButton_2.clicked.connect(self.adicionar_numero)
        self.pushButton_3.clicked.connect(self.adicionar_numero)
        self.pushButton_4.clicked.connect(self.adicionar_numero)
        self.pushButton_5.clicked.connect(self.adicionar_numero)
        self.pushButton_6.clicked.connect(self.adicionar_numero)
        self.pushButton_7.clicked.connect(self.adicionar_numero)
        self.pushButton_8.clicked.connect(self.adicionar_numero)
        self.pushButton_9.clicked.connect(self.adicionar_numero)
        self.pushButton_add.clicked.connect(self.adicionar_operador)
        self.pushButton_subtract.clicked.connect(self.adicionar_operador)
        self.pushButton_multiply.clicked.connect(self.adicionar_operador)
        self.pushButton_divide.clicked.connect(self.adicionar_operador)
        # self.btn_potentiation.clicked.connect(lambda: self.operator_pressed('^'))
        self.pushButton_equals.clicked.connect(self.calcular)
        self.pushButton_clear.clicked.connect(self.clear_pressed)

        self.num1 = ""
        self.num2 = ""
        self.operador = ""


    def adicionar_numero(self):
        numero = self.sender().text()
        if self.operador == "":
            self.num1 += numero
            self.visor.display(self.num1)
        else:
            self.num2 += numero
            self.visor.display(self.num2)

    # def number_pressed(self, digit):
    #     self.current_number += digit
    #     self.visor.setText(self.current_number)

    def adicionar_operador(self):
           self.operador = self.sender().text()
           self.pushButton_equals.setText("")

    def calcular(self):
           if self.num1 != "" and self.num2 != "":
               if self.operador == "+":
                   resultado = float(self.num1) + float(self.num2)
               elif self.operador == "-":
                   resultado = float(self.num1) - float(self.num2)
               elif self.operador == "*":
                   resultado = float(self.num1) * float(self.num2)
               elif self.operador == "/":
                   resultado = float(self.num1) / float(self.num2)
               self.visor.display(str(resultado))
               self.num1 = str(resultado)
               self.num2 = ""
               self.operador = ""

    def clear_pressed(self):
        self.result = 0
        self.operation = ''
        self.current_number = ''
        self.visor.setText('')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())