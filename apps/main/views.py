from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

class RegisterView(TemplateView):
    template_name = 'main/register.html'

class LoginView(TemplateView):
    template_name = 'main/login.html'

class LogoutView(TemplateView):
    template_name = 'main/logout.html'

class SettingsView(TemplateView):
    template_name = 'main/settings.html'
