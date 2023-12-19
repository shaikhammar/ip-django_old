from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views import View
from home.forms import LoginForm

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

class HomeView(TemplateView):
    template_name = 'home.html'
