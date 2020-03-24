from utilities.mongodb.config.mongodb_config import MongodbConfig

class ListingCollection:
    def __init__(self):
        self.mongodb_config = MongodbConfig()
    
    def search_all(self, database, collection):
        mongo_client = self.mongodb_config.auth()
        database = mongo_client[database]
        collection = database[collection]
        search_collection_all = collection.find()
        return search_collection_all



    

