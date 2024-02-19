from django.contrib import admin
from .models import (
    Standard,
    PCIRequirement,
    PCIChecklistItem,
    HIPAARequirement,
    HIPAAChecklistItem,
    ISO27001ControlGroup,
    ISO27001ChecklistItem,
)


@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ("standard_name", "standard_organization", "added_at")
    list_filter = ("standard_organization",)
    search_fields = ("standard_name", "standard_organization")
    date_hierarchy = "added_at"
    ordering = ("standard_name",)


@admin.register(PCIRequirement)
class PCIRequirementAdmin(admin.ModelAdmin):
    list_display = ("requirement_number", "standard", "added_at")
    list_filter = ("standard",)
    search_fields = ("requirement_number", "standard")
    date_hierarchy = "added_at"
    ordering = ("standard", "requirement_number")


@admin.register(PCIChecklistItem)
class PCIChecklistItemAdmin(admin.ModelAdmin):
    list_display = ("get_requirement_number", "checklist_number", "added_at")
    list_filter = ("requirement",)
    search_fields = ("item_description", "requirement")
    date_hierarchy = "added_at"
    ordering = ("requirement", "checklist_number")

    def get_requirement_number(self, obj):
        return obj.requirement.requirement_number

    get_requirement_number.short_description = (
        "Requirement Number"  # Sets column name in admin panel
    )


@admin.register(HIPAARequirement)
class HIPAARuleAdmin(admin.ModelAdmin):
    list_display = ("requirement_number", "rule_title", "added_at")
    list_filter = ("requirement_number",)
    search_fields = ("requirement_number", "rule_title")
    date_hierarchy = "added_at"
    ordering = ("requirement_number",)


@admin.register(HIPAAChecklistItem)
class HIPAAChecklistItemAdmin(admin.ModelAdmin):
    list_display = ("get_requirement_number", "item_description", "added_at")
    list_filter = ("rule",)
    search_fields = ("item_description", "rule")
    date_hierarchy = "added_at"
    ordering = ("rule",)

    def get_requirement_number(self, obj):
        return obj.rule.requirement_number

    get_requirement_number.short_description = (
        "Rule Number"  # Sets column name in admin panel
    )


@admin.register(ISO27001ControlGroup)
class ISO27001ControlGroupAdmin(admin.ModelAdmin):
    list_display = ("control_group_number","control_group_name", "added_at")
    search_fields = ("control_group_name",)
    date_hierarchy = "added_at"
    ordering = ("control_group_name",)


@admin.register(ISO27001ChecklistItem)
class ISO27001ChecklistItemAdmin(admin.ModelAdmin):
    list_display = ("get_control_group_number", "checklist_number", "added_at")
    list_filter = ("control_group",)
    search_fields = ("item_description", "control_group")
    date_hierarchy = "added_at"
    ordering = ("control_group", "checklist_number")

    def get_control_group_number(self, obj):
        return obj.control_group.control_group_number

    get_control_group_number.short_description = (
        "Control Group Number"  # Sets column name in admin panel
    )
