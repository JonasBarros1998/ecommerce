from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from products.models import Cftv
from ..serializer.CftvSerializer import CftvSerializer
from djangoQuerySet.djangoQuerySet import djangoQuerySet

class CftvViewSet(ModelViewSet):

    model = Cftv
    serializer_class = CftvSerializer

    def __init__(self):
        super().__init__()
        self.__djangoQuerySet = djangoQuerySet()

    def list(self, request=None, *args, **kwargs):
        cftvSerializer = self.__djangoQuerySet.listFull(
            self.model, self.serializer_class)
        return Response(cftvSerializer, status=status.HTTP_200_OK)

    def findOne(self, request, ids):
        filter_queryset = self.model.objects.filter(products_id = ids)
        cftvSerializer = self.__djangoQuerySet.querySetSerializer(filter_queryset, self.serializer_class)
        return Response(cftvSerializer, status=status.HTTP_200_OK)

    def findPrice(self, request, price):
        cftvSerializer = self.__djangoQuerySet.filterPrice(
            price, self.model, CftvSerializer)
        return Response(cftvSerializer, status=status.HTTP_200_OK)

    def findMake(self, request, make):
        cftvSerializer = self.__djangoQuerySet.filterString(
            make, self.model, CftvSerializer)
        return Response(cftvSerializer, status=status.HTTP_200_OK)
