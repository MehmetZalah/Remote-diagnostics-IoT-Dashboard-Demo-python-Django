from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ('temperature', 'Temperature'),
        ('vibration', 'Vibration'),
    ]
    EventType = models.CharField(max_length=20, choices=EVENT_TYPES)
    EventValue = models.FloatField()
    EventDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.EventType}: {self.EventValue} at {self.EventDateTime}'