from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication

from djangoQuerySet.djangoQuerySet import djangoQuerySet

from products.api.Categories.AirPhones.airPhoneSerializer import AirPhoneSerializer
from products.models import AirPhones

class AirPhonesViewSet(ModelViewSet):

    serializer_class = AirPhoneSerializer
    Model = AirPhones

    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [TokenHasReadWriteScope]

    def __init__(self):
        self.__djangoQuerySet = djangoQuerySet()
    
    def create(self, request, *args, **kwargs):

        airPhones = AirPhones(
            waterProof = request.data["waterProof"],
            batery = request.data["batery"],
            products_id = request.data["products"]
        )

        airPhones.save()

        return Response(request.data, status=status.HTTP_201_CREATED) 

    def list(self, request):
        
        serializer = self.__djangoQuerySet.listFull(self.Model, self.serializer_class, many=True)
        return Response(serializer, status = status.HTTP_200_OK)
    
    def findOne(self, request, air_phone_ids):

        serializer = self.__djangoQuerySet.filterOne(air_phone_ids, self.Model, self.serializer_class, many=True)
        return Response(serializer, status = status.HTTP_200_OK)