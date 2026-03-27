from django import forms
from django.forms import ModelForm
from .models import VoleyPlayer


class VoleyPlayerForm(ModelForm):
    class Meta:
        model = VoleyPlayer
        fields = '__all__'
        widgets = {
            'dateJoined': forms.DateInput(attrs={'type': 'date'})
        }