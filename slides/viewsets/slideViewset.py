from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from photoExplorer.search.searchImage import SearchImages

class SlideViewset(ModelViewSet):

    def __init__(self):
        super().__init__()
        self._searchImages = SearchImages()
        self._database = "PhotoExplorer"
        self._collection = "Slide"

    def list(self, request):
        links = self._searchImages.FindMany(self._database, self._collection)
        return Response({'response': links}, status = status.HTTP_200_OK)