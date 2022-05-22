import sys
sys.path.append('C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\CRUD')
from PyQt5 import QtCore, QtGui, QtWidgets
from Main import PersonDB

class Ui_UpdateWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(290, 128)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 250, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.iDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.iDLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.iDLineEdit.setObjectName("iDLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.iDLineEdit)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_17)
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
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.button_condition(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Update"))
        self.iDLabel.setText(_translate("MainWindow", "ID"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Pregnancies"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Glucose"))
        self.comboBox.setItemText(2, _translate("MainWindow", "BloodPressure"))
        self.comboBox.setItemText(3, _translate("MainWindow", "SkinThickness"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Insulin"))
        self.comboBox.setItemText(5, _translate("MainWindow", "BMI"))
        self.comboBox.setItemText(6, _translate("MainWindow", "DiabetesPedigreeFunction"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Age"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Outcome"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))
    
    def button_condition(self,mw):
        self.pushButton.clicked.connect(self.sendUpdate)
        
    
    def sendUpdate(self):
        text=self.comboBox.currentText()
        id=int(self.iDLineEdit.text())
        value=int(self.lineEdit_17.text())
        database=PersonDB()
        database.Update(numara=id,degisken=text,deger=value)
        
        
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_UpdateWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
