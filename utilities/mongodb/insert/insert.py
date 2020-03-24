#Arquivo especifico para salvar dados para a collection mongodb

from utilities.mongodb.config.mongodb_config import MongodbConfig

class Insert:
    def __init__(self):
        self.mongodb_config = MongodbConfig()
    
    def insert_item(self, database: str, collection: str, datas: "dict or array"):
        """
        Método para realizar a inserção de novos dados no banco 
        mongodb. 

        Parametros a serem utilizados: 

        `database`: "Nome da base de dados, criada no mongo"

        `collection`: "Nome da collection criada no mongodb"

        `datas`: "dict ou um array de objetos"
        """
        if(type(datas) == dict):
            return self._insert_one(database, collection, datas)
        elif(type(datas) == list):
            return self._insert_many(database, collection, datas)
    
    def _insert_one(self, database, collection, datas):
        mongo_client = self.mongodb_config.auth()
        database = mongo_client[database]
        collection = database[collection]
        response = collection.insert_one(datas)
        return response
    
    def _insert_many(self, datadase, collection, datas):
        mongo_client = self.mongodb_config.auth()
        database = mongo_client[datadase]
        collection = database[collection]
        response = collection.insert_many(datas)
        return response