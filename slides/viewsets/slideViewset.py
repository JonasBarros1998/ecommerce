from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

class SlideViewset(ModelViewSet):

    def __init__(self):
        super().__init__()
    
    def list(self, request):
        listingKeys = self.listing(bucketname = "ecommerce-slide")
        return Response({"keys": listingKeys}, status = status.HTTP_200_OK)