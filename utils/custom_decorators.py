from django.shortcuts import redirect
from functools import wraps


def login_required(view_function):
    """
    Декоратор для проверки авторизации пользователя
    """
    @wraps(view_function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapper