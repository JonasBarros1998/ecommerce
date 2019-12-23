from rest_framework.serializers import ModelSerializer

class SlidesSerializer(ModelSerializer):
    class Meta:

        fields = [
            'slides'
        ]