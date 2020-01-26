from django.urls import include, path
from .viewsets.mainProdutsViewset import mainProductsViewset
from .viewsets.insertMainProductsViewset import InsertMainProducts
from .viewsets.insertProductSpecialViewset import InsertProdutcSpecialsViewset
from .viewsets.productSpecialsViewset import ProductsSpecialsViewset

urlpatterns = [
   path("mainProducts/insert", InsertMainProducts.as_view({"post": "create"}), name="create"),
   path("mainProducts", mainProductsViewset.as_view({"get": "listing"}), name="listing"), 

   path("products-specials/insert/", InsertProdutcSpecialsViewset.as_view({"post": "create"}), name="create"),
   path("products-specials", ProductsSpecialsViewset.as_view({"get": "listing"}), name="listing")
]