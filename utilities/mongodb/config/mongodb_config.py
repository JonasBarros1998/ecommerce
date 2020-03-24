"""
Arquivo especifico para a configuração do mongoDb
"""
import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from pathlib import Path
from pymongo import MongoClient
from utilities.mongodb.config.errors.errors_mongodb import ErrorsMongodb

# Configurações do dotenv
load_dotenv()
env_path = Path('.') / '.env'

class MongodbConfig:
    def __init__(self):
        self.errors_mongodb = ErrorsMongodb()

    # @abstractmethod
    def auth(self):
        username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
        password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')

        self._valid_credentials_mongodb(username, password)

        mongo_client = MongoClient(host="ecommerce-mongodb",
                                   port=27017,
                                   username=username,
                                   password=password)

        return mongo_client
    
    #Verifica se as credenciais de username e passoword estão configuradas no arquivo .env
    def _valid_credentials_mongodb(self, username, password):
        return self.errors_mongodb.valid_credentials(username, password)