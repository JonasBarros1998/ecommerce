from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import FileUploadParser

from products.models import Cftv, Product
from ..serializer.CftvSerializer import CftvSerializer
from djangoQuerySet.djangoQuerySet import djangoQuerySet

class CftvViewSet(ModelViewSet):

    serializer_class = CftvSerializer             
    model = Cftv
    parser_class = [FileUploadParser]

    def __init__(self):
        self.__djangoQuerySet = djangoQuerySet() 

    def create(self, request,  *args, **kwargs):

        print(request.data)
        
        product = Product(
            mediaOne = request.data["mediaOne"],
            mediaTwo = request.data["mediaTwo"]
        )
        product.save()

        return Response({"status":"OK"}, status = status.HTTP_201_CREATED)
    
    def list(self, request = None, *args, **kwargs):

        cftvSerializer = self.__djangoQuerySet.listFull(self.model, self.serializer_class)
        return Response(cftvSerializer, status = status.HTTP_200_OK)

    def findOne(self, request, ids):

        cftvSerializer  = self.__djangoQuerySet.filterOne(ids, self.model, CftvSerializer)
        return Response(cftvSerializer, status = status.HTTP_200_OK)

    def findPrice(self, request, price):

        cftvSerializer = self.__djangoQuerySet.filterPrice(price, self.model, CftvSerializer)
        return Response(cftvSerializer, status = status.HTTP_200_OK)
    
    def findMake(self, request, make):

        cftvSerializer = self.__djangoQuerySet.filterString(make, self.model, CftvSerializer)
        return Response(cftvSerializer, status = status.HTTP_200_OK)