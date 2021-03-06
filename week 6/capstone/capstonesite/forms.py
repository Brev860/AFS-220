from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

Locations = ['Mexico', 'Caribbean', 'Europe']


class RegistrationForm(UserCreationForm):
  
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email', 'message']
    
 