from utilities.mongodb.config.mongodb_config import MongodbConfig

class ListingCollection:
    def __init__(self):
        self.mongodb_config = MongodbConfig()
        self.mongo_client = self.mongodb_config.auth()
    
    def search_all(self, database, collection):
        database = self.mongo_client[database]
        collection = database[collection]
        search_collection_all = collection.find()
        return search_collection_all
    
    def search_one(self, database, collection, data):
        database = self.mongo_client[database]
        collection = database[collection]
        search_collection = collection.find_one(data)
        return search_collection
