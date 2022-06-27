from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_officer = models.BooleanField(default=False)
    is_tstaff = models.BooleanField(default=False)
    is_farmer=models.BooleanField(default=False)
    name=models.CharField(max_length=25,null=True)
    address=models.TextField(null=True)
    gender=models.CharField(max_length=10 ,null=True)
    contact_no=models.CharField(max_length=10,null=True)
    location=models.CharField(max_length=25,null=True)
    specialisation=models.CharField(max_length=25,null=True)



class notification(models.Model):
    date = models.DateField(max_length=25)
    subject = models.CharField(max_length=25)
    description = models.TextField()

# class feedback(models.Model):
#     date = models.DateField(max_length=25)
#     subject = models.CharField(max_length=25)
#     description = models.TextField()



#market api

class market(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    quantity = models.TextField()
    location = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    amount = models.IntegerField()
    image = models.ImageField(upload_to='products')



# #send notification
class sendapplication(models.Model):
      name = models.ImageField(max_length=25)
