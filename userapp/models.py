from django.db import models
from adminapp.models import*

# Create your models here.
class Register(models.Model):
    firstname=models.CharField(max_length=45)
    lastname=models.CharField(max_length=56)
    username=models.CharField(max_length=78)
    password=models.CharField(max_length=80)
    mobilenumber=models.IntegerField()
    address=models.CharField(max_length=90)
    city=models.CharField(max_length=80)
    state=models.CharField(max_length=56)
    zipcode=models.IntegerField()
    
class Login(models.Model):
    username=models.CharField(max_length=89)
    password=models.CharField(max_length=100)

class Cart(models.Model):
    products=models.CharField(max_length=89)
    price=models.IntegerField()
    quantity=models.IntegerField()
    total=models.IntegerField()

class Cartdb(models.Model):
    userid=models.ForeignKey(Register,on_delete=models.CASCADE)
    productid=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0)

class Checkout(models.Model):
    userid=models.ForeignKey(Register,on_delete=models.CASCADE)   
    cartid=models.ForeignKey(Cartdb,on_delete=models.CASCADE,default=0)  
   
class Contactdb(models.Model):
    name=models.CharField(max_length=89)
    email=models.CharField(max_length=80)
    subject=models.CharField(max_length=78)
    messages=models.CharField(max_length=200)