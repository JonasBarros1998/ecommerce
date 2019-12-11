from django.contrib import admin
from django.urls import path, include
from oauth2_provider import urls
                    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('jm-ecommerce/', include('products.urls')), 
    path('jm-ecommerce/', include('comments.urls')),
    path('jm-ecommerce/', include('Users.urls')),
    path('jm-ecommerce/authentication/', include('oauth2_provider.urls'))
]
