from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Vehicles(models.Model):
    car_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    avg_rating = models.FloatField(default=0.0)
    rating = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    rates_number = models.IntegerField(default=0)
    def __str__(self):
        return self.car_id