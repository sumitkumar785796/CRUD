from django.db import models

# Create your models here.
class createRecord(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mob=models.CharField(max_length=10)
    address=models.TextField()