from rest_framework.serializers import ModelSerializer
from products.models import Product

class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id", 
            "name", 
            "price", 
            "fullDescription",
            "description", 
            "make", 
            "model", 
            "amount",
            "especification",
            "categorie", 
            "media"]
        
class ProductsSerializerMake(ModelSerializer):
    class Meta:
        model = Product
        fields = ['make']

class ProductsSerializerCategories(ModelSerializer):
    class Meta:
        model = Product
        fields = ['categorie']

class PrductsSerializerId(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']