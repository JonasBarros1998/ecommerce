from django.urls import path, include
from .api.userSetViews import UsersViewSet

urlpatterns = [
    path("createUser", UsersViewSet.as_view({'post': 'create'}), name='create')
]