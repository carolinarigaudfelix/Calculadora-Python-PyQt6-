import sys
from PySide6 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow, QLCDNumber

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

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
        self.pushButton_potentiation.clicked.connect(self.adicionar_operador)
        self.pushButton_equals.clicked.connect(self.calcular)
        self.pushButton_clear.clicked.connect(self.clear_pressed)
        self.pushButton_delete.clicked.connect(self.remover_numero)
        self.pushButton_dot.clicked.connect(self.ponto)

        self.num1 = ""
        self.num2 = ""
        self.operador = ""
        self.current_text = ""
        self.iterator=1
        self.vis = QLCDNumber()
        


    def adicionar_numero(self):
        numero = self.sender().text()
        if self.operador == "":
            self.num1 += numero
            self.visor.display(self.num1)
        else:
            self.num2 += numero
            self.visor.display(self.num2)
        print(numero)
        
    def adicionar_operador(self):
           self.operador = self.sender().text()
           self.pushButton_equals.setText("")

    def ponto(self):
        if '.' not in self.num1:
            self.visor.display(+ '.')
        # teste = str(self.current_text)
        # print(teste)
        # # Verifique se já há um ponto na tela
        # if '.' not in self.visor:
        #     # Se não houver, adicione um ponto
        #     self.visor.display(self.visor.display + '.')

    def remover_numero(self):
        i = self.iterator = self.iterator + 1
        resultado = str(self.current_text)
        # i=0
        # for i in resultado:
        #     print(i)
        print(resultado[:-i])
        

        # print(resultado)
        # new_result = resultado[:-1]
        # self.visor.display(str(new_result))

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
               elif self.operador == "^":
                   resultado = pow(float(self.num1),float(self.num2))
               self.visor.display(str(resultado))
               self.num1 = str(resultado)
               self.num2 = ""
               self.operador = ""
               self.current_text = resultado
               print(self.current_text)

    def clear_pressed(self):
        self.resultado = 0
        self.operador = 0
        self.num1 = 0
        self.num2 = 0
        self.visor.display('')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())