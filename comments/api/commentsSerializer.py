from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, StringRelatedField
from rest_framework import serializers
from rest_framework.settings import api_settings

from products.models import Product, Cftv

from products.api.productsSerializer import ProductsSerializer
from comments.models import Comments
#from Users.api.userSerializer import userSerializer
from django.contrib.auth.models import User

class CommentsSerializer(ModelSerializer):

    #user = userSerializer(read_only=True)
    product = ProductsSerializer(read_only=True, many=True)

    class Meta:
        model = Comments

        fields = [
            'id',
            'product',
            'comment',
            'avaliation',
            'date'
        ]


class CommentsProductsSerializer(ModelSerializer):

    class Meta:
        model = Comments

        fields = [
            'id',
            'comment',
            'avaliation',
            'date'
        ]

    
    
