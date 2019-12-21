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
    bucketName: Nome do bucket
    fileObject: Objeto com o arquivo para que o upload possa ser feito
    fileName: Como o arquivo deverá ser nomeado
    """
    @abstractmethod
    def requestImages(self, bucket, requestImages={}):

        copyRequest = requestImages.copy()
        print(copyRequest[0])
        #dictValues = convertRequestToDict.value()
        countDict = len(copyRequest)

        """
        for item_dict in round(countDict):
            itemImage = requestDict[item_dict]
            image = Image.open(itemImage)
            byteImage = io.BytesIO()
            image.save(byteImage, "JPEG")
            byteImage.seek(0)
            self.saveImages(byteImage, key, bucket)
        """

    def saveImages(self, body, key, bucket):

        try:
            uploadFile = self.__s3Client.put_object(Body=body,
                                                    Key=key,
                                                    Bucket=bucket)
            logging.info("A imagem foi salva")
            return {"status": self.__STATUS_201_CREATED}

        except ClientError as error:
            logging.error(error)
            return {"status": self.__STATUS_404_ERROR}
