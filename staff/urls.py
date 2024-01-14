from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *

urlpatterns = [
    path('obtain-pair', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token', TokenVerifyView.as_view(), name='token-verify'),
    path('profile', ProfileView.as_view(), name='profile')
]