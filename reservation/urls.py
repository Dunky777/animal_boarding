from django.urls import path

from .views import *

urlpatterns = [
    path('', reservation),
    path('1', reservation_django, name='reservation_django'),
    path('max', reservation_max),
]