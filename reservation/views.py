from datetime import timedelta

from django.db import transaction
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentApiView(APIView):
    def get(self, request):
        found_objects = Appointment.find_by_two_months()
        res = []
        for appointment in found_objects:
            start = appointment.start_date
            end = appointment.end_date
            delta = (end - start + timedelta(days=1)).days
            for i in range(delta):
                res.append(start.date())
                start += timedelta(days=1)

        return Response({
            'days': res,
        })


class AppointmentCreate(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save()