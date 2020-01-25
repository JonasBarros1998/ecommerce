import os
from dotenv import load_dotenv
from pathlib import Path
from pymongo import MongoClient
from .errorsMongoDb import ErrorsMongoDb
from ..errors.IAuthenticationMongoDb import IAuthenticationMongoDb

# Configurações do dotenv
load_dotenv()
env_path = Path('.') / '.env'

class InsertImages(IAuthenticationMongoDb, ErrorsMongoDb):

    def __init__(self):
        super().__init__()
        self.authentication()

    # Verificar a login e senha do usuario
    def authentication(self):
        super().authentication()

    # Validar os dados do usuario
    def invalidData(self, datas):
        super().invalidData(datas)

    # Fazer login no banco de dados
    def config(self):
        mongoUsername = os.getenv('MONGO_INITDB_ROOT_USERNAME')
        mongoPassword = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
        mongoClient = MongoClient(host="ecommerce-mongodb", port=27017,
                                        username=mongoUsername,
                                        password=mongoPassword, )
        return mongoClient

    # Inserir o link das imagen com um dict
    def insert(self, database: str, collection: str, datas: "dict or array"):
        """
            Método para inserir o link das imagens dentro de uma coleção no mongodb. 
            Parametros: 

            `database`: "Nome da base de dados, criada no mongo"
            `collection`: "Nome da collection criada no mongodb"
            `datas`: "dict ou um array de objetos"
        """
        self.invalidData(datas)
        if(type(datas) == dict):
            return self._InsertOneImages(database, collection, datas)
        elif(type(datas) == list):
            return self._InsertManyImages(database, collection, datas)

    # Inserir o link das imagens com um array de objetos
    def _InsertOneImages(self, database, collection, datas):
        try:
            mongoClient = self.config()
            database = mongoClient[database]
            collection = database[collection]
            collection.insert_one(datas)
            status = {
                "result": "save sucefully"
            }
            return status
        except:
            raise ValueError(
                f"Um errro ocorreu, e não foi possível salvar os dados")

    def _InsertManyImages(self, database, collection, datas):
        try:
            mongoClient = self.config()
            database = mongoClient[database]
            collection = database[collection]
            collection.insert_many(datas)
            result = {
                "status": "save sucefully"
            }
            return result
        except: 
            raise ValueError(
                f"Um errro ocorreu, e não foi possível salvar os dados")