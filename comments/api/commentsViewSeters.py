from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.authentication import SessionAuthentication

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope, TokenHasReadWriteScope

from djangoQuerySet.djangoQuerySet import djangoQuerySet
from utilities.Code.create.codeCreate import CodeCreate

from comments.models import Comments
from comments.api.commentsSerializer import CommentsSerializer, CommentsProductsSerializer

class CommenstViewSet(ModelViewSet):

    serializer_class = CommentsSerializer  
    Model = Comments

    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [TokenHasReadWriteScope]

    def __init__(self):
        self.__djangoQuerySet = djangoQuerySet()

    def create(self, request, *args, **kwargs):
        
        comments = self.Model(
            user_id = request.data["user"],
            comment = request.data["comments"],
            date = request.data["date"]
            )

        comments.save()

        comments.product.add(
            request.data["product"]
            )
            
        return Response({"response": request.data})
    

    def list(self, request, *args, **kwargs):

        commentSerializer = self.__djangoQuerySet.listFull(self.Model, CommentsSerializer)
        return Response(commentSerializer, status = status.HTTP_200_OK)
    

    def productComments(self, request, id_product):
        
        modelQuerySet = self.Model.objects.filter(product__id = id_product)
        response = self.__djangoQuerySet.querySetSerializer(modelQuerySet, CommentsProductsSerializer, many=True)
        
        return Response(data = response, status=status.HTTP_200_OK)
