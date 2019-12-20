from django.urls import path, include

from products.api.ProductsviewSet import ProductsViewSet
from products.categories.categorieCftv.viewsets.CftvViewSet import CftvViewSet

from products.api.Categories.AirPhones.airPhonesViewSet import AirPhonesViewSet
from products.api.Categories.SmartWatch.smartWathViewSet import SmartWathViewSet

urlpatterns = [

    #Rota para cadastro de produtos em geral
    path('products', ProductsViewSet.as_view({'get':'list', 'post': 'create'}), name='products'),
    path('products/make', ProductsViewSet.as_view({'get':'findMakeAll'}), name='makeProducts'),
    path('products/categories', ProductsViewSet.as_view({'get':'findCategoriesAll'}), name='findCategories'),
    path('products/categories/<str:categories>', ProductsViewSet.as_view({'get':'findOneCategories'}), name="findOneCategories"),

    #Rotas para produtos de cftv
    path('products/cftv', CftvViewSet.as_view({'get': 'list', 'post': 'create'}), name='products'),
    path('products/cftv/<int:ids>', CftvViewSet.as_view({'get': 'findOne'}), name='findOne'),
    path('products/ctfv/price/<str:price>', CftvViewSet.as_view({'get': 'findPrice'}), name='findPrice'),
    path('products/ctfv/make/<str:make>', CftvViewSet.as_view({'get': 'findMake'}), name='findMake'),
    
    #Rotas para produtos de airphone
    path('products/airPhone', AirPhonesViewSet.as_view({'get':'list', 'post':'create'}), name='airPhone'),
    path('products/airPhone/<int:air_phone_ids>', AirPhonesViewSet.as_view({'get':'findOne'}), name='findOneAirPhones'),
    path('products/airPhone/<str:air_phone_make>', AirPhonesViewSet.as_view({'get':'findMakeAll'}), name="airPhoneMake"),

    #Rotas para produtos de smartwatch
    path('products/smartWatch', SmartWathViewSet.as_view({'post':'create', 'get':'list'}), name='smartWatch'),
    path('products/smartWatch/<int:smart_watch_ids>', SmartWathViewSet.as_view({'get':'findOne'}), name='findOneSmartWatch'),
    path('products/smartWatch/<str:smart_watch_make>', SmartWathViewSet.as_view({'get':'findMakeAll'}), name='findMakeAll')
]