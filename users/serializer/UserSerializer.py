from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    model = User
    
    class Meta:

        fields = [
            'username',
            'password'
        ]
        