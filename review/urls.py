from django.urls import path
from .views import ReviewListAPIView, ReviewDetailAPIView

urlpatterns = [
    path('', ReviewListAPIView.as_view()),
    path('<int:pk>/', ReviewDetailAPIView.as_view()),
]