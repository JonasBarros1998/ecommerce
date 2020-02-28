from django.urls import path, include

from products.api.ProductsviewSet import ProductsViewSet
from products.categories.categorieCftv.viewsets.CftvViewSet import CftvViewSet
from products.categories.categorieCftv.viewsets.createCftvViewset import CreateCftvViewset

from products.categories.airphones.viewsets.airPhonesViewSet import AirphonesViewSet
from products.categories.airphones.viewsets.createAirphoneViewset import CreateAirphoneViewset

from products.categories.smartWatch.viewset.createSmartwatchViewset import CreateSmartwatchViewset
from products.categories.smartWatch.viewset.smartWathViewSet import SmartWathViewSet

from products.categories.categorieName.viewsets.categorieNameViewset import CategorieNameViewSet
from products.categories.categorieName.viewsets.InsertCategorieNameViewSet import InsertCategorieNameViewSet

urlpatterns = [

    # Rota para cadastro de produtos em geral
    path('products/', ProductsViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='products'),

    path('products/make', ProductsViewSet.as_view(
         {'get': 'findMakeAll'}), name='makeProducts'),

    path('products/one-make/<str:make>', ProductsViewSet.as_view(
         {'get': 'findOneMake'}), name='makeOneProducts'),

    path('products/categories',
         ProductsViewSet.as_view({'get': 'findCategoriesAll'}), name='findCategories'),

    path('products/categories/<str:categories>',
         ProductsViewSet.as_view({'get': 'findOneCategories'}), name="findOneCategories"),

    # Rotas para produtos de cftv
    path('products/cftv',
         CftvViewSet.as_view({'get': 'list'}), name='products'),
    path('products/cftv/',
         CreateCftvViewset.as_view({'post': 'create'}), name='save_products'),
    path('products/cftv/<int:ids>',
         CftvViewSet.as_view({'get': 'findOne'}), name='findOne'),
    path('products/ctfv/price/<str:price>',
         CftvViewSet.as_view({'get': 'findPrice'}), name='findPrice'),
    path('products/ctfv/make/<str:make>',
         CftvViewSet.as_view({'get': 'findMake'}), name='findMake'),

    # Rotas para produtos de airphone
    path('products/air-phone/',
         CreateAirphoneViewset.as_view({'post': 'create'}), name='airPhone'),
    path('product/air-phone', AirphonesViewSet.as_view({'get': 'list'})),
    path('products/air-phone/<int:air_phone_ids>',
         AirphonesViewSet.as_view({'get': 'findOne'}), name='findOneAirPhones'),
    path('products/air-phone/<str:air_phone_make>',
         AirphonesViewSet.as_view({'get': 'findMakeAll'}), name="airPhoneMake"),

    # Rotas para produtos de smartwatch
    path('products/smartwatch',
         SmartWathViewSet.as_view({'get': 'list'}), name='smartWatch'),
    path('products/smartwatch/',
         CreateSmartwatchViewset.as_view({'post': 'create'}), name='createSmartwatch'),
    path('products/smartwatch/<int:smart_watch_ids>',
         SmartWathViewSet.as_view({'get': 'findOne'}), name='findOneSmartwatch'),
    path('products/smartwatch/<str:smart_watch_make>',
         SmartWathViewSet.as_view({'get': 'findMakeAll'}), name='findSmartwatch'),

    # Rota salvar e listar as principais categories vendidas no ecommerce
    path('products/name-categorie/list',
         CategorieNameViewSet.as_view({'get': 'list'}), name='list_categorie'),
    path('products/name-categorie/insert',
         InsertCategorieNameViewSet.as_view({'post': 'create'}), name="create_categorie")
]
