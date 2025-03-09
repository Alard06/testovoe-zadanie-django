from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='settings'),
    path('settings_public_key/', views.SettingsPublicKeyView.as_view(), name='settings_public_key'),
    path('files/', views.FilesView.as_view(), name='files'),
]
