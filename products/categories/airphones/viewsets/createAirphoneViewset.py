from rest_framework.viewsets import ModelViewSet
from products.models import AirPhones, Product
from rest_framework.response import Response
from rest_framework import status

class CreateAirphoneViewset(ModelViewSet):
    def __init__(self):
        ...
    
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
    
        airPhones = AirPhones(
            waterProof = request.data["waterProof"],
            bateryPhone = request.data["bateryPhone"],
            bateryCase = request.data["bateryCase"],
            voiceControl = request.data["voiceControl"],
            products = product) 
        airPhones.save()
    
        return Response(request.data, status=status.HTTP_201_CREATED)

