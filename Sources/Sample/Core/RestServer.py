from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from Sample.Conf.ServerConf import APP_PORT
from Sample.RestResources.HelloWorld import HelloWorld
from Sample.RestResources.StudentRestResource import StudentRestResource
from Sample.DataStore.MongoDataStore import MongoDataStore
from flask_cors import CORS
class RestServer():
    def __init__(self) -> None:
        self.__RestServer = Flask(__name__)
        # self.__RestServer = 
        self.__RestResources = Api(self.__RestServer)
        self.__RetServerPort = APP_PORT
    

    def StartRestServer(self):
        try:
            self.__PrepareRestResources()
            self.__ConnectToDatabase()
            Swagger(self.__RestServer)
            CORS(self.__RestServer)
            self.__RestServer.run(port=APP_PORT, debug=True)
        except Exception as e:
            print(e)

    
    def __PrepareRestResources(self):
        self.__RestResources.add_resource(HelloWorld, "/hello")
        self.__RestResources.add_resource(StudentRestResource, "/student")
        # self.__RestResources.add_resource(StudentRestResource, "/student")


    def __ConnectToDatabase(self):
        MongoDataStore().ConnectToDatabase()