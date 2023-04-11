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
        numero = self.sender().text() 
        if self.operador == "":
            if "." in self.num1:
                self.num1 += numero
                self.visor.display(self.num1)

            else:
                self.num1 += numero
                self.visor.display(self.num1)
        else:
            if "." in self.num2:
                self.num2 += numero
                self.visor.display(self.num2)

            else:
                self.num2 += numero
                self.visor.display(self.num2)
        

    def remover_numero(self):
        i = self.iterator
        new_num = self.num1[:-i]
        self.visor.display(new_num)
        self.iterator =i
        self.num1 = new_num


       




    def calcular(self):
           if self.num1 != "" and self.num2 != "":
               if self.operador == "+":
                   resultado = round(float(self.num1) + float(self.num2),2)
               elif self.operador == "-":
                   resultado = round(float(self.num1) - float(self.num2),2)
               elif self.operador == "*":
                   resultado = round(float(self.num1) * float(self.num2),2)
               elif self.operador == "/":
                   resultado = round(float(self.num1) / float(self.num2),2)
               elif self.operador == "^":
                   resultado = round(pow(float(self.num1),float(self.num2)),2)
               self.visor.display(str(resultado))
               self.num1 = str(resultado)
               self.num2 = ""
               self.operador = ""
               self.current_text = resultado
               print(self.current_text)

    def clear_pressed(self):
        self.visor.display('')
        self.num1 = ""
        self.num2 = ""


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())