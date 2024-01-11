from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Appointment(models.Model):
    phone = models.CharField(max_length=32, default=None)
    telegram = models.CharField(max_length=64, null=True)
    start_date = models.DateTimeField(unique=True)
    end_date = models.DateTimeField(unique=True)

