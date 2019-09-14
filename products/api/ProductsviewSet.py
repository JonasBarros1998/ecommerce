from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .productsSerializer import ProductsSerializer
from products.models import Products

class ProductsViewSet(ModelViewSet):

    def listProducts(self, request):

        products = Products.objects.all()
        productsSerializer = ProductsSerializer(products, many=True)
    
        return Response(productsSerializer.data) 

    def findOne(self, request, id):

        product = Products.objects.filter(id = id)
        productSerializer = ProductsSerializer(product, many=True)

        return Response(productSerializer.data)


