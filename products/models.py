from django.db import models

class Product(models.Model):
    
    title = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False)
    description = models.TextField(null=False)
    make = models.CharField(max_length=100, null = False)
    model = models.CharField(max_length = 50, null=False)
    amount = models.IntegerField(null=True)

    mediaOne = models.ImageField(upload_to="products", null=False)
    mediaTwo = models.ImageField(upload_to="products", null=False)
    mediaThree = models.ImageField(upload_to="products", null=False)
    mediaFour = models.ImageField(upload_to="products", null=True)
    mediaFive = models.ImageField(upload_to="products", null=True)
    mediaSix = models.ImageField(upload_to="products", null=True)


class Cftv(models.Model):

    resolution = models.CharField(max_length=50, null=True)
    amountCameras = models.IntegerField(null=True)
    coaxialCableSize = models.FloatField(null=True)
    products = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='product', related_query_name="products")   

class SmartWatch(models.Model):

    color = models.CharField(max_length = 50, null=True)
    products = models.OneToOneField(Product, on_delete = models.CASCADE)


class AirPhones(models.Model):

    waterProof = models.BooleanField(null=False)
    batery = models.CharField(max_length=50, null=False)
    products = models.OneToOneField(Product, on_delete = models.CASCADE)