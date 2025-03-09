from django.db import models
from django.contrib.auth.models import User
from utils.encryption import encrypt_data, decrypt_data
from cryptography.fernet import InvalidToken


class YandexUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    _public_key = models.CharField(max_length=255, db_column='public_key', blank=True, default="")

    @property
    def public_key(self):
        """Расшифрованный публичный ключ."""
        if not self._public_key:
            return "" 
        try:
            return decrypt_data(self._public_key)
        except InvalidToken:
            return ""  

    @public_key.setter
    def public_key(self, value):
        """Шифрование публичного ключа перед сохранением."""
        if value: 
            self._public_key = encrypt_data(value)
        else:
            self._public_key = "" 
            
    def __str__(self):
        return f"{self.user.username} - {self.public_key}"