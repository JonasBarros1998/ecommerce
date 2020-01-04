from rest_framework.serializers import ModelSerializer
from ..models import Comments

class CommentsProductsSerializer(ModelSerializer):

    class Meta:
        model = Comments
        fields = [
            'id',
            'comment',
            'avaliation',
            'date',
            'name']
