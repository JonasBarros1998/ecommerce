"""
Modulo serve apenas para enviar arquivos(podendo ser de
qualquer tipo), para o bucket do s3.
"""
import boto3
from botocore.client import ClientError
from abc import ABC, abstractmethod
import logging
from PIL import Image 
import io


class SaveFileBucket(ABC):
    def __init__(self):
        self.__s3Client = boto3.client('s3')
        self.__STATUS_201_CREATED = "STATUS_201_CREATED"
        self.__STATUS_404_ERROR = "STATUS_404_ERROR"

    """
    ***Function Params***
    bucket: Nome do bucket
    requestImages: Dict com as imagens a ser salva no s3
    item_dict[1]: A imagem a ser aberta com o PILLOW
    item_dict[0]: O nome da imagem a ser salva no bucket
    """
    @abstractmethod
    def requestImages(self, bucket, requestImages={}):
        _nameImage = 0
        _image = 1
        for item_dict in iter(requestImages.items()):   
            image = Image.open(item_dict[_image])
            byteImage = io.BytesIO()
            image.save(byteImage, "JPEG")
            byteImage.seek(0)
            self.saveImages(byteImage, item_dict[_nameImage], bucket)

    
    def saveImages(self, body, key, bucket):

        try:
            uploadFile = self.__s3Client.put_object(ACL='public-read',
                                                    Body=body,
                                                    Key=key,
                                                    Bucket=bucket)
            logging.info("A imagem foi salva")
            return {"status": self.__STATUS_201_CREATED}

        except ClientError as error:
            logging.error(error)
            return {"status": self.__STATUS_404_ERROR}