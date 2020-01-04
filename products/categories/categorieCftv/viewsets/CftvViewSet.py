import io
import os
import shutil
import ast
from PIL import Image

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FileUploadParser

from products.models import Cftv, Product
from _amazon.s3.saveImagesBucket import SaveFileBucket
from ..serializer.CftvSerializer import CftvSerializer
from djangoQuerySet.djangoQuerySet import djangoQuerySet

class CftvViewSet(SaveFileBucket,ModelViewSet):

    model = Cftv
    parser_class = [FileUploadParser]
    serializer_class = CftvSerializer

    def __init__(self):
        super().__init__()
        self.__djangoQuerySet = djangoQuerySet()

    def requestImages(self, bucket, requestImages={}):
        return super().requestImages(bucket, requestImages=requestImages)

    def create(self, request,  *args, **kwargs):

        product = Product(
            title = request.data['products']["title"],
            price = request.data['products']["price"],
            description = request.data['products']['description'],
            fullDescription = request.data['products']['fullDescription'],
            make = request.data['products']["make"],
            model = request.data['products']["model"],
            amount = request.data['products']["amount"],
            especification = request.data['products']['especification'],
            categories = request.data['products']['categories'],
            mediaOne=request.data['products']["mediaOne"],
            mediaTwo=request.data['products']["mediaTwo"],
            mediaThree=request.data['products']["mediaThree"],
            mediaFour=request.data['products']["mediaFour"],
            mediaFive=request.data['products']["mediaFive"],
            mediaSix=request.data['products']["mediaSix"])
        product.save()

        cftv = Cftv(
            resolution=request.data["resolution"],
            amountCameras=request.data["amountCameras"],
            coaxialCableSize=request.data["coaxialCableSize"],
            products=product)
        cftv.save()

        # Depois que as imagens forma salvas no bucket,
        # temos que exclui-las, no diretorio do projeto
        """
        shutil.rmtree('_imagesAndVideos')
        dictRequestImages = {
            product.mediaOne.name: request.data["mediaOne"],
            product.mediaTwo.name: request.data["mediaTwo"],
            product.mediaThree.name: request.data["mediaThree"],
            product.mediaFour.name: request.data["mediaFour"],
            product.mediaFive.name: request.data["mediaFive"],
            product.mediaSix.name: request.data["mediaSix"]
        }
        self.requestImages('code-images-and-videos',
                           requestImages=dictRequestImages)"""

        return Response({"status": "OK"}, status=status.HTTP_201_CREATED)

    def list(self, request=None, *args, **kwargs):

        cftvSerializer = self.__djangoQuerySet.listFull(
            self.model, self.serializer_class)
        return Response(cftvSerializer, status=status.HTTP_200_OK)

    def findOne(self, request, ids):

        cftvSerializer = self.__djangoQuerySet.filterOne(
            ids, self.model, CftvSerializer)
        return Response(cftvSerializer, status=status.HTTP_200_OK)

    def findPrice(self, request, price):

        cftvSerializer = self.__djangoQuerySet.filterPrice(
            price, self.model, CftvSerializer)
        return Response(cftvSerializer, status=status.HTTP_200_OK)

    def findMake(self, request, make):

        cftvSerializer = self.__djangoQuerySet.filterString(
            make, self.model, CftvSerializer)
        return Response(cftvSerializer, status=status.HTTP_200_OK)
