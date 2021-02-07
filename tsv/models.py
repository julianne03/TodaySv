from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Answers(models.Model) :
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    weather = models.CharField(max_length=80, null=True)
    mood = models.CharField(max_length=80, null=True)
    wake_up = models.DateTimeField(null=True)
    did_well = models.CharField(max_length=100, null=True)
    happiness = models.TextField(max_length=100, null=True)
    breakfast = models.CharField(max_length=100, null=True)
    lunch = models.CharField(max_length=100, null=True)
    dinner = models.CharField(max_length=100, null=True)
