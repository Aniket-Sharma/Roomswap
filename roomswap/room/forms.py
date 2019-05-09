from django import forms
from .models import room
from django.conf import settings

class SignUpForm(forms.ModelForm):
    class Meta:
        model = room
        fields = ('hostel', 'room_no', 'desire', 'contact',)

    hostel = forms.ChoiceField(choices=settings.HOSTEL_CHOICES)
    room_no = forms.CharField(help_text='Enter your current room nummber',
                              widget=forms.TextInput(attrs={'placeholder': 'Your current room number'}))