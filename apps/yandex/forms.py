from django import forms
from .models import YandexUser

class PublicKeyForm(forms.ModelForm):
    class Meta:
        model = YandexUser
        fields = ['_public_key']  
        widgets = {
            'public_key': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите публичный ключ'}),
        }
        labels = {
            'public_key': 'Публичный ключ',
        }

