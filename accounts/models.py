from django.db import models
from django.contrib.auth.models import AbstractUser


class Business(AbstractUser):
    """
    A model for the business or company with the following fields:
    - username
    - email
    - business_name
    - business_address
    - business_phone
    - business_website
    """

    business_name = models.CharField(
        max_length=100,
        help_text="Enter your business name as per the registration certificate",
    )
    business_address = models.TextField()
    business_phone = models.CharField(
        max_length=100, help_text="Enter your business phone number"
    )
    business_website = models.URLField(
        max_length=100,
        help_text="Enter the URL of your business website i.e. https://www.example.com",
    )

    def __str__(self):
        return self.business_name

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ["business_name"]


class Contact(models.Model):
    """
    A model for the contact form with the following fields:
    - contact_name
    - contact_email
    - contact_phone
    - contact_message
    """

    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    contact_message = models.TextField()

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name_plural = "Contacts"
        ordering = ["contact_email", "contact_name"]
