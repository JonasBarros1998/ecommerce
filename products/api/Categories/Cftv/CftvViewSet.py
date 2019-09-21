from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from products.models import Cftv
from .CftvSerializer import CftvSerializer

import json

class CftvViewSet(ModelViewSet):

    serializer_class = CftvSerializer                                                                             

    def create(self, request,  *args, **kwargs):
        
        cftvSerializer = self.get_serializer(data = request.data)
        cftvSerializer.is_valid(raise_exception = True)
        self.perform_create(cftvSerializer)

        return Response(cftvSerializer.data, status = status.HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):

        cftv = Cftv.objects.all()
        cftvSerializer = CftvSerializer(cftv, many = True)
        print(f">>>> {cftvSerializer.data}")

        return Response(cftvSerializer.data, status = status.HTTP_200_OK)

    def findOne(self, request, id):

        cftv = Cftv.objects.filter(id = id)
        cftvSerializer = CftvSerializer(cftv, many=True)

        return Response(cftvSerializer.data, status = status.HTTP_200_OK)

    def findPrice(self, request, price):

        price = price.split("ate")
        formatprice = json.dumps(price)
        listPrice = json.loads(formatprice)
        lowerPrice = listPrice[0]
        higherPrice = listPrice[1]
        

        cftv = Cftv.objects.filter(products__price__gte = lowerPrice).filter(products__price__lte = higherPrice)
        cftvSerializer = CftvSerializer(cftv, many=True)

        return Response(cftvSerializer.data, status = status.HTTP_200_OK)
    
    def findMake(self, request, make):
    
        cftv = Cftv.objects.filter(products__make = make)
        cftvSerializer = CftvSerializer(cftv, many=True)

        return Response(cftvSerializer.data, status = status.HTTP_200_OK)