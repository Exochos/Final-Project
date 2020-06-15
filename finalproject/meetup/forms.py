from django import forms
from .models import *

class MeetUpForm(forms.ModelForm):
    class Meta:
        model=MeetUp
        fields='__all__'

class ActivityForm(forms.ModelForm):
    class Meta:
        model=Activity
        fields='__all__'
