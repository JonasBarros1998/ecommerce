from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from utilities.mongodb.listing.listing import ListingCollection


class ListingViewSet(ModelViewSet):
    def __init__(self):
        self.listing_collection = ListingCollection()
        self._item = []

    def list_all_items(self, request):
        search_collection = self.listing_collection.search_all(
            "client", "informations")
        for itens in search_collection:
            itens['_id'] = str(itens['_id'])
            self._item.append(itens)

        return Response({"response": self._item}, status=status.HTTP_200_OK)

    def list_item_client(self, request):
        query_params = request.query_params['to_find']
        split_query_params = query_params.split('-')
        datas = { split_query_params[0]: split_query_params[1] }
        search_one_client = self.listing_collection.search_one('client', 'informations', datas)

        if(search_one_client == None):
            return Response({"response": None}, status=status.HTTP_200_OK)
        else:
            search_one_client['_id'] = str(search_one_client['_id'])
            return Response({"response": search_one_client}, status=status.HTTP_200_OK)
