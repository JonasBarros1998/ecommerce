from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from rest_framework.authentication import SessionAuthentication

from .authenticationSerializer import AuthenticateSerializer

class AuthenticationViewSet(ModelViewSet):
    
    serializer_class = AuthenticateSerializer
    
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [TokenHasReadWriteScope]

    def authenticateUser(self, request):

        user = authenticate(
                email = request.data['email'],
                password = request.data['password']
            )       

        if(user == None):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
           
        else:
            responseUser = {
                "Message": "Logado com sucesso",
                "Username": user
            }
            return Response(responseUser, status=status.HTTP_202_ACCEPTED)
