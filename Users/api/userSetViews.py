from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

class UsersViewSet(ModelViewSet):

    def verifield(self, request):

        email = request.data['email']
        email = email.lower()

        #verifica se o email do usuario existe.
        user = User.objects.filter(username = email).exists()

        if(user == True):
            return Response({"mensage": "email exists"}, status = status.HTTP_409_CONFLICT)
        
        else:
            return Response({"mensage": "email approved"}, status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        user = {
            "username": request.data["email"].lower(),
            "password": request.data["password"]
        }

        User.objects.create_user(
            username = user["username"],
            password=user["password"]
        )

        return Response({"Novo usuario adicionado": user["username"]}, status=status.HTTP_201_CREATED)