from django.shortcuts import render, redirect

from compliance_checker import renderers
from .models import (
    Standard,
    PCIRequirement,
    PCIChecklistItem,
    PCIChecklistResponse,
    HIPAARequirement,
    HIPAAChecklistItem,
    HIPAAChecklistResponse,
    ISO27001ControlGroup,
    ISO27001ChecklistItem,
    ISO27001ChecklistResponse,
)
from accounts.decorators import user_required
from django.contrib import messages


@user_required
def dashboard(request):
    business = request.user
    total_compliance_percentage = (
        business.get_pci_compliance_percentage
        + business.get_hipaa_compliance_percentage
        + business.get_iso27k_compliance_percentage
    ) / 3
    total_non_compliance_percentage = 100 - total_compliance_percentage

    template_name = "compliance_checker/dashboard.html"
    context = {
        "section": "dashboard",
        "total_compliance_percentage": total_compliance_percentage,
        "total_non_compliance_percentage": total_non_compliance_percentage,
    }
    return render(request, template_name, context)


@user_required
def pci_dss_compliance(request):
    business = request.user
    pci_checklist_items = PCIChecklistItem.objects.all()
    pci_requirements = PCIRequirement.objects.all()

    if request.method == "POST":
        checked_items = request.POST.getlist("checklist_items")
        for item in pci_checklist_items:
            response, created = PCIChecklistResponse.objects.get_or_create(
                checklist_item=item,
                business=business,
            )
            response.response_status = str(item.id) in checked_items
            response.save()

        messages.success(
            request, "PCI DSS Compliance checklist submitted successfully."
        )

        return redirect("pci_dss_report")

    template_name = "compliance_checker/pci_dss_compliance.html"
    context = {"pci_requirements": pci_requirements, "section": "pci_dss_compliance"}
    return render(request, template_name, context)


@user_required
def pci_dss_report(request):
    business = request.user
    pci_responses = PCIChecklistResponse.objects.filter(business=business)

    template_name = "compliance_checker/pci_dss_report.html"
    context = {"pci_responses": pci_responses, "section": "pci_dss_report"}
    return render(request, template_name, context)


@user_required
def generate_pci_dss_report(request):
    business = request.user
    pci_responses = PCIChecklistResponse.objects.filter(business=business)

    template_name = "compliance_checker/pci_dss_report_pdf.html"
    data = {
        "pci_responses": pci_responses,
        "business": business,
    }
    return renderers.render_to_pdf(template_name, data)


@user_required
def hipaa_compliance(request):
    hipaa_requirements = HIPAARequirement.objects.all()
    hipaa_checklist_items = HIPAAChecklistItem.objects.all()

    if request.method == "POST":
        checked_items = request.POST.getlist("checklist_items")
        for item in hipaa_checklist_items:
            response, created = HIPAAChecklistResponse.objects.get_or_create(
                checklist_item=item,
                business=request.user,
            )
            response.response_status = str(item.id) in checked_items
            response.save()

        messages.success(request, "HIPAA Compliance checklist submitted successfully.")

        return redirect("hipaa_report")

    template_name = "compliance_checker/hipaa_compliance.html"
    context = {"hipaa_requirements": hipaa_requirements, "section": "hipaa_compliance"}
    return render(request, template_name, context)


@user_required
def hipaa_report(request):
    business = request.user
    hipaa_responses = HIPAAChecklistResponse.objects.filter(business=business)

    template_name = "compliance_checker/hipaa_report.html"
    context = {"hipaa_responses": hipaa_responses, "section": "hipaa_report"}
    return render(request, template_name, context)


@user_required
def generate_hipaa_report(request):
    business = request.user
    hipaa_responses = HIPAAChecklistResponse.objects.filter(business=business)

    template_name = "compliance_checker/hipaa_report_pdf.html"
    data = {
        "hipaa_responses": hipaa_responses,
        "business": business,
    }
    return renderers.render_to_pdf(template_name, data)


@user_required
def iso27k_compliance(request):
    iso27k_control_groups = ISO27001ControlGroup.objects.all()
    iso27k_checklist_items = ISO27001ChecklistItem.objects.all()

    if request.method == "POST":
        checked_items = request.POST.getlist("checklist_items")
        for item in iso27k_checklist_items:
            response, created = ISO27001ChecklistResponse.objects.get_or_create(
                checklist_item=item,
                business=request.user,
            )
            response.response_status = str(item.id) in checked_items
            response.save()

        messages.success(
            request, "ISO 27001 Compliance checklist submitted successfully."
        )

        return redirect("iso27k_report")

    template_name = "compliance_checker/iso27k_compliance.html"
    context = {
        "iso27k_control_groups": iso27k_control_groups,
        "section": "iso27k_compliance",
    }
    return render(request, template_name, context)


@user_required
def iso27k_report(request):
    business = request.user
    iso27k_responses = ISO27001ChecklistResponse.objects.filter(business=business)

    template_name = "compliance_checker/iso27k_report.html"
    context = {"iso27k_responses": iso27k_responses, "section": "iso27k_report"}
    return render(request, template_name, context)


@user_required
def generate_iso27k_report(request):
    business = request.user
    iso27k_responses = ISO27001ChecklistResponse.objects.filter(business=business)

    template_name = "compliance_checker/iso27k_report_pdf.html"
    data = {
        "iso27k_responses": iso27k_responses,
        "business": business,
    }
    return renderers.render_to_pdf(template_name, data)
