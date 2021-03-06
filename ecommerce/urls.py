from django.contrib import admin
from django.urls import path, include
from oauth2_provider import urls
                    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('jm-ecommerce/', include('products.urls')), 
    path('jm-ecommerce/', include('comments.urls')),
    path('jm-ecommerce/', include('users.urls')),
    path('jm-ecommerce/', include('slides.urls')),
    path('jm-ecommerce/', include('authentication.urls')),
    path('jm-ecommerce/', include('mainProducts.urls')),
    path("jm-ecommerce/", include('client.urls'))
]
