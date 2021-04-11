from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('registration',views.registration , name='registration'),
    path('login', views.loginPage, name='login'),
    path('',views.home, name='home')
]
