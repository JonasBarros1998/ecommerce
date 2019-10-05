from rest_framework.response import Response
from rest_framework import status

class codeCreate:
    def __init__(self, Model, manyToMany = False):
        self.__Model = Model
        self.__many = manyToMany 

    def createObject(self, dataRequest = None, *args):

        if(self.__many == True):
            return self.manyToMany()
        else:
            model = self.__Model()
            data = dataRequest.data
            self.__Model.objects.create(model.__dict__.values())

            return Response(data = data, status = status.HTTP_201_CREATED)           

    def manyToMany(self, fieldMany = None, field = None, *args):

        model = self.__Model.objects.create(args.__dict__.values())
        model.field.add(fieldMany)



