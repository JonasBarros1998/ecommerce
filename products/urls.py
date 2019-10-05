from django.urls import path, include
from products.api.ProductsviewSet import ProductsViewSet
from products.api.Categories.Cftv.CftvViewSet import CftvViewSet

urlpatterns = [
    #Rota para cadastro de produtos em geral
    path('products', ProductsViewSet.as_view({'get':'list', 'post': 'create'}), name='products'),
    
    #Rotas para produtos de CFTV
    path('products/cftv', CftvViewSet.as_view({'get': 'list', 'post': 'create'}), name='products'),
    path('products/cftv/<int:ids>', CftvViewSet.as_view({'get': 'findOne'}), name='findOne'),
    path('products/ctfv/price/<str:price>', CftvViewSet.as_view({'get': 'findPrice'}), name='findPrice'),
    path('products/ctfv/make/<str:make>', CftvViewSet.as_view({'get': 'findMake'}), name='findMake'),
]