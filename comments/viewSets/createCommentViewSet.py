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

    """
        Função para pegar o nome do usuario, realizando 
    uma consulta no banco atraves do ID do usuario, 
    provindo do localStorage do navegador do usuario
    """
    def searchUser(self, userId):
        user = User.objects.get(id=userId)
        first_name = user.first_name
        last_name = user.last_name
        return f'{first_name} {last_name}'

    def create(self, request, *args, **kwargs):
       
        nameUser = self.searchUser(request.data['user_id'])

        comments = Comments(
            name = nameUser,
            comment = request.data["comment"],
            avaliation = request.data['avaliation'])
        comments.save()

        comments.product.add(request.data["product"])
        return Response({"response": request.data})
