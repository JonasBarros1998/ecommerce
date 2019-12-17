from django.urls import path, include
from .viewsets.userView import UserView

urlpatterns = [
    path('user/register/', UserView.as_view({'post': 'create'}), name='create_user'),
    path('user/register/verifield/', UserView.as_view({'post': 'verifieldUser'}), name='user_verifield')
]
