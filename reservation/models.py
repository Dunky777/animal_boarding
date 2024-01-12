from datetime import datetime

import pytz
from django.contrib.auth.models import User
from django.db import models
import os
from dotenv import load_dotenv

load_dotenv()

# Create your models here.
from django.db.models import Q

TIME_ZONE = os.getenv('TIME_ZONE')

class Appointment(models.Model):
    phone = models.CharField(max_length=32, default=None)
    telegram = models.CharField(max_length=64, null=True, blank=True)
    start_date = models.DateTimeField(unique=True)
    end_date = models.DateTimeField(unique=True)
    @staticmethod
    def find_by_two_months():
        curr_month = datetime.now(tz=pytz.timezone(TIME_ZONE)).month
        return Appointment.objects.filter(Q(start_date__month=curr_month) | Q(end_date__month=curr_month))
