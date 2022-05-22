import sys
sys.path.append('C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\Gui')
sys.path.append('C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\CRUD')
from PyQt5 import QtCore, QtGui, QtWidgets
from CRUD_CREATE import Ui_CreateWindow
from CRUD_READ import Ui_ReadWindow
from CRUD_DELETE import Ui_DeleteWindow
from CRUD_UPDATE import Ui_UpdateWindow
from CRUD_PREDICT import Ui_PredictWindow
from Main import PersonDB
from KNN import KNN


class Ui_MainWindow(object):
    cond=0
    def OpenCreate(self):
        self.label_3.setText("Data is not trained!")
        self.window=QtWidgets.QMainWindow()
        self.window.setWindowIcon(QtGui.QIcon('C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\acf.jpg'))
        self.ui=Ui_CreateWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def OpenUpdate(self):
        self.label_3.setText("Data is not trained!")
        self.window=QtWidgets.QMainWindow()
        self.window.setWindowIcon(QtGui.QIcon('C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\acf.jpg'))
        self.ui=Ui_UpdateWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def OpenDelete(self):
        self.label_3.setText("Data is not trained!")
        self.window=QtWidgets.QMainWindow()
        self.window.setWindowIcon(QtGui.QIcon('C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\acf.jpg'))
        self.ui=Ui_DeleteWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def OpenRead(self):
        self.window=QtWidgets.QMainWindow()
        self.window.setWindowIcon(QtGui.QIcon('C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\acf.jpg'))
        self.ui=Ui_ReadWindow()
        self.ui.setupUi(self.window)
        dbb.Read(self.ui)
        self.window.show()

    def OpenPredict(self):
        self.window=QtWidgets.QMainWindow()
        self.window.setWindowIcon(QtGui.QIcon('C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\acf.jpg'))
        self.ui=Ui_PredictWindow()
        self.ui.setupUi(self.window,patient)
        self.window.show()

    def text_label(self):
        cond=patient.prepare()
        if cond==1:
            self.label_3.setText("Data is trained!")
        else:
            self.label_3.setText("Data is not trained!")

    


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Diabetes Model")
        MainWindow.setEnabled(True)
        MainWindow.resize(392, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 374, 189))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CreateButton = QtWidgets.QPushButton(self.widget)
        self.CreateButton.setObjectName("CreateButton")
        self.gridLayout_2.addWidget(self.CreateButton, 2, 3, 1, 1)
        self.UpdateButton = QtWidgets.QPushButton(self.widget)
        self.UpdateButton.setObjectName("UpdateButton")
        self.gridLayout_2.addWidget(self.UpdateButton, 4, 3, 1, 1)
        self.ReadButton = QtWidgets.QPushButton(self.widget)
        self.ReadButton.setObjectName("ReadButton")
        self.gridLayout_2.addWidget(self.ReadButton, 5, 3, 1, 1)
        self.DeleteButton = QtWidgets.QPushButton(self.widget)
        self.DeleteButton.setObjectName("DeleteButton")
        self.gridLayout_2.addWidget(self.DeleteButton, 6, 3, 1, 1)
        self.TrainButton = QtWidgets.QPushButton(self.widget)
        self.TrainButton.setObjectName("TrainButton")
        self.gridLayout_2.addWidget(self.TrainButton, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.GraphButton = QtWidgets.QPushButton(self.widget)
        self.GraphButton.setObjectName("GraphButton")
        self.gridLayout_2.addWidget(self.GraphButton, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.PredictButton = QtWidgets.QPushButton(self.widget)
        self.PredictButton.setObjectName("PredictButton")
        self.gridLayout_2.addWidget(self.PredictButton, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.CreateButton.clicked.connect(self.OpenCreate)
        self.UpdateButton.clicked.connect(self.OpenUpdate)
        self.DeleteButton.clicked.connect(self.OpenDelete)
        self.ReadButton.clicked.connect(self.OpenRead)
        self.TrainButton.clicked.connect(self.text_label)
        self.PredictButton.clicked.connect(self.OpenPredict)
        self.GraphButton.clicked.connect(patient.gr_plot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CreateButton.setText(_translate("MainWindow", "Create"))
        self.UpdateButton.setText(_translate("MainWindow", "Update"))
        self.ReadButton.setText(_translate("MainWindow", "Read"))
        self.DeleteButton.setText(_translate("MainWindow", "Delete"))
        self.TrainButton.setText(_translate("MainWindow", "Prepare and Train Data"))
        self.label_2.setText(_translate("MainWindow", "Prediction System:"))
        self.GraphButton.setText(_translate("MainWindow", "Graph"))
        self.label_3.setText(_translate("MainWindow", "Data is not trained!"))
        self.PredictButton.setText(_translate("MainWindow", "Prediction"))
        self.label.setText(_translate("MainWindow", "Database edit:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\acf.jpg'))
    dbb=PersonDB()
    patient=KNN()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    
    MainWindow.show()
    sys.exit(app.exec_())
