from django.contrib.postgres.fields import ArrayField
from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=250, null=False)
    fullDescription = models.TextField(null=False)
    make = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=50, null=False)
    amount = models.IntegerField(null=False)
    especification = models.TextField(null=False)
    categorie = models.CharField(max_length=100, null=False)
    media = models.CharField(max_length=300, null=True)

class Cftv(models.Model):

    resolution = models.CharField(max_length=50, null=False)
    amountCameras = models.IntegerField(null=False)
    coaxialCableSize = models.FloatField(null=False)
    products = models.OneToOneField(Product, on_delete=models.CASCADE,
                                    related_name='product',
                                    related_query_name="products")

class SmartWatch(models.Model):

    waterProof = models.CharField(null=False, max_length=30)
    color = models.CharField(max_length=20, null=False)
    heartRate = models.CharField(max_length=120, null=False)
    products = models.OneToOneField(Product, on_delete=models.CASCADE,
                                    related_name='smartwatch_product',
                                    related_query_name="smartwatch_products")

class AirPhones(models.Model):

    waterProof = models.CharField(null = False, max_length = 10)
    bateryPhone = models.CharField(max_length = 50, null = False)
    bateryCase = models.CharField(max_length = 30, null = False)
    voiceControl = models.CharField(null = False, max_length = 10)
    products = models.OneToOneField(Product, on_delete=models.CASCADE,
                                    related_query_name='products')
