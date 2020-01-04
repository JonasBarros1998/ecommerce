from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Comments(models.Model):
    
    name = models.CharField(null = False, max_length = 50)
    #Um produto tem varios comentarios, e um comentario está relacionado a um produto
    product = models.ManyToManyField(Product)
    #Comentario do cliente
    comment = models.TextField(null = False)
    avaliation = models.IntegerField(null = True)
    date = models.DateField(max_length = 50, auto_now_add = True, null = True)