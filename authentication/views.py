from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('signin') # to redirect to the given page after signup is done.

# inheriting the LoginView class
class Login(LoginView):
    template_name = 'login.html'