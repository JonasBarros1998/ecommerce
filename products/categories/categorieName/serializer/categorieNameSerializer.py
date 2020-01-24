from rest_framework.serializers import ModelSerializer
class CategorieNameSerializer(ModelSerializer):
    class Meta:
        fields = [
            'title',
            'link'
        ]