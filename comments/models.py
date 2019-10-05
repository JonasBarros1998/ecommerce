from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Comments(models.Model):
    
    #Todo comentario tem um usuario, e todo o usuario  tem um comentario
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    #Um produto tem varios comentarios, e um comentario está relacionado a um produto
    product = models.ManyToManyField(Product)

    #Comentario do cliente
    comment = models.TextField(null=False)
    
    avaliation = models.IntegerField(null=True)

    date = models.DateField(max_length=50, null=True, auto_now=True)