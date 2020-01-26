from rest_framework.serializers import ModelSerializer

class ProductSpecialSerializer(ModelSerializer):
    class Meta:
        fields = [
            'images',
            'price',
            'pricePromotion'
            'description',
        ]
    