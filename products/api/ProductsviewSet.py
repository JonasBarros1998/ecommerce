from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope

from .productsSerializer import ProductsSerializer, ProductsSerializerMake, ProductsSerializerCategories

from products.models import Cftv, SmartWatch, AirPhones

from products.models import Product
from djangoQuerySet.djangoQuerySet import djangoQuerySet
from utilities.Erors.settingsCategories.settingsCategoriesErros import CategoriesError
from utilities.ProductsCategories.categoriesSettings import AllCategories 


class ProductsViewSet(ModelViewSet):

    Model = Product
    serializer_class = ProductsSerializer

    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [TokenHasReadWriteScope]

    def __init__(self):
        self.__djangoQuerySet = djangoQuerySet()


    def create(self, request, *args, **kwargs):

        productsSerializer = self.get_serializer(data = request.data)
        productsSerializer.is_valid(raise_exception = True)
        self.perform_create(productsSerializer)

        return Response(productsSerializer.data, status = status.HTTP_201_CREATED)
    
    def findMakeAll(self, request):

        urlComplet = request.build_absolute_uri()
        urlComplet = urlComplet.lower()
        searchValue = urlComplet.find("true")

        if(searchValue != -1):
            product = self.__djangoQuerySet.filterColumn("make", self.Model, ProductsSerializerMake, repeat=True, many=True)
            return Response(product, status = status.HTTP_200_OK)
        
        else:
            product = self.__djangoQuerySet.filterColumn("make", self.Model, ProductsSerializerMake, many=True)
            return Response(product, status = status.HTTP_200_OK)
    
    def findCategoriesAll(self, request):

        categories = self.__djangoQuerySet.filterColumn('categories', self.Model, ProductsSerializerCategories)
        return Response(categories, status = status.HTTP_200_OK)
    
    def findOneCategories(self, request, categories):

        categories = categories.lower()
        response = AllCategories().methodsCategories(categories)
        serializer = response.data

        return Response(serializer, status=status.HTTP_200_OK)
    
    def classification(self, request, order):
        pass 
    


