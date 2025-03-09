from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import YandexUser
from .forms import PublicKeyForm
from utils.custom_decorators import login_required
from django.utils.decorators import method_decorator
from utils.yandex_data import get_yandex_files
import asyncio
from django.core.cache import cache
from core.settings import CACHE_TTL
from django.utils.dateparse import parse_datetime
from typing import Any
from django.http import HttpRequest, HttpResponse

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
            old_cache_key = f"yandex_files_{yandex_user.public_key}"
            cache.delete(old_cache_key)
            yandex_user.public_key = form.cleaned_data['_public_key']
            yandex_user.save()

            return redirect('index')
        return render(request, self.template_name, {'form': form})
    


class FilesView(TemplateView):
    template_name = 'yandex/files.html'

    @method_decorator(login_required)
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        yandex_user, created = YandexUser.objects.get_or_create(user=request.user)
        if not yandex_user.public_key:
            return render(request, self.template_name, {'files': []})

        sort_by = request.GET.get('sort', 'name')
        file_type = request.GET.get('type', None)  
        cache_key = f"yandex_files_{yandex_user.public_key}_{sort_by}_{file_type if file_type else 'all'}"

        files = cache.get(cache_key)

        if files is None:
            files = asyncio.run(get_yandex_files(yandex_user.public_key))
            files = files.get('items', [])

            if file_type:
                files = [file for file in files if file.get('name', '').endswith(f".{file_type}")]

            if sort_by == 'type':
                files.sort(key=lambda x: x.get('name', '').split('.')[-1])
            elif sort_by == 'size':
                files.sort(key=lambda x: x.get('size', 0))
            elif sort_by == 'created':
                files.sort(key=lambda x: parse_datetime(x.get('created', '')))
            else:
                files.sort(key=lambda x: x.get('name', ''))

            cache.set(cache_key, files, timeout=60 * 3)  

        return render(request, self.template_name, {
            'files': files,
            'sort_by': sort_by,
            'selected_type': file_type,  
        })