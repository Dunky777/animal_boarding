from datetime import datetime

from django.db.models import Q
from rest_framework import serializers

from reservation.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate_phone(self, value: str):
        # Пример валидации поля field1
        if len(value) > 4:
            raise serializers.ValidationError("Введите корректный номер телефона")
        return value

    def validate_telegram(self, value: str):
        if value is None or value == '':
            return None
        if len(value) < 2:
            raise serializers.ValidationError("Введите корректный никнейм телеграма (пример @yourname)")
        if value[0] == '@' and value.count('@') == 1:
            raise serializers.ValidationError("Введите корректный никнейм телеграма (пример @yourname)")
        return value

    def validate(self, data: dict):
        start = data['start_date']
        end = data['end_date']

        if start > end:
            raise serializers.ValidationError("Некорректная дата. Нарушена последовательность")
        if start == end:
            raise serializers.ValidationError("Даты не должны совпадать")
        if not (start.hour >= 8 and start.hour <= 22 and end.hour >= 8 and end.hour <= 22):
            raise serializers.ValidationError("Диапазон времени запрещен")

        curr_date = datetime.now()
        curr_month = curr_date.month
        if start.month not in [curr_month, curr_month + 1] and end.month not in [curr_month, curr_month + 1]:
            raise serializers.ValidationError("Только текущий и следующий месяцы доступны")

        found_objects = Appointment.find_by_two_months()
        for obj in found_objects:
            obj_start = obj.start_date
            obj_end = obj.end_date
            if obj_start <= start <= obj_end or obj_start <= end <= obj_end:
                raise serializers.ValidationError(
                    "Невозможно выбрать данный диапазон. Кто-то уже забронировал один или несколько дней")
        return data
