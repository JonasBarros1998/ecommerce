import os
from dotenv import load_dotenv
from pathlib import Path
from pymongo import MongoClient
from ..errors.IAuthenticationMongoDb import IAuthenticationMongoDb
from ..errors.IAuthenticationMongoDb import IAuthenticationMongoDb

# Configurações do dotenv
load_dotenv()
env_path = Path('.') / '.env'

class SearchImages(IAuthenticationMongoDb):

    def __init__(self):
        super().__init__()
        self.authentication()

    # Verificar se no arquivo .env existe nome e senha de usuario
    def authentication(self):
        super().authentication()

    # Authenticar o usuario
    def config(self):
        mongoUsername = os.getenv('MONGO_INITDB_ROOT_USERNAME')
        mongoPassword = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
        mongoClient = MongoClient(host="ecommerce-mongodb", port=27017,
                                  username=mongoUsername,
                                  password=mongoPassword)
        return mongoClient

    # Fazer a pesquisa por uma unica imagem
    def FindOne(self, database, collection, values):
        mongoClient = self.config()
        database = mongoClient[database]
        collection = database[collection]
        OneLinkImage = collection.find_one(values)
        if(OneLinkImage == None):
            result = {"status": "empty collection"}
            return result
        else:
            for item in OneLinkImage:
                item['_id'] = str(item['_id'])
                return item
                
    # listagem de todas as imagens
    def FindMany(self, database, collection):
        """
        Método para listagram de todos os links das imagens
        paramentros: 

        `database` Nome da dabase do mongo

        `collection` Nome da collection do mongo
        
        """
        listImages = []
        mongoClient = self.config()
        database = mongoClient[database]
        collection = database[collection]
        listLinkImages = collection.find()
        
        if(listLinkImages == None):
            result = {"status": "empty collection"}
            return result
        else:
            for itens in listLinkImages:
                itens['_id'] = str(itens['_id'])
                listImages.append(itens)
            return listImages
