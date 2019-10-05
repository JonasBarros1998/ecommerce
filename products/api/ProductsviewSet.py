from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope

from .productsSerializer import ProductsSerializer
from products.models import Product


class ProductsViewSet(ModelViewSet):

    serializer_class = ProductsSerializer

    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [TokenHasReadWriteScope]

    def create(self, request, *args, **kwargs):

        productsSerializer = self.get_serializer(data = request.data)
        productsSerializer.is_valid(raise_exception = True)
        self.perform_create(productsSerializer)

        return Response(productsSerializer.data, status = status.HTTP_201_CREATED)

    def list(self, request):

        products = Product.objects.all()
        productsSerializer = ProductsSerializer(products, many=True)
    
        return Response(productsSerializer.data, status=status.HTTP_200_OK) 


    def findOneProduct(self, request, id):

        product = Product.objects.filter(id = id)
        productSerializer = ProductsSerializer(product, many=True)

        return Response(productSerializer.data, status = status.HTTP_200_OK)