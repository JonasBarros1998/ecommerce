from django.urls import path, include
from products.api.ProductsviewSet import ProductsViewSet

urlpatterns = [
    path('products', ProductsViewSet.as_view({'get': 'allProducts', 'post': 'create'}), name='products'),
    
    path('products/<int:id>', ProductsViewSet.as_view({'get': 'findOneProduct'}), name='findOneProducts')
]