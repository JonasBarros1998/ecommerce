from django.urls import include, path
from slides.viewsets.InsertSlidesViewset import CreateImages
from slides.viewsets.slideViewset import SlideViewset

urlpatterns = [
   #Url para reinderização, de imagens para os slides, descomente para funcionar
   #path("slides", SlideViewset.as_view({"get": "list"}), name="listingObject")
   #url para renderização de imagens, usando um servidor comun para upload de imagens
   path("slides", CreateImages.as_view({"post": "create"}), name="create"),
   path("search-slides", SlideViewset.as_view({"get":"list"}), name="listing")
]