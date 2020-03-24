"""
Modulo especifico para cadastro  e listagem de produtos.
"""

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from .productsSerializer import ProductsSerializer, ProductsSerializerMake, ProductsSerializerCategories
from products.models import Cftv, SmartWatch, AirPhones, Product

from djangoQuerySet.djangoQuerySet import djangoQuerySet
from utilities.Erors.settingsCategories.settingsCategoriesErros import CategoriesError
from utilities.ProductsCategories.categoriesSettings import AllCategories
from django.core.paginator import Paginator
from ..utils.params import Params

class ProductsViewSet(ModelViewSet):
    Model = Product
    serializer_class = ProductsSerializer
    # authentication_classes = [OAuth2Authentication, SessionAuthentication]
    # permission_classes = [TokenHasReadWriteScope]

    def __init__(self):
        self.__djangoQuerySet = djangoQuerySet()
        self._products = Product.objects.all()
        self._params = Params()

    def create(self, request, *args, **kwargs):
        productsSerializer = self.get_serializer(data=request.data)
        productsSerializer.is_valid(raise_exception=True)
        self.perform_create(productsSerializer)
        return Response(productsSerializer.data, status=status.HTTP_201_CREATED)

    # Listar todos os produtos cadastrados
    def list(self, request):
        response = self.__djangoQuerySet.listFull(self.Model, self.serializer_class)
        return Response(response, status = status.HTTP_200_OK)

    # Metodo para filtrar todas as marcas vendidas no ecommerce
    def findMakeAll(self, request):
        urlComplet = request.build_absolute_uri()
        urlComplet = urlComplet.lower()
        searchValue = urlComplet.find("true")

        # Retorna toda a listagem de marcas, sem marcas repetidas
        if(searchValue != -1):
            product = self.__djangoQuerySet.filterColumn(
                "make", self.Model, ProductsSerializerMake, repeat=True, many=True)
            return Response(product, status=status.HTTP_200_OK)

        # Retorna todas as marcas, pode ser que tenha marcas repetidas
        else:
            product = self.__djangoQuerySet.filterColumn(
                "make", self.Model, ProductsSerializerMake, many=True)
            return Response(product, status=status.HTTP_200_OK)

    # Retornar os produtos, apartir da marca
    def findOneMake(self, request, make):
        queryset = self.Model.objects.filter(make=make)
        serializer = ProductsSerializer(queryset, many=True, read_only=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def findCategoriesAll(self, request):
        categorie = self.__djangoQuerySet.filterColumn(
            'categorie', self.Model, ProductsSerializerCategories)
        return Response(categorie, status=status.HTTP_200_OK)

    def findOneCategories(self, request, categories):
        categories = categories.lower()
        queryset = self.Model.objects.filter(categorie=categories)
        response = ProductsSerializer(queryset, many=True, read_only=False)
        serializer = response.data
        return Response(serializer, status=status.HTTP_200_OK)