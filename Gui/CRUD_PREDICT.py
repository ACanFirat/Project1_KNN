# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PredictWindow(object):
    def setupUi(self, MainWindow,ddb):
        self.model=ddb
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(371, 365)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 311, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_17)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_18)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 240, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 280, 160, 20))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.sendCreate)

    

    def sendCreate(self):

            index_1=int(self.lineEdit_17.text())
            index_2=int(self.lineEdit_18.text())
            index_3=int(self.lineEdit_13.text())
            index_4=int(self.lineEdit_16.text())
            index_5=int(self.lineEdit_14.text())
            index_6=float(self.lineEdit_10.text())
            index_7=float(self.lineEdit_12.text())
            index_8=int(self.lineEdit_15.text())
            
            result=self.model.predict(pregnancies=index_1,glucose=index_2,bloodpressure=index_3,skinthickness=index_4,insulin=index_5,bmi=index_6,dpf=index_7,age=index_8)
            if result==1:
                self.label_9.setText("Patient is Diabete")
            else:
                self.label_9.setText("Patient is not Diabete")    
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Pregnancies"))
        self.label_2.setText(_translate("MainWindow", "Glucose"))
        self.label_3.setText(_translate("MainWindow", "BloodPressure"))
        self.label_4.setText(_translate("MainWindow", "SkinThickness"))
        self.label_5.setText(_translate("MainWindow", "Insulin"))
        self.label_6.setText(_translate("MainWindow", "BMI"))
        self.label_7.setText(_translate("MainWindow", "DPF"))
        self.label_8.setText(_translate("MainWindow", "Age"))
        self.pushButton.setText(_translate("MainWindow", "Predict"))
        self.label_9.setText(_translate("MainWindow", "Outcome"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_PredictWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
