import sys
from PySide6 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


        self.setWindowIcon(QtGui.QIcon("calculator\src\image.png"))
        self.setWindowTitle("Calculator PyQt6")

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
        self.pushButton_negative.clicked.connect(self.negative_operador)
        self.pushButton_equals.clicked.connect(self.calcular)
        self.pushButton_clear.clicked.connect(self.clear_pressed)
        self.pushButton_delete.clicked.connect(self.remover_numero)
        self.pushButton_dot.clicked.connect(self.ponto)

        self.num1 = ""
        self.num2 = ""
        self.operador = ""
        self.current_text = ""
        self.iterator=1
        self.resultado = 0.0
        

    def adicionar_numero(self):
        numero = self.sender().text()

        if self.operador == "":
            self.num1 += numero
            self.visor.setText(self.num1)
        else:
            self.num2 += numero
            self.visor.setText(self.num2)
        
    def negative_operador(self):
        if self.operador == "":
            if self.num1 == "":
                self.num1 += "-"
                self.visor.setText(self.num1)
            elif self.num1[0] == "-":
                self.num1 = self.num1[1:]
                self.visor.setText(self.num1)
            else:
                self.num1 = "-" + self.num1
                self.visor.setText(self.num1)
        else:
            if self.num2 == "":
                self.num2 += "-"
                self.visor.setText(self.num2)
            elif self.num2[0] == "-":
                self.num2 = self.num2[1:]
                self.visor.setText(self.num2)
            else:
                self.num2 = "-" + self.num2
                self.visor.setText(self.num2)
    def adicionar_operador(self):
           self.operador = self.sender().text()


    def ponto(self):
        if self.num1 != "" and "." not in self.num1:
            numero = self.sender().text() 
            if self.operador == "":
                if "." in self.num1:
                    self.num1 += numero
                    self.visor.setText(self.num1)

                else:
                    self.num1 += numero
                    self.visor.setText(self.num1)
            else:
                if "." in self.num1:
                    self.num1 += numero
                    self.visor.setText(self.num1)

                else:
                    self.num1 += numero
                    self.visor.setText(self.num1)
        if self.num2 != "" and "." not in self.num2:
            numero = self.sender().text() 
            if self.operador == "":
                if "." in self.num2:
                    self.num2 += numero
                    self.visor.setText(self.num2)

                else:
                    self.num2 += numero
                    self.visor.setText(self.num2)
            else:
                if "." in self.num2:
                    self.num2 += numero
                    self.visor.setText(self.num2)

                else:
                    self.num2 += numero
                    self.visor.setText(self.num2)
        
    def remover_numero(self):
        i = self.iterator
        new_num = self.num1[:-i]
        self.visor.setText(new_num)
        self.iterator =i
        self.num1 = new_num

    def calcular(self):
        if self.num1 != "" and self.num2 != "":
            if self.operador == "+":
                resultado = round(float(self.num1) + float(self.num2),2)
                if float(self.num1) < 0 and float(self.num2) < 0:
                    resultado = "-" + str(abs(resultado))
                elif float(self.num1) < 0 or float(self.num2) < 0:
                        resultado = str(resultado)
                        self.visor.setText(resultado)
                        self.num1 = str(resultado)
                        self.num2 = ""
                        self.operador = ""

            elif self.operador == "×":
                resultado = round(float(self.num1) * float(self.num2), 2)
            elif self.operador == "÷":
                resultado = round(float(self.num1) / float(self.num2), 2)
            elif self.operador == "^":
                resultado = round(pow(float(self.num1), float(self.num2)), 2)
            elif self.operador == "–":
                resultado = round(float(self.num1) - float(self.num2), 2)

            self.current_text = resultado
            self.visor.setText(str(resultado))
            self.num1 = str(resultado) 
            self.num2 = "" 
            self.operador = ""

        elif self.num1 != "" and self.num2 == "":
            self.operador = self.sender().text() 
            self.visor.setText(self.operador)
        elif self.num1 == "" and self.num2 != "":
            self.num1 = self.num2 
            self.num2 = ""
            self.operador = self.sender().text() 
            self.visor.setText(self.operador)
            
    def adicionar_negativo(self):
        if self.operador == "":
            if self.num1 == "":
                self.num1 += "-"
                self.visor.setText(self.num1)
            elif self.num1[0] == "-":
                self.num1 = self.num1[1:]
                self.visor.setText(self.num1)
            else:
                self.num1 = "-" + self.num1
                self.visor.setText(self.num1)
        else:
            if self.num2 == "":
                self.num2 += "-"
                self.visor.setText(self.num2)
            elif self.num2[0] == "-":
                self.num2 = self.num2[1:]
                self.visor.setText(self.num2)
            else:
                self.num2 = "-" + self.num2
                self.visor.setText(self.num2)

    def clear_pressed(self):
        self.visor.setText('')
        self.resultado = ""
        self.num1 = ""
        self.num2 = ""


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())