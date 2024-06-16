
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    dob= models.CharField(max_length=255)
    phone_number= models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.BinaryField()
    confirm_password  = models.CharField(max_length=255)