from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):

    date = models.DateField(null=False)
    genre = models.CharField(max_length = 50, null=False)
    cpf = models.FloatField(null=False)
    phone = models.FloatField(max_length=80, null=False)
    phoneResidential = models.FloatField(null=True)

    """
    A cada registro adicionado pelo usuario, estará atrelado, ao um usuario especifico.  
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

