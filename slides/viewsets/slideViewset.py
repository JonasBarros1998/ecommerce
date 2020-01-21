from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from _amazon.s3.listingFilesBucket import ListingFilesBucket

class SlideViewset(ListingFilesBucket, ModelViewSet):

    def __init__(self):
        super().__init__()
    
    def listing(self, bucketname):
        return super().listing(bucketname)
    
    def list(self, request):
        listingKeys = self.listing(bucketname = "ecommerce-slide")
        return Response({"keys": listingKeys}, status = status.HTTP_200_OK)