from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Business, Contact


class CompanyCreationForm(UserCreationForm):
    class Meta:
        model = Business
        fields = (
            "username",
            "email",
            "business_name",
            "business_address",
            "business_phone",
            "business_website",
            "password1",
            "password2",
        )
        labels = {
            "username": "Business Registration Number",
            "email": "Business Email",
            "business_phone": "Business Phone Number",
            "business_website": "Business Website",
        }
        widgets = {
            "business_address": forms.Textarea(attrs={"rows": 2}),
        }


class CompanyLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=63, label="Business Registration Number")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("contact_name", "contact_email", "contact_phone", "contact_message")
        widgets = {
            "contact_message": forms.Textarea(attrs={"rows": 3}),
        }
