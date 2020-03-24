# Arquivo specifico para edição de algum dado em uma collectio do mongodb
from utilities.mongodb.config.mongodb_config import MongodbConfig
from bson.objectid import ObjectId

class Update:
    def __init__(self):
        self.mongodb_config = MongodbConfig()

    def find_one_and_update(self, database: str, collection: str, find: dict, data_update: dict):
        """
        Método para pesquisar e adicionar alguma dado em uma collection

        `databse` Nome da base de dados, criada no mongo.

        `collection` Nome da collection criada no mongodb.

        `find` Um dict com  o item a ser consultado.

        `data_update` Os dados a serem adicionados na colecao.
        """

        mongo_client = self.mongodb_config.auth()
        database = mongo_client[database]
        collection = database[collection]

        datas_updating = collection.find_one_and_update(find, data_update, upsert=True)
        return datas_updating

    def _valid_credentials(self):
        return self.mongodb_config.valid_credentials()
