from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope

from djangoQuerySet.djangoQuerySet import djangoQuerySet

from products.models import SmartWatch
from products.categories.smartWatch.serializer.smartWatchSerializer import SmartWatchSerializer

class SmartWathViewSet(ModelViewSet):

    serializer_class = SmartWatchSerializer
    Model = SmartWatch

    def __init__(self):
        self.__djangoQuerySet = djangoQuerySet()
        
    def list(self, request=None):
        serializer = self.__djangoQuerySet.listFull(
            self.Model, self.serializer_class)
        return Response(serializer, status=status.HTTP_200_OK)

    def findOne(self, request, smart_watch_ids):
        serializer = self.__djangoQuerySet.filterOne(
            smart_watch_ids, self.Model, self.serializer_class)
        return Response(serializer, status=status.HTTP_200_OK)

    def findMakeAll(self, request, smart_watch_make):
        queryset = self.Model.objects.filter(products__make=smart_watch_make)
        smartWatch = self.__djangoQuerySet.querySetSerializer(
            queryset, SmartWatchSerializer)
        return Response(smartWatch, status=status.HTTP_200_OK)
