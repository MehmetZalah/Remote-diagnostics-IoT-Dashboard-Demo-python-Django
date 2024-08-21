from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dashboard.models import Event

class EventCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        temperature_value = request.data.get('temperature')
        vibration_value = request.data.get('vibration')

        if temperature_value is not None:
            Event.objects.create(EventType='temperature', EventValue=temperature_value)
        
        if vibration_value is not None:
            Event.objects.create(EventType='vibration', EventValue=vibration_value)

        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)