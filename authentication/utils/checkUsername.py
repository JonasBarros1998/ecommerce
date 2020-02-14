from django.contrib.auth.models import User

class CheckUsername:
    def __init__(self, ):
        ...
    
    def checkUser(self, username:str):
        """
        Funçao para verificar a existencia do usuario dentro da base de dados

        Parametros: 

        `username`: Nome do usuario a ser consultado
        """ 
        userExist = User.objects.filter(username = username).exists()

        if(not userExist):
            return False
        else:
            return True
    
