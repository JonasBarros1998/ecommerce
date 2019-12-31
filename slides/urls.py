from django.urls import include, path
from slides.viewsets.slideViewset import SlideViewset

urlpatterns = [
   #Url para reinderização, de imagens para os slides, descomente para funcionar
   #path("slides", SlideViewset.as_view({"get": "list"}), name="listingObject")
]