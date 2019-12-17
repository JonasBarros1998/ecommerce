from django.db import models
from django.contrib.auth.models import User

class RegisterUser(models.Model):
    user = models.OneToOneField(User, 
                                                        on_delete=models.CASCADE, 
                                                        primary_key=True)
    fullName =models.CharField(max_length=120, null=False)
    birthDate = models.DateField(null = False)
    male = models.CharField(max_length=30, null=False)
    feminine = models.CharField(max_length=30, null=False)
    cpf = models.CharField(max_length=50, null=False)
    smartPhone = models.CharField(max_length=50, null=False )
    phone = models.CharField(max_length=50, null=False)