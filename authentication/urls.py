from django.urls import path
from authentication.api.oauth2.gearToken import GearToken

urlpatterns = [
    path("authorizeToken/", GearToken.as_view({'post':'token'}), name="token"),
]
