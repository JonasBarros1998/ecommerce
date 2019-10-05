from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, StringRelatedField
from products.models import Cftv, Product
from rest_framework import serializers
from products.api.productsSerializer import ProductsSerializer

class CftvSerializer(ModelSerializer):

    products = ProductsSerializer(read_only=True)
    product = PrimaryKeyRelatedField(queryset = Product.objects.all(), source="products")

    class Meta:
        model = Cftv
        fields = ["id", "resolution", "amountCameras", "coaxialCableSize","product", "products"]