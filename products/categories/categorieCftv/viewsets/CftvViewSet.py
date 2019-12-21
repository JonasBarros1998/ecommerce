from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
import io
from rest_framework.parsers import FileUploadParser

from products.models import Cftv, Product
from ..serializer.CftvSerializer import CftvSerializer
from djangoQuerySet.djangoQuerySet import djangoQuerySet
from _amazon.s3.saveImagesBucket import SaveFileBucket

class CftvViewSet(SaveFileBucket, ModelViewSet):

    serializer_class = CftvSerializer             
    model = Cftv
    parser_class = [FileUploadParser]

    def __init__(self):
        super().__init__()
        self.__djangoQuerySet = djangoQuerySet() 
    
    def requestImages(self, bucket, requestImages={}):
        return super().requestImages(bucket, requestImages=requestImages)

    def create(self, request,  *args, **kwargs):

        product = Product(
            mediaOne = request.data["mediaOne"],
            mediaTwo = request.data["mediaTwo"],
            mediaThree = request.data["mediaThree"],
            mediaFour = request.data["mediaFour"],
            mediaFive = request.data["mediaFive"],
            mediaSix = request.data["mediaSix"]
        )
        product.save()

        dictRequestImages = {
            product.mediaOne: request.data["mediaOne"],
            product.mediaTwo: request.data["mediaTwo"],
            product.mediaThree: request.data["mediaThree"],
            product.mediaFour: request.data["mediaFour"],
            product.mediaFive: request.data["mediaFive"],
            product.mediaSix: request.data["mediaSix"]
        }
            
        self.requestImages('code-images-and-videos', 
                    requestImages=dictRequestImages)

        return Response({"status":"OK"}, status = status.HTTP_201_CREATED)
    
    def list(self, request = None, *args, **kwargs):

        cftvSerializer = self.__djangoQuerySet.listFull(self.model, self.serializer_class)
        return Response(cftvSerializer, status = status.HTTP_200_OK)

    def findOne(self, request, ids):

        cftvSerializer  = self.__djangoQuerySet.filterOne(ids, self.model, CftvSerializer)
        return Response(cftvSerializer, status = status.HTTP_200_OK)

    def findPrice(self, request, price):

        cftvSerializer = self.__djangoQuerySet.filterPrice(price, self.model, CftvSerializer)
        return Response(cftvSerializer, status = status.HTTP_200_OK)
    
    def findMake(self, request, make):

        cftvSerializer = self.__djangoQuerySet.filterString(make, self.model, CftvSerializer)
        return Response(cftvSerializer, status = status.HTTP_200_OK)