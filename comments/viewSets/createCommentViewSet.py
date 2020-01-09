from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope

from comments.models import Comments

class CreateCommentViewSet(ModelViewSet):

    authentication_classes = [OAuth2Authentication, 
                              SessionAuthentication]
                              
    permission_classes = [TokenHasReadWriteScope]

    def __init__(self):
        ...

    """Adicionar um novo comentario, para isso o usuario 
    tem que estar autenticado"""
    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.data['user_id'])
        first_name = user.first_name
        last_name = user.last_name
        name = f'{first_name} {last_name}'

        comments = Comments(
            comment=request.data["comments"],
            name=name)
        comments.save()

        comments.product.add(request.data["product"])
        return Response({"response": request.data})
