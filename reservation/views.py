from django.shortcuts import render
from .forms import *


# Create your views here.
def reservation(request):
    return render(request, 'reservation/reservation.html')


# Create your views here.
def reservation_django(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AppointmentForm()
    return render(request, 'reservation/reservation_django.html', {'form': form})


def reservation_max(request):
    return render(request, 'reservation/index.html')