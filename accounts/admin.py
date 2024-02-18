from django.contrib import admin
from .models import Business, Contact


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("username", "business_name", "business_address", "business_phone")
    search_fields = ("business_name", "business_address", "business_phone")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("contact_name", "contact_email", "contact_message", "contact_phone")
    search_fields = ("contact_name", "contact_email", "contact_message")
