from django.urls import path

from .views import *

urlpatterns = [
    path('reserved_days', AppointmentApiView.as_view()),
    path('reserve', AppointmentCreate.as_view())
]