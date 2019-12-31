from django.db import models
import PIL

class Product(models.Model):
    
    title = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=250, null=False)
    fullDescription = models.TextField(null=False)
    make = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=50, null=False)
    amount = models.IntegerField(null=False)
    especification = models.TextField(null=False)
    categories = models.CharField(max_length=50, null=False)

    mediaOne = models.ImageField(null=True)
    mediaTwo = models.ImageField(null=True)
    mediaThree = models.ImageField(null=True)
    mediaFour = models.ImageField(null=True)
    mediaFive = models.ImageField(null=True)
    mediaSix = models.ImageField(null=True)

class Cftv(models.Model):

    resolution = models.CharField(max_length=50, null=False)
    amountCameras = models.IntegerField(null=False)
    coaxialCableSize = models.FloatField(null=False)
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
    products = models.OneToOneField(Product, on_delete = models.CASCADE, 
                                    related_query_name = 'products')

        