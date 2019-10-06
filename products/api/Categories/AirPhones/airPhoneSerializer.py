from rest_framework.serializers import ModelSerializer
from products.models import AirPhones
from products.api.productsSerializer import ProductsSerializer

class AirPhoneSerializer(ModelSerializer):

    products = ProductsSerializer(read_only=True, many=False) 
    
    class Meta:
        
        model = AirPhones

        fields = [
            'id',
            'waterProof',
            'batery',
            'products'
        ]