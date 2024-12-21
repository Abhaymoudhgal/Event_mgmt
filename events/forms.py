from django import forms
from .models import Event, Attendee, Task

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'date']

class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'deadline', 'status', 'assigned_attendee']