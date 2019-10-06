
from .querysetValidate import djangoQuerysetValidate
from rest_framework.response import Response
import json

"""
Todos os modulos da aplicação que consite em salvar, 
editar, deletar e listar, tera qiefazer uso dessa classe.. 

Pra que ela fique totalmente desviculada da aplicação como um tood
é proibido haver algum import de algum modulo dentro dela

Author: Jonas Florencio 
Data: 01/10/2019
Ultima atualização: 01/10/2019
"""

class djangoQuerySet:
    def __init__(self):
        self.__djangoQuerysetValidate = djangoQuerysetValidate()


    def listFull(self, model, classSerializer:"Espera receber uma classe serializadora", 
                               many = True, read_only = False):
        """
        model: Nome da modelagem da aplicação
        classSerializer: Nome do serializador que voce está usado
        many: é aceitavel multiplos vaores
        read_only: Num sei o que é ainda
        """

        self.__instance = hasattr(model, '__name__')

        if(self.__instance == False):
            self.__djangoQuerysetValidate.checkInstance('model', self.__instance)

        else:
            queryset = model.objects.all()

            serializer = classSerializer(queryset, many = many, read_only = read_only)
            
            return serializer.data

    def filterOne(self, ids, model, classSerializer, many=True, read_only = False):
        
        self.__instance = hasattr(model, '__name__')

        if(self.__instance == False): 
            self.__djangoQuerysetValidate.checkInstance('model', self.__instance)

        else:    
            queryset = model.objects.filter(id = ids)
            serializer = classSerializer(queryset, many = many, read_only = read_only)

            return serializer.data
    
    def filterPrice(self, price, model, classSerializer,
                                   many = True, read_only = False):
        
        price = price.split("ate")
        formatePrice = json.dumps(price)
        listPrice = json.loads(formatePrice)

        lowerPrice = listPrice[0]
        higherPrice = listPrice[1]

        queryset = model.objects.filter(products__price__gte = lowerPrice
        ).filter(products__price__lte = higherPrice)
        
        serializer = classSerializer(queryset, many = many, read_only = read_only)

        return serializer.data
    
    def filterMake(self, make, model, classSerializer, many = True, read_only = False):

        self.__instance = hasattr(model, "__name__")

        if(self.__instance == False):
            self.__djangoQuerysetValidate.checkInstance('model', self.__instance)
        
        else:
            queryset = model.objects.filter(products__make = make)
            serializer = classSerializer(queryset, many = many, read_only = read_only)

            return serializer.data
    
    def querySetSerializer(self, queryset, classSerializer, 
                                                many=True, read_only = False):
        
        serializer = classSerializer(queryset, many=many, read_only = read_only)
        return serializer.data
