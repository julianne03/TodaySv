from django.db import models
from django.utils import timezone
# Create your models here.
class Answers(models.Model) :

    WEATHER_CHOICES = {
        ('sunny', 'images/sunny'),
        ('cloudy', 'images/cloudy'),
        ('windy', 'images/windy'),
        ('rainy', 'images/rainy'),
        ('snowy', 'images/snowy')
    }

    weather = models.CharField(max_length=80, choices=WEATHER_CHOICES, null=True)
