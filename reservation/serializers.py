from datetime import timedelta

from rest_framework.serializers import ModelSerializer

from reservation.models import Appointment


class AppointmentReservedDays(ModelSerializer):
    class Meta():
        model = Appointment
        fields = ['start_date', 'end_date']

    def get_all_dates(self, obj):
        all_dates = [obj.start_date + timedelta(days=x) for x in range((obj.end_date - obj.start_date).days + 1)]
        return [date.strftime('%Y-%m-%d') for date in all_dates]
