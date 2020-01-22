from django.urls import include, path
from slides.viewsets.InsertSlidesViewset import CreateImages

urlpatterns = [
   #Url para reinderização, de imagens para os slides, descomente para funcionar
   #path("slides", SlideViewset.as_view({"get": "list"}), name="listingObject")
   #url para renderização de imagens, usando um servidor comun para upload de imagens
   path("insert-slides", CreateImages.as_view({"post": "create"}), name="listingObject")
]