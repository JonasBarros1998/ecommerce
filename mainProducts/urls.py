from django.urls import include, path
from .viewsets.mainProdutsViewset import mainProductsViewset
from .viewsets.insertMainProductsViewset import InsertMainProducts

urlpatterns = [
   path("mainProducts/insert", InsertMainProducts.as_view({"post": "create"}), name="create"),
   path("mainProducts", mainProductsViewset.as_view({"get": "listing"}), name="listing")
]