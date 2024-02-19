from django.shortcuts import render
from .models import Standard
from accounts.decorators import user_required


def dashboard(request):
    template_name = "compliance_checker/dashboard.html"
    context = {"section": "dashboard"}
    return render(request, template_name, context)
