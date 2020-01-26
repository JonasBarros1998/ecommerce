from rest_framework.serializers import ModelSerializer

class MainProductSerializer(ModelSerializer):
    class Meta:
        field = [
            "title",
            "price",
            "image",
            "categorie",
            "productId"
        ]

    
