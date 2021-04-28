from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
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
    if request.user.is_authenticated:
        context = {'username_is': request.user}
    else:
        context = {'username_is': 'Welcome!'}
    return render(request, 'home.html', context)

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

def contact(request):
    if request.user.is_authenticated:
        username_is = request.user
    else:
        username_is = 'Welcome!'

    context = {'username_is': username_is}
    return render(request, 'contact.html', context)

def destinations(request):
    if request.user.is_authenticated:
        username_is = request.user
    else:
        username_is = 'Welcome!'
    
    dests = Destination.objects.all()
    dests2 = Destination2.objects.all()
    dests3 = Destination3.objects.all()
    des = {}
    if request.method == 'POST':
         loc = request.POST.get('locations')
         if loc == 'Mexico':
             des = dests
         elif loc == 'Caribbean':
             des = dests2
         elif loc == 'Europe':
             des = dests3    
        

    context = {'des':des, 'username_is': username_is}
    return render(request, 'destinations.html', context)

def profile(request):
    if request.user.is_authenticated:
            username_is = request.user
    else:
        username_is = 'Welcome!'
    
    context = {'username_is': username_is}
    return render(request, 'profile.html', context)

def about(request):
    if request.user.is_authenticated:
            username_is = request.user
    else:
        username_is = 'Welcome!'

    context = {'username_is': username_is}
    return render(request, 'about.html', context)