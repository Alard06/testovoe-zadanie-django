from cryptography.fernet import Fernet
from django.conf import settings


def get_cipher() -> Fernet:
    """
    Возвращает объект шифрования Fernet, используя ключ из настроек Django.

    :return: Объект Fernet для шифрования и дешифрования.
    """
    key: str = settings.ENCRYPTION_KEY
    return Fernet(key)


def encrypt_data(data: str) -> str:
    """
    Шифрует строку данных.

    :param data: Строка данных для шифрования.
    :return: Зашифрованная строка в формате base64.
    """
    cipher: Fernet = get_cipher()
    encrypted_data: bytes = cipher.encrypt(data.encode())
    return encrypted_data.decode()


def decrypt_data(encrypted_data: str) -> str:
    """
    Дешифрует строку данных.

    :param encrypted_data: Зашифрованная строка в формате base64.
    :return: Расшифрованная строка.
    """
    cipher: Fernet = get_cipher()
    decrypted_data: bytes = cipher.decrypt(encrypted_data.encode())
    return decrypted_data.decode()