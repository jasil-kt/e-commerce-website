from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)



class customer(models.Model):
    customer_data = models.ForeignKey("Login",on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_no = models.CharField()

class seller(models.Model):
    seller_data = models.ForeignKey("Login", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    gst_no = models.IntegerField()
    product_category = models.CharField()
