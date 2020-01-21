import os
from pathlib import Path
from dotenv import load_dotenv
from abc import ABC, abstractmethod

load_dotenv()
env_path = Path('.') / '.env'

class IAuthenticationMongoDb(ABC):

    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def authentication(self):
        usernameMongoDb = os.getenv('MONGO_INITDB_ROOT_USERNAME')
        passwordMongoDb = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
        if(usernameMongoDb == None):
            raise TypeError(
                f'''usernameMongoDb = {usernameMongoDb} |
                usernameMongoDb é um valor nulo, 
                configure seu arquivo .env, com usernameMongoDb do mongodb''')
        elif(passwordMongoDb == None):
            raise TypeError(
                f'''MONGO_INITDB_ROOT_PASSWORD = {passwordMongoDb} |
                MONGO_INITDB_ROOT_PASSWORD é um valor nulo, 
                configure seu arquivo .env, com MONGO_INITDB_ROOT_PASSWORD do mongodb''')
        else:
            return True