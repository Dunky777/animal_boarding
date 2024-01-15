from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reservation.urls')),
    path('api/reviews/', include('review.urls')),
    path('api/staff/', include('staff.urls')),
]
