from django.db import models
class carinfo(models.Model):
    carName=models.CharField(max_length=200)
    carImages=models.CharField(max_length=2000)
    fuleType=models.CharField(max_length=100)
    seats=models.CharField(max_length=100)
    trasmission=models.CharField(max_length=100)
    carRent=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    carType=models.CharField(max_length=200)
