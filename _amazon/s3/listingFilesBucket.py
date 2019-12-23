"""
Esse modulo é responsavel por listar
todos os arquivos e imagens que
estão salvos no bucket da amazon s3 
"""
from abc import ABC, abstractmethod
import boto3


listingKeys = []
class ListingFilesBucket(ABC):

    def __init__(self):
        super().__init__()
        self.__s3Resource = boto3.resource('s3')

    @abstractmethod
    def listing(self, bucketname):
        bucket = self.__s3Resource.Bucket(bucketname)

        for itemBucket in bucket.objects.all():
            listingKeys.append(itemBucket.key)
            
        return listingKeys

