from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    mileage = models.FloatField()
    price = models.FloatField()
    description = models.TextField(max_length=255)
    used = models.BooleanField()