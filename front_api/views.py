from datetime import datetime, timedelta

from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from reservation.models import Appointment
from reservation.serializers import DateSerializer


class AppointmentApiView(APIView):
    def get(self, request):
        curr_month = datetime.now().month
        found_objects = Appointment.objects.filter(Q(start_date__month=curr_month) | Q(end_date__month=curr_month))
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
