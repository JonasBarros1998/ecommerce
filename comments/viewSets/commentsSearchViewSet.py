from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from djangoQuerySet.djangoQuerySet import djangoQuerySet
from ..models import Comments
from ..serializer.commentsSerializer import CommentsSerializer
from ..serializer.commentProductSerializer import CommentsProductsSerializer


class CommentsSearchViewSet(ModelViewSet):

    model = Comments

    def __init__(self):
        super().__init__()
        self.__djangoQuerySet = djangoQuerySet()
    
    #Listar todos os comentarios idependentemente de produtos
    def list(self, request, *args, **kwargs):
        commentSerializer = self.__djangoQuerySet.listFull(
            self.model, CommentsSerializer)
        return Response(commentSerializer, status = status.HTTP_200_OK)
    
    #Listar os comentarios relacionado ao produto
    def productComments(self, request, id_product):
        modelQuerySet = self.model.objects.filter(product__id = id_product)
        response = self.__djangoQuerySet.querySetSerializer(modelQuerySet,
                CommentsProductsSerializer, many = True)
        return Response(data = response, status = status.HTTP_200_OK)
