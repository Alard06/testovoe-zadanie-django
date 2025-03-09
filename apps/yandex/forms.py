from django import forms
from .models import YandexUser

class PublicKeyForm(forms.ModelForm):
    class Meta:
        model = YandexUser
        fields = ['public_key']
        labels = {
            'public_key': 'Публичный ключ',
        }
        widgets = {
            'public_key': forms.TextInput(attrs={'class': 'form-control'}),
        }