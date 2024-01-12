from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

# r = DefaultRouter()
# r.register('reserved-days', AppointmentListView)
#
# urlpatterns = [
# ] + r.urls

urlpatterns = [
    path('reserved_days', AppointmentApiView.as_view()),
    path('reserve', AppointmentCreate.as_view())
]