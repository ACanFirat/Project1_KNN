# -*- coding: utf-8 -*-


import sys
sys.path.append('C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\CRUD')
from PyQt5 import QtCore, QtGui, QtWidgets
from Main import PersonDB


class Ui_DeleteWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(290, 102)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 250, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.comboBox)
        self.iDLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.iDLineEdit.setObjectName("iDLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.iDLineEdit)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.sendDelete)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ID"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Pregnancies"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Glucose"))
        self.comboBox.setItemText(3, _translate("MainWindow", "BloodPressure"))
        self.comboBox.setItemText(4, _translate("MainWindow", "SkinThickness"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Insulin"))
        self.comboBox.setItemText(6, _translate("MainWindow", "BMI"))
        self.comboBox.setItemText(7, _translate("MainWindow", "DiabetesPedigreeFunction"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Age"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Outcome"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))

    def sendDelete(self):
        text=self.comboBox.currentText()
        id=int(self.iDLineEdit.text())
        database=PersonDB()
        database.Delete(text,id)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DeleteWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
