from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from utils.custom_decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(TemplateView):
    template_name = 'main/index.html'

class LogoutView(TemplateView):
    template_name = 'main/logout.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class RegisterView(CreateView):
    model = User
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm



class LoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('index')
    form_class = AuthenticationForm

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


