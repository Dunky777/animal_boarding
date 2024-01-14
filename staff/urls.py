from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path('obtain-pair', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh')
]