from cryptography.fernet import Fernet
import base64
import os
from django.conf import settings

def get_cipher():
    key = settings.ENCRYPTION_KEY
    return Fernet(key)

def encrypt_data(data: str) -> str:
    cipher = get_cipher()
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data.decode()

def decrypt_data(encrypted_data: str) -> str:
    cipher = get_cipher()
    decrypted_data = cipher.decrypt(encrypted_data.encode())
    return decrypted_data.decode()
