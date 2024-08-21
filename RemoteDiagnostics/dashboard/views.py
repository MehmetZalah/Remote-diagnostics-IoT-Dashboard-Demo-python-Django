from django.shortcuts import render
from .models import Event

def dashboard_view(request):

    last_temperature = Event.objects.filter(EventType='temperature').order_by('-EventDateTime').first()
    last_vibration = Event.objects.filter(EventType='vibration').order_by('-EventDateTime').first()

    context = {
    'last_temperature': last_temperature.EventValue if last_temperature else 'No data',
    'last_temperature_datetime' : str(last_temperature.EventDateTime).split('.')[0] if last_temperature else 'No data',
    'last_vibration': last_vibration.EventValue if last_vibration else 'No data',
    'last_vibration_datetime' : str(last_vibration.EventDateTime).split('.')[0] if last_vibration else 'No data',
    }

    return render(request, 'dashboard/dashboard.html', context)
