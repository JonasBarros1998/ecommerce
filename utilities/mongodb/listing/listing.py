from utilities.mongodb.config.mongodb_config import MongodbConfig


class ListingCollection:
    def __init__(self):
        self.mongodb_config = MongodbConfig()
        self.mongo_client = self.mongodb_config.auth()

    def search_all(self, database, collection):
        """
        Função para listagem de todos os itens cadastrados
        na collection do mongodb

        `database`: nome da database.

        `collection`: nome da collection para fazer a consulta.
        """
        database = self.mongo_client[database]
        collection = database[collection]
        search_collection_all = collection.find()
        return search_collection_all

    def search_indice(self, database, collection, indice):
        """
        Função para listagem de todos os itens cadastrados
        na collection do mongodb

        `database`: nome da database.

        `collection`: nome da collection para fazer a consulta.

        `indice`: dict de consulta para pesquisa
        """
        database = self.mongo_client[database]
        collection = database[collection]
        search_collection_all = collection.find(indice)
        return search_collection_all

    
    def search_one(self, database, collection, data):
        database = self.mongo_client[database]
        collection = database[collection]
        search_collection = collection.find_one(data)
        return search_collection
