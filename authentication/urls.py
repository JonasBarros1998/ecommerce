from django.urls import include, path
from oauth2_provider import urls
from .viewSets.authenticationViewSet import AuthenticationViewSet
from .viewSets.validatorTokenViewSet import ValidatorTokenViewSet
from .viewSets.forgotPasswordViewset import ForgotPasswordViewset

urlpatterns = [
    path('authentication/',
         include('oauth2_provider.urls'), name="url_authentication"),

    path('authentication/id',
         AuthenticationViewSet.as_view({'post': 'searchUserId'}),
         name="search_id_user"),

    path('authentication/valid/token',
         ValidatorTokenViewSet.as_view({'get': 'validator'}),
         name='valid_token'),

    path('authentication/forgot-password',
         ForgotPasswordViewset.as_view({'post': 'dispatchEmail'}),
         name='forgot_password'),

    path("authentication/reset-password/hash/<str:hash_link>",
         ForgotPasswordViewset.as_view({'put': 'forgotPassword'}),
         name="reset_password")
]
