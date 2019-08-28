from django.db import models

class Chart(models.Model):
    
    subtotal = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    total = models.FloatField(null=False)