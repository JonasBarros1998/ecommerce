from django.urls import path, include
from api.ProductsviewSet import ProductsViewSet

urlpatterns = [
    path('products', ProductsViewSet.as_view({'get': 'listProducts'}), name='listProducts')
    path('products/<id:int>', ProductsViewSet.as_view({'get': 'findOne'}), name=True)

]