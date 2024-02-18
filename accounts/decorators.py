from django.shortcuts import redirect
from django.contrib import messages


def user_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            # User is authenticated, allow access to the view.
            return view_func(request, *args, **kwargs)
        else:
            # User is not authenticated, redirect to the login view.
            messages.error(
                request,
                "You need to log in first to access the page you requested.",
            )
            return redirect(
                "login"
            )  # Replace with the actual URL name of the login view.

    return wrapper


def guest_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # User is not authenticated (guest user), allow access to the view.
            return view_func(request, *args, **kwargs)
        else:
            # User is authenticated, redirect to the home view.
            messages.error(
                request,
                "You are already logged in. You need to log out first to access this page.",
            )
            return redirect(
                "home"
            )  # Replace with the actual URL name of the home view.

    return wrapper
