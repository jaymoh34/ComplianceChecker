from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from accounts.forms import CompanyCreationForm, AuthenticationForm, ContactForm
from django.contrib import messages
from .decorators import guest_required, user_required
from bs4 import BeautifulSoup


@guest_required
def signup_business(request):
    if request.method == "POST":
        form = CompanyCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("login_business")
        else:
            errors = str()
            for key, value in form.errors.items():
                soup = BeautifulSoup(str(value), "html.parser")
                errors += f"{key.title()}: {soup.get_text()}<br>"

            messages.error(request, errors)
    else:
        form = CompanyCreationForm()

    template_name = "registration/signup.html"
    context = {"form": form, "section": "signup"}
    return render(request, template_name, context)


@guest_required
def login_business(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            business = authenticate(request, username=username, password=password)

            if business is not None:
                login(request, business)
                messages.success(request, f"Welcome back, {username}")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
                
        else:
            errors = str()
            for key, value in form.errors.items():
                soup = BeautifulSoup(str(value), "html.parser")
                errors += f"{key.title()}: {soup.get_text()}<br>"

        messages.error(request, "Invalid username or password")

    context = {"section": "login"}
    template_name = "registration/login.html"
    return render(request, template_name, context)


def logout_business(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect("login_business")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully")
            return redirect("contact")
        else:
            errors = list()
            for key, value in form.errors.items():
                errors.append(f"{key}: {value}")

            messages.error(request, errors)

    return redirect("home")
