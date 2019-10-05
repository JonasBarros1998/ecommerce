from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from products.models import Cftv
from .CftvSerializer import CftvSerializer

from djangoQuerySet.djangoQuerySet import djangoQuerySet
import json

class CftvViewSet(ModelViewSet, djangoQuerySet):

    serializer_class = CftvSerializer             
    model = Cftv

    def __init__(self):
        self.__djangoQuerySet = djangoQuerySet() 

    def create(self, request,  *args, **kwargs):
        
        cftvSerializer = self.get_serializer(data = request.data)
        cftvSerializer.is_valid(raise_exception = True)
        self.perform_create(cftvSerializer)

        return Response(cftvSerializer.data, status = status.HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):

        cftvSerializer = self.__djangoQuerySet.listFull(self.model, CftvSerializer)
        return Response(cftvSerializer, status = status.HTTP_200_OK)

    def findOne(self, request, ids):

        cftvSerializer  = self.__djangoQuerySet.filterOne(ids, self.model, CftvSerializer)
        return Response(cftvSerializer, status = status.HTTP_200_OK)

    def findPrice(self, request, price):

        cftvSerializer = self.__djangoQuerySet.filterPrice(price, self.model, CftvSerializer)
        return Response(cftvSerializer, status = status.HTTP_200_OK)
    
    def findMake(self, request, make):

        cftvSerializer = self.__djangoQuerySet.filterMake(make, self.model, CftvSerializer)
        return Response(cftvSerializer, status = status.HTTP_200_OK)