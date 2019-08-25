from django.urls import path
from login.View.login import userExist

urlpatterns = [
    path("registrar", userExist, name="newUser")
]
