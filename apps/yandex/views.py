from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import YandexUser
from .forms import PublicKeyForm
from utils.custom_decorators import login_required
from django.utils.decorators import method_decorator


class ProfileView(TemplateView):
    model = YandexUser
    template_name = 'yandex/settings_profile.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SettingsPublicKeyView(TemplateView):
    template_name = 'yandex/settings_public_key.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        yandex_user, created = YandexUser.objects.get_or_create(user=request.user)
        form = PublicKeyForm(instance=yandex_user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        yandex_user, created = YandexUser.objects.get_or_create(user=request.user)
        form = PublicKeyForm(request.POST, instance=yandex_user)
        if form.is_valid():
            form.save()
            return redirect('settings_public_key') 
        return render(request, self.template_name, {'form': form})

class FilesView(TemplateView):
    template_name = 'yandex/files.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

