from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views.generic import TemplateView, RedirectView, CreateView
from django.views import View
from home.forms import LoginForm, SignupForm
from users.models import User
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse_lazy

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class LogoutView(LogoutView):
    template_name = ''

class SignupView(CreateView):
    model = User
    template_name = "signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('login')
