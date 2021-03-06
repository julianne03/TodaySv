from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class Answers(models.Model) :
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_date = models.CharField(max_length=30)
    cm_answer_date = models.DateTimeField(null=True)
    weather = models.CharField(max_length=80, null=True)
    mood = models.CharField(max_length=80, null=True)
    wake_up = models.CharField(max_length=30, null=True)
    did_well = models.CharField(max_length=100, null=True)
    happiness = models.CharField(max_length=100, null=True)
    breakfast = models.CharField(max_length=100, null=True)
    lunch = models.CharField(max_length=100, null=True)
    dinner = models.CharField(max_length=100, null=True)

class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, blank=True)
    image = models.ImageField(blank=True, upload_to="%Y/%m/%d")
