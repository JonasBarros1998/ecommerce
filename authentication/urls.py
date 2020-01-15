from django.urls import include, path
from oauth2_provider import urls
from .viewSets.authenticationViewSet import AuthenticationViewSet
from .viewSets.validatorTokenViewSet import ValidatorTokenViewSet

urlpatterns = [
    path('authentication/', 
            include('oauth2_provider.urls'), name="url_authentication"),
    
    path('authentication/id', 
            AuthenticationViewSet.as_view({'post': 'searchUserId'}), 
            name="search_id_user"),
    
    path('authentication/valid/token', 
            ValidatorTokenViewSet.as_view({'get':'validator'}), 
            name='valid_token')
]