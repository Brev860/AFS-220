from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from .models import *



# Create your views here.


def registration(response):
    form = UserCreationForm(response.POST)

    if response.method == 'POST':
        if form.is_valid():
            form.save()
       
    return render(response, 'registration/registration.html', {'form': form})

def home(request):
    return render(request, 'home.html')
    

