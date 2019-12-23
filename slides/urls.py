from django.urls import include, path
from slides.viewsets.slideViewset import SlideViewset

urlpatterns = [
   path("slides", SlideViewset.as_view({"get": "list"}), name="listingObject")
]