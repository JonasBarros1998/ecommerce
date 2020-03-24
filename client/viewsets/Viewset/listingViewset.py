from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from utilities.mongodb.listing.listing import ListingCollection

class ListingViewSet(ModelViewSet):
    def __init__(self):
        self.listing_collection = ListingCollection()
        self._item = []
    
    def list_all_items(self, request):
        search_collection = self.listing_collection.search_all("client", "informations")
        for itens in search_collection:
            itens['_id'] = str(itens['_id'])
            self._item.append(itens)

        return Response({"response": self._item}, status=status.HTTP_200_OK)



    
