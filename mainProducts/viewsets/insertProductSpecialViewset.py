from photoExplorer.Insert.insertImages import InsertImages
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from ..serializer.productSpecialSerializer import ProductSpecialSerializer

class InsertProdutcSpecialsViewset(ModelViewSet):

    serializer_class = ProductSpecialSerializer

    def __init__(self):
        super().__init__()
        self._insertImage = InsertImages()
        self._database = "PhotoExplorer"
        self._collection = "productSpecial"

    def create(self, request):
        datas = request.data
        self._insertImage.insert(self._database, self._collection, datas)
        return Response({"status": 201}, status=status.HTTP_201_CREATED)