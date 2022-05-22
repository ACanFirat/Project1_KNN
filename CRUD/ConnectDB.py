import sqlite3

class DbTools:
    db = object()
    __dbName = "C:\\Users\\acfir\\Desktop\\Coding\\Artificial Intelligence\\Project1_KNN\\diabetes.db"

    def __init__(self) -> None:
        pass
        
    @staticmethod
    def ConnectDB():
        try:
            global db
            db = sqlite3.connect(DbTools.__dbName)
            print("Connection Successfull!")
        except Exception as error:
            print("Could not connet to database!")
            print(error)
        return db

    @staticmethod
    def DisconnectDB():
        try:
            db.close()
            print("Disconnection Successfull!")
        except Exception as error:
            print("Could not disconnect database!")
            print(error)

if __name__ == "__main__":
    DbTools.ConnectDB()
    DbTools.DisconnectDB()