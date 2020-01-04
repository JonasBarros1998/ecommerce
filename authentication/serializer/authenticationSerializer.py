from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class AuthenticationSerializer(ModelSerializer): 
    class Meta: 
        model = User
        fields = [
            'id',
            'username'
        ]