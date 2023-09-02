from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class descri(models.Model):
    photo = models.ImageField(upload_to='images/')
    product_name = models.CharField(max_length = 100)
    product_price = models.IntegerField()
    product_descrition = models.CharField(max_length = 100)

class createacc(models.Model):
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)


class wish(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    productid = models.ForeignKey(descri,on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


class cart(models.Model):
    userid = models.ForeignKey(User,on_delete = models.CASCADE)
    productid = models.ForeignKey(descri,on_delete = models.CASCADE)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()

class checkout(models.Model):
    userid = models.ForeignKey(User,on_delete= models.CASCADE)
    productid = models.ForeignKey(descri,on_delete= models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    zipcode  = models.IntegerField()
 
