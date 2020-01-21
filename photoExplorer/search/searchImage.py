from pymongo import MongoClient
from ..errors.IAuthenticationMongoDb import IAuthenticationMongoDb

class SearchImages(IAuthenticationMongoDb):

    def __init__(self):
        super().__init__()
        self.authentication()

    def authentication(self):
        super().authentication()
    
    def FindOne(self, database, collection, values):
        mongoClient = MongoClient(username = "jonas", password = "jonas-179406")
        database = mongoClient[database]
        collection = database[collection]
        OneLinkImage = collection.find_one(values)
        if(OneLinkImage == None):
            result = {
                "status":"empty database"
            }
            return result
        else: 
            return OneLinkImage

    def FindMany(self, database, collection):
        mongoClient = MongoClient(username = "jonas", password = "jonas-179406")
        database = mongoClient[database]
        collection = database[collection]
        listLinkImages = collection.find()
        return listLinkImages