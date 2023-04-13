# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(469, 710)
        MainWindow.setStyleSheet(u"background-color: rgb(21, 21, 21);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(21, 21, 21);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_subtract = QPushButton(self.centralwidget)
        self.pushButton_subtract.setObjectName(u"pushButton_subtract")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_subtract.sizePolicy().hasHeightForWidth())
        self.pushButton_subtract.setSizePolicy(sizePolicy)
        self.pushButton_subtract.setStyleSheet(u"QPushButton{\n"
"font: 75 36pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(255, 73, 170);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 235, 255);\n"
"	color: rgb(255, 112, 181);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_subtract, 3, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(173, 173, 173);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(173, 173, 173);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)

        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(173, 173, 173);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(173, 173, 173);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)

        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"		background-color: rgb(255, 140, 211);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_clear, 1, 0, 1, 1)

        self.pushButton_divide = QPushButton(self.centralwidget)
        self.pushButton_divide.setObjectName(u"pushButton_divide")
        sizePolicy.setHeightForWidth(self.pushButton_divide.sizePolicy().hasHeightForWidth())
        self.pushButton_divide.setSizePolicy(sizePolicy)
        self.pushButton_divide.setStyleSheet(u"QPushButton{\n"
"font: 75 36pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(255, 73, 170);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 235, 255);\n"
"	color: rgb(255, 112, 181);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_divide, 1, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(173, 173, 173);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_potentiation = QPushButton(self.centralwidget)
        self.pushButton_potentiation.setObjectName(u"pushButton_potentiation")
        sizePolicy.setHeightForWidth(self.pushButton_potentiation.sizePolicy().hasHeightForWidth())
        self.pushButton_potentiation.setSizePolicy(sizePolicy)
        self.pushButton_potentiation.setStyleSheet(u"QPushButton{\n"
"font: 75 36pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(255, 73, 170);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 235, 255);\n"
"	color: rgb(255, 112, 181);\n"
"}\n"
"	")

        self.gridLayout.addWidget(self.pushButton_potentiation, 1, 2, 1, 1)

        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"		background-color: rgb(255, 140, 211);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_delete, 1, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(173, 173, 173);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(173, 173, 173);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(173, 173, 173);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(173, 173, 173);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_multiply = QPushButton(self.centralwidget)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        sizePolicy.setHeightForWidth(self.pushButton_multiply.sizePolicy().hasHeightForWidth())
        self.pushButton_multiply.setSizePolicy(sizePolicy)
        self.pushButton_multiply.setStyleSheet(u"QPushButton{\n"
"font: 75 36pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(255, 73, 170);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 235, 255);\n"
"	color: rgb(255, 112, 181);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_multiply, 2, 3, 1, 1)

        self.pushButton_equals = QPushButton(self.centralwidget)
        self.pushButton_equals.setObjectName(u"pushButton_equals")
        sizePolicy.setHeightForWidth(self.pushButton_equals.sizePolicy().hasHeightForWidth())
        self.pushButton_equals.setSizePolicy(sizePolicy)
        self.pushButton_equals.setStyleSheet(u"QPushButton{\n"
"font: 75 36pt \"MS ShellL Dlg 2\";\n"
"	\n"
"	background-color: rgb(255, 140, 211);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 235, 255);\n"
"	color: rgb(255, 112, 181);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_equals, 5, 3, 1, 1)

        self.pushButton_0 = QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        self.pushButton_0.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(173, 173, 173);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(79, 79, 79);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_0, 5, 1, 1, 1)

        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setStyleSheet(u"QPushButton{\n"
"font: 75 36pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(255, 73, 170);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 235, 255);\n"
"	color: rgb(255, 112, 181);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_add, 4, 3, 1, 1)

        self.pushButton_dot = QPushButton(self.centralwidget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_dot.sizePolicy().hasHeightForWidth())
        self.pushButton_dot.setSizePolicy(sizePolicy1)
        self.pushButton_dot.setStyleSheet(u"QPushButton{\n"
"font: 75 36pt \"MS ShellL Dlg 2\";\n"
"	background-color: rgb(255, 73, 170);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	background-color: rgb(255, 235, 255);\n"
"	color: rgb(255, 112, 181);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_dot, 5, 2, 1, 1)

        self.visor = QLabel(self.centralwidget)
        self.visor.setObjectName(u"visor")
        sizePolicy.setHeightForWidth(self.visor.sizePolicy().hasHeightForWidth())
        self.visor.setSizePolicy(sizePolicy)
        self.visor.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.visor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.visor, 0, 0, 1, 4)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 469, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_subtract.setText(QCoreApplication.translate("MainWindow", u"\u2013", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_potentiation.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.pushButton_equals.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.visor.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

