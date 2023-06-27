from django.db import models
class userdata(models.Model):
    userName=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.CharField(max_length=200)

# Create your models here.
