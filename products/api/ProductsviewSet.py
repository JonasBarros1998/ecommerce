from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .productsSerializer import ProductsSerializer
from products.models import Products

class ProductsViewSet(ModelViewSet):

    serializer_class = ProductsSerializer
        
    def create(self, request, *args, **kwargs):

        productsSerializer = self.get_serializer(data = request.data)
        productsSerializer.is_valid(raise_exception = True)
        self.perform_create(productsSerializer)

        return Response(productsSerializer.data, status = status.HTTP_201_CREATED)


    def allProducts(self, request):

        products = Products.objects.all()
        productsSerializer = ProductsSerializer(products, many=True)
    
        return Response(productsSerializer.data, status=status.HTTP_200_OK) 


    def findOneProduct(self, request, id):

        product = Products.objects.filter(id = id)
        productSerializer = ProductsSerializer(product, many=True)

        return Response(productSerializer.data, status = status.HTTP_200_OK)

