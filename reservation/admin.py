from django.contrib import admin
from .models import Appointment


# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'telegram', 'start_date', 'end_date']
    list_editable = ['start_date', 'end_date']
