from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def registration(request):
    form = UserCreationForm()

    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    return render(request, 'registration/registration.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = authenticate(username = username , password = password)
        
        if user is not None:
           
            login(request, user)
            return redirect('home')
    form = {}
    return render(request, 'registration/login.html', form)
   