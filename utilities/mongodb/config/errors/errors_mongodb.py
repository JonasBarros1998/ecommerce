class ErrorsMongodb:
    def __init__(self):
        ...

    def valid_credentials(self, username, password):
        if(username == None):
            raise TypeError("""A variavel de ambiente `MONGO_INITDB_ROOT_USERNAME` 
                    não está configurada  no seu arquivo .env  """)

        elif(password == None):
            raise TypeError(""" A variavel de ambiente `MONGO_INITDB_ROOT_PASSWORD` 
                    não está configurada  no seu arquivo .env """)
        

