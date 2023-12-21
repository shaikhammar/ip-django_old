from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views.generic import TemplateView, RedirectView
from django.views import View
from home.forms import LoginForm, SignupForm
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class LogoutView(LogoutView):
    template_name = ''

class SignupView(TemplateView):
    form_class = SignupForm
    template_name = 'signup.html'