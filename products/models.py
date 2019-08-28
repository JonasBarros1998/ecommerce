from django.db import models

class Products(models.Model):
    
    name = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False)
    description = models.TextField(null=False)