from rest_framework.viewsets import ModelViewSet 
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasResourceScope, OAuth2Authentication, TokenHasScope
from rest_framework import status

class ValidatorTokenViewSet(ModelViewSet): 
    authentication_classes = [OAuth2Authentication, 
                              SessionAuthentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read'] 
    
    def __init__(self):
        super().__init__()
    
    def validator(self, request):
        return Response({"status": status.HTTP_200_OK}, status=status.HTTP_200_OK)

