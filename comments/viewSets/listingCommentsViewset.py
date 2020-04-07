from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from utilities.mongodb.listing.listing import ListingCollection  

class ListingCommentsViewset(ModelViewSet):

    def __init__(self):
        super().__init__()
        self.__listing = ListingCollection()
        self.__datas = []

    #Listar todos os comentarios relacionado ao produto 
    def list(self, request):
        product_id = request.query_params['id']
        database = 'client'
        collection = 'comments'
        search = {'id': product_id}
        data_collection = self.__listing.search_indice(database, collection, search)
        for item in data_collection: 
            item['_id']  = str(item['_id'])
            self.__datas.append(item)
        return Response({"response": self.__datas}, status=status.HTTP_200_OK)

