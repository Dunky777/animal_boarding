from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AppointmentListView

# r = DefaultRouter()
# r.register('reserved-days', AppointmentListView)
#
# urlpatterns = [
# ] + r.urls

urlpatterns = [
    path('reserved_days', AppointmentListView.as_view()),
]