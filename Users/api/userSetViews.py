from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

class UsersViewSet(ModelViewSet):

    def create(self, request, *args, **kwargs):

        user = {
            "username": request.data["email"],
            "password": request.data["password"]
        }

        User.objects.create_user(
            username = user["username"],
            password=user["password"]
        )

        return Response({"Novo usuario adicionado": user["username"]}, status=status.HTTP_201_CREATED)