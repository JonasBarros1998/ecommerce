from rest_framework.serializers import ModelSerializer
from products.models import Products

class ProductsSerializer(ModelSerializer):
    queryset = Products
    fields = ["id", "name", "description"]