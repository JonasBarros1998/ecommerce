from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.authentication import SessionAuthentication

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope, TokenHasReadWriteScope

from djangoQuerySet.djangoQuerySet import djangoQuerySet

from comments.models import Comments
from ..serializer.commentsSerializer import CommentsSerializer
from ..serializer.commentProductSerializer import CommentsProductsSerializer

from django.contrib.auth.models import User

class CommenstViewSet(ModelViewSet):

    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [TokenHasReadWriteScope]

    serializer_class = CommentsSerializer  
    Model = Comments

    def __init__(self):
        self.__djangoQuerySet = djangoQuerySet()

    def create(self, request, *args, **kwargs):
        
        user = User.objects.get(id=request.data['user_id'])
        first_name = user.first_name
        last_name = user.last_name
        name = f'{first_name} {last_name}' 
        
        comments = Comments(
            comment = request.data["comments"],
            name = name)
        comments.save()

        comments.product.add(request.data["product"])
        return Response({"response": request.data})

    def list(self, request, *args, **kwargs):

        commentSerializer = self.__djangoQuerySet.listFull(self.Model, CommentsSerializer)
        return Response(commentSerializer, status = status.HTTP_200_OK)
    
    def productComments(self, request, id_product):
        
        modelQuerySet = self.Model.objects.filter(product__id = id_product)
        response = self.__djangoQuerySet.querySetSerializer(modelQuerySet, 
                                                            CommentsProductsSerializer, 
                                                            many=True)

        return Response(data = response, status=status.HTTP_200_OK)
