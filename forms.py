from django import forms
from django.contrib.auth.models import User
from . import models

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class EventForm(forms.ModelForm):
    class Meta:
        model=models.Event
        fields=['name','date','time','venue','email','image','requirements','odyesno']
