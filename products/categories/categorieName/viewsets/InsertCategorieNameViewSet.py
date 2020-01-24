from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from photoExplorer.Insert.insertImages import InsertImages
from ..serializer.categorieNameSerializer import CategorieNameSerializer

class InsertCategorieNameViewSet(ModelViewSet):

    serializer_class = CategorieNameSerializer

    def __init__(self):
        super().__init__()
        self._insertImages = InsertImages()
        self._database = "PhotoExplorer"
        self._collection = "categorieName" 
    
    def create(self, request):
        self._insertImages.insert(self._database, self._collection, request.data)
        return Response({"status": 201}, status = status.HTTP_200_OK)