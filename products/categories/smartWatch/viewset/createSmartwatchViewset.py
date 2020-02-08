from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope

from djangoQuerySet.djangoQuerySet import djangoQuerySet

from products.models import SmartWatch, Product

class CreateSmartwatchViewset(ModelViewSet):

    def __init__(self):
        super().__init__()
        self.__djangoQuerySet = djangoQuerySet()

    def create(self, request):

        product = Product(
            title = request.data['products']["title"],
            price = request.data['products']["price"],
            description = request.data['products']['description'],
            fullDescription = request.data['products']['fullDescription'],
            make = request.data['products']["make"],
            model = request.data['products']["model"],
            amount = request.data['products']["amount"],
            especification = request.data['products']['especification'],
            categories = request.data['products']['categories'],
            media = request.data['products']['media'])
        product.save()

        smartWatch = SmartWatch(
            waterProof = request.data["waterProof"],
            color = request.data["color"],
            heartRate = request.data["heartRate"],
            products = product)
        smartWatch.save()

        return Response(request.data, status = status.HTTP_200_OK)
