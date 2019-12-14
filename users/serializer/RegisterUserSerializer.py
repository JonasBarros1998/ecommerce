from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import RegisterUser
from django.contrib.auth.models import User
from .UserSerializer import UserSerializer

class RegisterUserSerializer(ModelSerializer):

    user = UserSerializer(User, many=False, read_only=False)
    class Meta:
        
        model = RegisterUser

        fields = [
            'fullName',
            'birthDate',
            'male',
            'feminine',
            'cpf',
            'smartphone',
            'phone',
            'user'
        ]
