from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.TextField()
    cpassword=models.TextField()
    
    def __str__(self):
        return self.name

class meta:
    model=User
    fields=('name','email','password','cpassword')

# class Login(models.Model):
#    email=models.EmailField( max_length=254)
#    password=models.TextField()
    