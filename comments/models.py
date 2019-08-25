from django.db import models
from django.contrib.auth.models import User
from products.models import Products

class Comments(models.Model):

    #Todo comentario tem um usuario, e todo o usuario  tem um comentario
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    #Um produto tem varios comentarios, e um comentario está relacionado a um produto
    products = models.ForeignKey(Products, on_delete = models.CASCADE)

    #Comentario do cliente
    comments = models.TextField(null=False)
