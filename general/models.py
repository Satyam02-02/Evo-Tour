from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    mobile = models.CharField(max_length=40)
    queue = models.CharField(max_length=200)




class LoginModel(models.Model):
    aid = models.CharField(max_length=120)
    passwd = models.CharField(max_length=50)


