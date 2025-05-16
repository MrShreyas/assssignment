from django.urls import path
from .views import get_reminders, create_reminder

urlpatterns = [
    path('reminders/', get_reminders, name='get_reminders'),
    path('reminders/create/', create_reminder, name='create_reminder')
]
