from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from photoExplorer.search.searchImage import SearchImages

class CategorieNameViewSet(ModelViewSet):

    def __init__(self):
        super().__init__()
        self._searchImages = SearchImages()
        self._databse = "PhotoExplorer"
        self._collection = "categorieName"

    def list(self, request):
        links = self._searchImages.FindMany(self._databse, self._collection)
        return Response({"response": links}, status = status.HTTP_201_CREATED)
