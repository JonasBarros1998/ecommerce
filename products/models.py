from django.db import models
import PIL

class Product(models.Model):
    
    title = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.TextField(null=True)
    make = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=50, null=True)
    amount = models.IntegerField(null=True)
    categories = models.CharField(max_length=50, null=True)

    mediaOne = models.ImageField(null=True)
    mediaTwo = models.ImageField(null=True)
    mediaThree = models.ImageField(null=True)
    mediaFour = models.ImageField(null=True)
    mediaFive = models.ImageField(null=True)
    mediaSix = models.ImageField(null=True)


class Cftv(models.Model):

    resolution = models.CharField(max_length=50, null=True)
    amountCameras = models.IntegerField(null=True)
    coaxialCableSize = models.FloatField(null=True)
    products = models.OneToOneField(Product, on_delete = models.CASCADE, 
                                related_name='product', 
                                related_query_name="products")   

class SmartWatch(models.Model):

    waterProof = models.BooleanField(null=False)
    color = models.CharField(max_length = 20, null=False)
    heartRate = models.CharField(max_length=120, null=False)
    products = models.OneToOneField(Product, on_delete = models.CASCADE)

class AirPhones(models.Model):

    waterProof = models.BooleanField(null=False)
    bateryPhone = models.CharField(max_length=50, null=False)
    bateryCase = models.CharField(max_length=30, null=False)
    voiceControl = models.BooleanField(null=False) 
    products = models.OneToOneField(Product, on_delete = models.CASCADE, related_query_name = 'products')

        