from django.db import models
from django.utils import timezone


# A model for the compliance standard or regulation
class Standard(models.Model):
    standard_name = models.CharField(max_length=100)
    standard_abbreviation = models.CharField(max_length=10)
    standard_organization = models.CharField(max_length=100)
    standard_description = models.TextField()
    standard_source = models.URLField()
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.standard_name

    class Meta:
        verbose_name_plural = "Standards"
        ordering = ["standard_name"]


class PCIRequirement(models.Model):
    standard = models.ForeignKey(
        Standard,
        on_delete=models.CASCADE,
        related_name="pci_requirements",
    )
    requirement_number = models.IntegerField()
    requirement_description = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.requirement_number} - {self.requirement_description} - {self.standard}"

    class Meta:
        verbose_name_plural = "PCI Requirements"
        ordering = ["standard", "requirement_number"]


class PCIChecklistItem(models.Model):
    item_description = models.TextField()
    checklist_number = models.IntegerField(
        default=1, help_text="The importance of the item"
    )
    requirement = models.ForeignKey(
        PCIRequirement, on_delete=models.CASCADE, related_name="pci_items"
    )
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.item_description}"

    class Meta:
        verbose_name_plural = "PCI Checklist Items"
        ordering = ["requirement", "checklist_number"]


class PCIChecklistResponse(models.Model):
    checklist_item = models.ForeignKey(PCIChecklistItem, on_delete=models.CASCADE)
    requirement = models.ForeignKey(
        PCIRequirement,
        on_delete=models.CASCADE,
        related_name="pci_responses",
        null=True,
        blank=True,
    )
    business = models.ForeignKey(
        "accounts.Business",
        on_delete=models.CASCADE,
        related_name="pci_responses",
        null=True,
        blank=True,
    )
    response_status = models.BooleanField(default=False)
    response_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.checklist_item}"

    def save(self, *args, **kwargs):
        self.requirement = self.checklist_item.requirement
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "PCI Checklist Response"
        verbose_name_plural = "PCI Checklist Responses"
        ordering = ["checklist_item"]


class HIPAARequirement(models.Model):
    standard = models.ForeignKey(
        Standard, on_delete=models.CASCADE, related_name="hipaa_requirements"
    )
    requirement_number = models.IntegerField()
    requirement_description = models.CharField(max_length=255)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.requirement_number} - {self.requirement_description} - {self.standard}"

    class Meta:
        verbose_name_plural = "HIPAA Requirements"
        ordering = ["standard", "requirement_number"]


class HIPAAChecklistItem(models.Model):
    item_description = models.CharField(max_length=255)

    requirement = models.ForeignKey(
        HIPAARequirement, on_delete=models.CASCADE, related_name="hipaa_items"
    )
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.item_description[:15]}"

    class Meta:
        verbose_name_plural = "HIPAA Checklist Items"
        ordering = ["requirement", "item_description"]


class HIPAAChecklistResponse(models.Model):
    checklist_item = models.ForeignKey(HIPAAChecklistItem, on_delete=models.CASCADE)
    requirement = models.ForeignKey(
        HIPAARequirement,
        on_delete=models.CASCADE,
        related_name="hipaa_responses",
        null=True,
        blank=True,
    )
    business = models.ForeignKey(
        "accounts.Business",
        on_delete=models.CASCADE,
        related_name="hipaa_responses",
        null=True,
        blank=True,
    )
    response_status = models.BooleanField(default=False)
    response_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.checklist_item}"

    def save(self, *args, **kwargs):
        self.requirement = self.checklist_item.requirement
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "HIPAA Checklist Responses"
        ordering = ["checklist_item"]


class ISO27001ControlGroup(models.Model):
    control_group_name = models.CharField(max_length=255)
    control_group_number = models.IntegerField()
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.control_group_number} - {self.control_group_name}"

    class Meta:
        verbose_name_plural = "ISO27001 Control Groups"
        ordering = ["control_group_number"]


class ISO27001ChecklistItem(models.Model):
    item_description = models.CharField(max_length=255)
    checklist_number = models.IntegerField(
        default=1, help_text="The importance of the item"
    )
    control_group = models.ForeignKey(
        ISO27001ControlGroup, on_delete=models.CASCADE, related_name="iso27k_items"
    )
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.checklist_number} {self.item_description[:15]}"

    class Meta:
        verbose_name_plural = "ISO27001 Checklist Items"
        ordering = ["control_group", "checklist_number"]


class ISO27001ChecklistResponse(models.Model):
    checklist_item = models.ForeignKey(ISO27001ChecklistItem, on_delete=models.CASCADE)
    control_group = models.ForeignKey(
        ISO27001ControlGroup,
        on_delete=models.CASCADE,
        related_name="iso_responses",
        null=True,
        blank=True,
    )
    business = models.ForeignKey(
        "accounts.Business",
        on_delete=models.CASCADE,
        related_name="iso_responses",
        null=True,
        blank=True,
    )
    response_status = models.BooleanField(default=False)
    response_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.checklist_item}"

    def save(self, *args, **kwargs):
        self.control_group = self.checklist_item.control_group
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "ISO27001 Checklist Responses"
        ordering = ["checklist_item"]
