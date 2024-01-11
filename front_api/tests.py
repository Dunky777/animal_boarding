from django.test import TestCase

# Create your tests here.
from rest_framework import serializers

from reservation.models import Appointment


class AppointmentReservedDays(serializers.Serializer):
    text = serializers.CharField(min_length=10)

    class Meta():
        model = Appointment
        fields = ['start_date', 'end_date']