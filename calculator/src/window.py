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
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_equals = QPushButton(self.frame)
        self.pushButton_equals.setObjectName(u"pushButton_equals")
        font = QFont()
        font.setPointSize(12)
        self.pushButton_equals.setFont(font)
        self.pushButton_equals.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.pushButton_equals, 8, 4, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_4, 6, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_3, 7, 2, 1, 1)

        self.pushButton_divide = QPushButton(self.frame)
        self.pushButton_divide.setObjectName(u"pushButton_divide")
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.pushButton_divide, 2, 4, 1, 1)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_5, 6, 1, 1, 1)

        self.pushButton_add = QPushButton(self.frame)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.pushButton_add, 7, 4, 1, 1)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_6, 6, 2, 1, 1)

        self.pushButton_multiply = QPushButton(self.frame)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        self.pushButton_multiply.setFont(font)
        self.pushButton_multiply.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.pushButton_multiply, 4, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_2, 7, 1, 1, 1)

        self.pushButton_0 = QPushButton(self.frame)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_0, 8, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.frame)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_1, 7, 0, 1, 1)

        self.pushButton_dot = QPushButton(self.frame)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_dot, 8, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_8, 4, 1, 1, 1)

        self.pushButton_subtract = QPushButton(self.frame)
        self.pushButton_subtract.setObjectName(u"pushButton_subtract")
        self.pushButton_subtract.setFont(font)
        self.pushButton_subtract.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.pushButton_subtract, 6, 4, 1, 1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(u"background-color: rgb(157, 195, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_9, 4, 2, 1, 1)

        self.pushButton_clear = QPushButton(self.frame)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.pushButton_clear, 2, 0, 1, 1)

        self.pushButton_delete = QPushButton(self.frame)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.pushButton_delete, 2, 1, 1, 1)

        self.pushButton_potentiation = QPushButton(self.frame)
        self.pushButton_potentiation.setObjectName(u"pushButton_potentiation")
        self.pushButton_potentiation.setFont(font)
        self.pushButton_potentiation.setStyleSheet(u"background: rgb(85, 170, 255);")

        self.gridLayout.addWidget(self.pushButton_potentiation, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.visor = QLCDNumber(self.frame)
        self.visor.setObjectName(u"visor")
        self.visor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0)")

        self.gridLayout_2.addWidget(self.visor, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 360, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_equals.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_subtract.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton_potentiation.setText(QCoreApplication.translate("MainWindow", u"^", None))
    # retranslateUi

