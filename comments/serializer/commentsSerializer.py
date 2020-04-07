from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, StringRelatedField
from rest_framework import serializers
from rest_framework.settings import api_settings

from products.models import Product, Cftv

from products.api.productsSerializer import PrductsSerializerId
from comments.models import Comments
from authentication.serializer.authenticationSerializer import AuthenticationSerializer
from django.contrib.auth.models import User

class CommentsSerializer(ModelSerializer):

    product = PrductsSerializerId(read_only = True, many = True)
    
    class Meta:
        model = Comments
        fields = [
            'product',
            'comment',
            'avaliation',
            'date',
            'name']


