from pymongo import MongoClient
from Sample.Conf.ServerConf import MONGO_DB_HOST, MONGO_DB_PORT, MONGO_DB_USER, MONGO_DB_PASSWORD
from Sample.Utils.singleton import singleton
from Sample.Conf.ServerConf import MONGO_DB_NAME
from bson.json_util import dumps

@singleton
class MongoDataStore():
    def __init__(self) -> None:
        self.__dbHost = MONGO_DB_HOST
        self.__dbPort = MONGO_DB_PORT
        self.__dbUserName = MONGO_DB_USER
        self.__dbPassword = MONGO_DB_PASSWORD
        self.__dbName = MONGO_DB_NAME
        self.__dbClient = None
        self.__DB = None

    def ConnectToDatabase(self):
        try:
            # f"mongodb://{self.__dbUserName}:{self.__dbPassword}@{self.__dbHost}:{self.__dbPort}/"
            connectionString = None

            if self.__dbUserName and self.__dbPassword:
                connectionString = f"mongodb://{self.__dbUserName}:{self.__dbPassword}@{self.__dbHost}:{self.__dbPort}/"
            else:
                connectionString = f"mongodb://{self.__dbHost}:{self.__dbPort}/"
            self.__dbClient = MongoClient(connectionString)
            
            self.__DB = self.__dbClient[self.__dbName]
            print("Successfully Connected to database")
            # return self.__dbClient
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise e

    def AddStudent(self, student):
        studentCollection = self.__DB.students
        studentCollection.insert_one(student)
        print("Student added successfully")

    def GetAllStudents(self):
        studentCollection = self.__DB.students
        allStudents = list(studentCollection.find())
        return dumps(allStudents)

