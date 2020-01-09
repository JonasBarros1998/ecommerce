from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope

from djangoQuerySet.djangoQuerySet import djangoQuerySet
from ..serializer.authenticationSerializer import AuthenticationSerializer


class AuthenticationViewSet(ModelViewSet):
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [TokenHasReadWriteScope]
    serializer_class = AuthenticationSerializer

    def __init__(self):
        super().__init__()
        self.__djangoQuerySet = djangoQuerySet()

    def searchUserId(self, request):
        queryset = User.objects.filter(username=request.data['username'])
        userQuerySet = self.__djangoQuerySet.querySetSerializer(
            queryset, self.serializer_class)
        return Response({"response": userQuerySet}, status=status.HTTP_202_ACCEPTED)
