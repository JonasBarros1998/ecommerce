from django.urls import path, include
from .api.userSetViews import UsersViewSet

urlpatterns = [
    path("user/register/", UsersViewSet.as_view({'post':'create'}), name="create user"),
    path("user/register/verifield/", UsersViewSet.as_view({'post': 'verifield'}, name="verifield"))
]