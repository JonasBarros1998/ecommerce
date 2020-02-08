from rest_framework.serializers import ModelSerializer
from products.models import SmartWatch
from products.api.productsSerializer import ProductsSerializer
from products.models import Product

class SmartWatchSerializer(ModelSerializer):

    products = ProductsSerializer(Product, many=False, read_only=True)

    class Meta:
        
        model = SmartWatch

        fields = [
            'id',
            'waterProof',
            'color', 
            'heartRate',
            'products'
        ]