from products.models import Cftv, Product
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status


class CreateCftvViewset(ModelViewSet):
    def __init__(self):
        super().__init__()

    def create(self, request,  *args, **kwargs):

        product = Product(
            name=request.data['products']["title"],
            price=request.data['products']["price"],
            description=request.data['products']['description'],
            fullDescription=request.data['products']['fullDescription'],
            make=request.data['products']["make"],
            model=request.data['products']["model"],
            amount=request.data['products']["amount"],
            especification=request.data['products']['especification'],
            categorie=request.data['products']['categories'],
            media=request.data['products']['media'])
        product.save()

        cftv = Cftv(
            resolution=request.data["resolution"],
            amountCameras=request.data["amountCameras"],
            coaxialCableSize=request.data["coaxialCableSize"],
            products=product)
        cftv.save()

        return Response({"status": "OK"}, status=status.HTTP_201_CREATED)
