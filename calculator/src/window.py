# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 620)
        MainWindow.setMaximumSize(QSize(360, 620))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(38, 97, 175);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.visor = QLCDNumber(self.frame)
        self.visor.setObjectName(u"visor")
        font = QFont()
        font.setPointSize(9)
        self.visor.setFont(font)
        self.visor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.visor, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_result = QPushButton(self.frame)
        self.btn_result.setObjectName(u"btn_result")
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_result.setFont(font1)
        self.btn_result.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.btn_result, 8, 4, 1, 1)

        self.btn_4 = QPushButton(self.frame)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setFont(font1)
        self.btn_4.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_4, 6, 0, 1, 1)

        self.btn_3 = QPushButton(self.frame)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setFont(font1)
        self.btn_3.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_3, 7, 2, 1, 1)

        self.btn_division = QPushButton(self.frame)
        self.btn_division.setObjectName(u"btn_division")
        self.btn_division.setFont(font1)
        self.btn_division.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.btn_division, 2, 4, 1, 1)

        self.btn_5 = QPushButton(self.frame)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setFont(font1)
        self.btn_5.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_5, 6, 1, 1, 1)

        self.btn_addition = QPushButton(self.frame)
        self.btn_addition.setObjectName(u"btn_addition")
        self.btn_addition.setFont(font1)
        self.btn_addition.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.btn_addition, 7, 4, 1, 1)

        self.btn_6 = QPushButton(self.frame)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setFont(font1)
        self.btn_6.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_6, 6, 2, 1, 1)

        self.btn_multiplication = QPushButton(self.frame)
        self.btn_multiplication.setObjectName(u"btn_multiplication")
        self.btn_multiplication.setFont(font1)
        self.btn_multiplication.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.btn_multiplication, 4, 4, 1, 1)

        self.btn_2 = QPushButton(self.frame)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setFont(font1)
        self.btn_2.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_2, 7, 1, 1, 1)

        self.btn_0 = QPushButton(self.frame)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setFont(font1)
        self.btn_0.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_0, 8, 1, 1, 1)

        self.btn_1 = QPushButton(self.frame)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setFont(font1)
        self.btn_1.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_1, 7, 0, 1, 1)

        self.btn_dot = QPushButton(self.frame)
        self.btn_dot.setObjectName(u"btn_dot")
        self.btn_dot.setFont(font1)
        self.btn_dot.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_dot, 8, 2, 1, 1)

        self.btn_8 = QPushButton(self.frame)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setFont(font1)
        self.btn_8.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_8, 4, 1, 1, 1)

        self.btn_subtraction = QPushButton(self.frame)
        self.btn_subtraction.setObjectName(u"btn_subtraction")
        self.btn_subtraction.setFont(font1)
        self.btn_subtraction.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.btn_subtraction, 6, 4, 1, 1)

        self.btn_7 = QPushButton(self.frame)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setFont(font1)
        self.btn_7.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_7, 4, 0, 1, 1)

        self.btn_9 = QPushButton(self.frame)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setFont(font1)
        self.btn_9.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_9, 4, 2, 1, 1)

        self.btn_clear = QPushButton(self.frame)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setFont(font1)
        self.btn_clear.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.btn_clear, 2, 0, 1, 1)

        self.btn_delete_2 = QPushButton(self.frame)
        self.btn_delete_2.setObjectName(u"btn_delete_2")
        self.btn_delete_2.setFont(font1)
        self.btn_delete_2.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.btn_delete_2, 2, 1, 1, 1)

        self.btn_potentiation = QPushButton(self.frame)
        self.btn_potentiation.setObjectName(u"btn_potentiation")
        self.btn_potentiation.setFont(font1)
        self.btn_potentiation.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.btn_potentiation, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 360, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_result.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_addition.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_multiplication.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_subtraction.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_delete_2.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.btn_potentiation.setText(QCoreApplication.translate("MainWindow", u"^", None))
    # retranslateUi

