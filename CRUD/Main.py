from ConnectDB import DbTools
from CRUD import CRUD
from Personal import Person
from PyQt5 import QtWidgets



class PersonDB(CRUD):

    @staticmethod
    def Create(obj:Person):
        try:
            query = f"INSERT INTO diabetes (Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome) VALUES(?,?,?,?,?,?,?,?,?);"
            db = DbTools.ConnectDB()
            cursor = db.cursor()
            cursor.execute(query,(obj.Pregnancies,obj.Glucose,obj.BloodPressure,obj.SkinThickness,obj.Insulin,obj.BMI,obj.DPF,obj.Age,obj.Outcome))
            db.commit()
            print("Insert Done.")
            DbTools.DisconnectDB()

        except Exception as error:
            print("Could not insert person to database!")
            print(error)


    @staticmethod
    def Read(read_window):
        #persons = list()
        personsstr = list()
        try:
            query = "SELECT * FROM diabetes;"
            db = DbTools.ConnectDB()
            cursor = db.cursor()
            cursor.execute(query)
            personsstr = cursor.fetchall()
            print("Read Done.")
            # print(personsstr)
            
        except Exception as error:
            print("Could not read person to database!")
            print(error)
        read_window.tableWidget.setRowCount(len(personsstr))
        i=0
        for person in personsstr:
            # newPerson = Person(id=person[0],pregnancies=person[1],glucose=person[2],bloodpressure=person[3],skinthickness=person[4],insulin=person[5],bmi=person[6],dpf=person[7],age=person[8],outcome=person[9])
            # persons.append(newPerson)
            # print(person)
            for j in range(10):
                read_window.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(person[j])))
            i+=1
            
            
       


    @staticmethod
    def Update(numara,degisken,deger):
        try:
            query = f"UPDATE diabetes SET {degisken}={deger} WHERE ID = {numara};"
            db = DbTools.ConnectDB()
            cursor = db.cursor()
            cursor.execute(query)
            db.commit()
            print("Update Successfull!")
            DbTools.DisconnectDB()
        except Exception as error:
            print("Could not update")
            print(error)

    @staticmethod
    def Delete(cond,val):
        try:
            query = f"DELETE FROM diabetes WHERE {cond}={val};"
            db = DbTools.ConnectDB()
            cursor = db.cursor()
            cursor.execute(query)
            db.commit()
            DbTools.DisconnectDB()
        except Exception as error:
            print("Could not delete!")
            print(error)

if __name__ == "__main__":
    
    
    #CREATE ETMEK İÇİN!
    #newPerson = Person(pregnancies=0,glucose=0,bloodpressure=0,skinthickness=0,insulin=0,bmi=0,dpf=0,age=0,outcome=0)
    #PersonDB.Create(newPerson)


    #READ etmek için!
    listPersons = PersonDB.Read()


    # UPDATE İÇİN!!
    #PersonDB.Update(6,'SkinThickness',40)

    #DELETE İÇİN
    # selectedPerson = Person(id=5)#5'e eşit olan id'yi sil.
    # selectedPerson = Person(pregnancies=10)#10'a eşit olan pregnancies(ler)'i sil.
    # selectedPerson = Person(age=18)#18'e eşit olan age'i sil.
    # PersonDB.Delete(selectedPerson)
    pass