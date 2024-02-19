# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("pci_dss_compliance/", views.pci_dss_compliance, name="pci_dss_compliance"),
    path("pci_dss_report/", views.pci_dss_report, name="pci_dss_report"),
    path(
        "generate_pci_dss_report/",
        views.generate_pci_dss_report,
        name="generate_pci_dss_report",
    ),
    path("hipaa_compliance/", views.hipaa_compliance, name="hipaa_compliance"),
    path("hipaa_report/", views.hipaa_report, name="hipaa_report"),
    path(
        "generate_hipaa_report/",
        views.generate_hipaa_report,
        name="generate_hipaa_report",
    ),
    path("iso27k_compliance/", views.iso27k_compliance, name="iso27k_compliance"),
    path("iso27k_report/", views.iso27k_report, name="iso27k_report"),
    path(
        "generate_iso27k_report/",
        views.generate_iso27k_report,
        name="generate_iso27k_report",
    ),
]
