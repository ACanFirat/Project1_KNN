import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class KNN():

    
    cnx = sqlite3.connect('diabetes.db')

    data = pd.read_sql_query("SELECT * FROM diabetes", cnx)
    
    diabetes_patients = data[data.Outcome == 1]
    healthy_patients = data[data.Outcome == 0]
    knn = KNeighborsClassifier(n_neighbors = 11) 


    def prepare(self):
        self.data = pd.read_sql_query("SELECT * FROM diabetes", self.cnx)
        self.diabetes_patients = self.data[self.data.Outcome == 1]
        self.healthy_patients = self.data[self.data.Outcome == 0]

        y = self.data.Outcome.values
        x_ham_veri = self.data.drop(["Outcome"],axis=1)
        x_ham_veri = x_ham_veri.drop(["ID"],axis=1) 



        x = (x_ham_veri - np.min(x_ham_veri))/(np.max(x_ham_veri)-np.min(x_ham_veri))



        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.33,random_state=1)
        print(type(x_train))

        
        self.knn.fit(x_train,y_train)
        #prediction = self.knn.predict(x_test)
        
        return 1 
        
        

    def predict(self,pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,dpf,age):

        x_df=pd.DataFrame(np.array([pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,dpf,age]))
        print(x_df.shape)
        x = (x_df - np.min(x_df))/(np.max(x_df)-np.min(x_df))
        x=np.transpose(x)


        new_prediction = self.knn.predict(x)
        return int(new_prediction)

    def gr_plot(self):
        plt.scatter(self.healthy_patients.Age, self.healthy_patients.Glucose, color="green", label="Healthy", alpha = 0.4)
        plt.scatter(self.diabetes_patients.Age, self.diabetes_patients.Glucose, color="red", label="Diabetes Patients", alpha = 0.4)
        plt.xlabel("Age")
        plt.ylabel("Glucose")
        plt.legend()
        plt.show()


    




