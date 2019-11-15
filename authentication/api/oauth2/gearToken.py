from oauth2_provider.views.mixins import OAuthLibMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import QueryDict
from rest_framework import status

class GearToken(ModelViewSet, OAuthLibMixin):

    def __init__(self):
        super()
    
    def token(self, request):

        requestToken = self.create_token_response(request)
        return Response(requestToken, status=status.HTTP_201_CREATED)


        """
    def searchUser(self, request):

        dictQuerySet = request.data
        copyDict = dictQuerySet.copy()
        converDict = copyDict.dict()
        dictKeys = converDict.keys()
        convertDictForList = list(dictKeys)
        #Capturar o primeiro valor do array
        dictValue = convertDictForList[0]
        convertForDict = json.loads(dictValue)
        userEmail = convertForDict['email']
        emailExist = User.objects.filter(email = userEmail).exists()

        if(emailExist):
            nameUser = User.objects.filter(email = userEmail) 
            convertForDict['email'] = str(nameUser[0])
            
            request.data = __class__
            print(request.data)

        #self.oauthLibMixin.create_token_response(request)
        """

"""
{'client_id': 'X5YPhQN6rRe1UH71FDi9IjKrWUoeC2osFwcuvJkz', 
'client_secret': 'imBlF1QjQgqwIG3PjpLnbMJEue8fUs3KgeP0GNuy4JYFBofFsBnW0ldRzqK0grEtFX86EMXSBtwd9MH5Eti8ulMvjJ55aU4IOug36UBjW4G6V2yNMas49Yeumr9oX3kx', 
'email': 'jonas_barros@outlook.com', 
'password': 'code2798', 
'grant_type': 'password'}
"""

    


