from rest_framework.serializers import ModelSerializer
from products.models import Product

class ProductsSerializer(ModelSerializer):

    class Meta:
        
        model = Product
        fields = [
            "id", 
            "title", 
            "price", 
            "fullDescription",
            "description", 
            "make", 
            "model", 
            "amount",
            "especification",
            "categories"]
        
class ProductsSerializerMake(ModelSerializer):

    class Meta:
        model = Product
        fields = ['make']

class ProductsSerializerCategories(ModelSerializer):

    class Meta:
        model = Product
        fields = ['categories']