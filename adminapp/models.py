from django.db import models

# Create your models here.
class Products(models.Model):
    productname=models.CharField(max_length=100)
    productprice=models.IntegerField()
    productquantity=models.IntegerField()
    productimage=models.ImageField(upload_to='sample')


class Category(models.Model):
    categoryname=models.CharField(max_length=100)
    categorydescription=models.CharField(max_length=200)
    categoryimage=models.ImageField(upload_to='sample')