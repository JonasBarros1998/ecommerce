from django.urls import include, path
from oauth2_provider import urls
from .viewSets.authenticationViewSet import AuthenticationViewSet

urlpatterns = [
    path('authentication/', include('oauth2_provider.urls'), name="url_authentication"),
    path('authentication/Id', AuthenticationViewSet.as_view({'post': 'searchUserId'}), name="search_id_user")
]
