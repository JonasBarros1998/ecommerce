from abc import ABC, abstractclassmethod, abstractmethod

class ErrorsMongoDb(ABC):
    
    @abstractmethod
    def invalidData(self, datas):
        if(type(datas) == dict):
            return True
        elif(type(datas) == list):
            return True
        else:
            raise TypeError(
                f'''Esse é um formato de dados inválidos, 
                Formatos permitidos: array de objetos e dict''')