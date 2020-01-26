from photoExplorer.search.searchImage import SearchImages
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

class ProductsSpecialsViewset(ModelViewSet):
    def __init__(self):
        super().__init__()
        self._searchImages = SearchImages()
        self._database = "PhotoExplorer"
        self._collection = "productSpecial"
    
    def listing(self, request):
        listingProduct = self._searchImages.FindMany(self._database, self._collection)
        return Response({"response": listingProduct}, status=status.HTTP_201_CREATED)

