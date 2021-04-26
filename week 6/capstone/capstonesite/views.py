from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def registration(request):
    form = RegistrationForm()

    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
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
        # else:
        #    return messages.info(request, 'Username or Password is Incorrect')
            
    form = {}
    return render(request, 'registration/login.html', form)

def logoutUser(request):
    logout(request)
    return redirect('login')

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
    context={}
    
    loc1 = Destination.objects.all()
    loc2 = Destination2.objects.all()
    loc3 = Destination3.objects.all()
   
    context = {'username_is': username_is, 'loc1': loc1, 'loc2': loc2, 'loc3': loc3}
    return render(request, 'profile.html', context)

def about(request):
    if request.user.is_authenticated:
            username_is = request.user
    else:
        username_is = 'Welcome!'

    context = {'username_is': username_is}
    return render(request, 'about.html', context)

def fav_dest(request):
    dest = {}
    
    if request.method == 'POST':
         tab = request.POST.get('table')
         if 'Destination3' in tab:
             dest = Destination3.objects.all()
             
         elif 'Destination2' in tab:
             dest = Destination2.objects.all()
         else:
             dest = Destination.objects.all() 
    wish = get_object_or_404(dest, id=request.POST.get('fav_dest'))
    wish.fav.add(request.user)
    
    return redirect('profile')
    
    
