from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication

from djangoQuerySet.djangoQuerySet import djangoQuerySet

from ..serializers.airPhoneSerializer import AirPhoneSerializer
from products.models import AirPhones

class AirphonesViewSet(ModelViewSet):

    serializer_class = AirPhoneSerializer
    Model = AirPhones

    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [TokenHasReadWriteScope]

    def __init__(self):
        self.__djangoQuerySet = djangoQuerySet()

    def list(self, request=None):
        serializer = self.__djangoQuerySet.listFull(
            self.Model, self.serializer_class)
        return Response(serializer, status=status.HTTP_200_OK)

    def findOne(self, request, air_phone_ids):
        serializer = self.__djangoQuerySet.filterOne(
            air_phone_ids, self.Model, self.serializer_class)
        return Response(serializer, status=status.HTTP_200_OK)

    def findMakeAll(self, request, air_phone_make):
        airPhone = self.__djangoQuerySet.filterString(
            air_phone_make, self.Model, self.serializer_class)
        return Response(airPhone, status=status.HTTP_200_OK)
