from photoExplorer.Insert.insertImages import InsertImages
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from ..serializers.slideSerializer import SlidesSerializer

class CreateImages(ModelViewSet):

    serializer_class = SlidesSerializer

    def __init__(self):
        super().__init__()
        self._insert = InsertImages()
        self._database = "PhotoExplorer"
        self._collection = "Slide"
    
    def create(self, request):
        slides = request.data['slides']
        self._insert.insert(self._database, self._collection, datas = slides)
        return Response({"response":"created"}, status=status.HTTP_201_CREATED)

