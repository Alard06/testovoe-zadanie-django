from django.shortcuts import redirect
from functools import wraps
from django.http import HttpRequest, HttpResponse
from typing import Callable, Any


def login_required(view_function: Callable[[HttpRequest, Any], HttpResponse]) -> Callable[[HttpRequest, Any], HttpResponse]:
    """
    Декоратор для проверки авторизации пользователя.

    :param view_function: Функция представления, которую нужно обернуть.
    :return: Обернутая функция, которая проверяет авторизацию пользователя.
    """
    @wraps(view_function)
    def wrapper(request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapper