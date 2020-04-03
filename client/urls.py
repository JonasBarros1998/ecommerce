from django.urls import path, include
from client.viewsets.clientViewset import ClientViewset
from client.viewsets.Viewset.listingViewset import ListingViewSet 

urlpatterns = [
    path("client/update-item", ClientViewset.as_view({"post": "update_item"}), name="update-item"), 
    path("client/create-client", ClientViewset.as_view({"post": "create_client"}), name="create-client"),
    path("client/address", ClientViewset.as_view({"post": "find_client_update_address"}), name="address"),
    path("client/save-purchase", ClientViewset.as_view({"post": "save_purchase"}), name="save-purchase"),
    path("client/listing-one/", ListingViewSet.as_view({"get": "list_item_client"}), name="listing_one"),
    path("client/listing-items", ListingViewSet.as_view({"get": "list_all_items"}), name="list_all_items"),
]

