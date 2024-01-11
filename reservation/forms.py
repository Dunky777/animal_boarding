from django import forms


class AppointmentForm(forms.Form):
    start_date = forms.DateTimeField(label='Начиная с', widget=forms.DateTimeInput(
       attrs={'class': 'form-control', 'type': 'datetime-local'}
    ))
    end_date = forms.DateTimeField(label='До')
