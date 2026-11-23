from django import forms
from .models import Event, RSVP

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date_time', 'location', 'description', 'private']
        widgets = {
            'date_time': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M', 
                attrs={'type': 'datetime-local'},
            ),
        }

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ('signup',)
