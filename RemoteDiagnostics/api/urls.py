from django.urls import path
from .views import EventCreateAPIView

urlpatterns = [
    path('addEvent/', EventCreateAPIView.as_view(), name='add-event'),
]
