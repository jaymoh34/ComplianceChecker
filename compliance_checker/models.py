from django.db import models
from django.utils import timezone


# A model for the compliance standard or regulation
class Standard(models.Model):
    standard_name = models.CharField(max_length=100)
    standard_organization = models.CharField(max_length=100)
    standard_description = models.TextField()
    standard_source = models.URLField()
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.standard_name

    class Meta:
        verbose_name_plural = "Standards"
        ordering = ["standard_name"]


class ChecklistItem(models.Model):
    text = models.CharField(max_length=200)
    weight = models.IntegerField(default=1, help_text="The importance of the item")
    standard = models.ForeignKey(
        Standard, on_delete=models.CASCADE, related_name="items"
    )
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Checklist Items"
        ordering = ["standard", "text"]


class ChecklistResponse(models.Model):
    checklist_item = models.OneToOneField(ChecklistItem, on_delete=models.CASCADE)
    STATUS = (
        ("P", "Pending"),  # Not answered yet
        ("C", "Completed"),  # Answered and compliant
        ("N", "Non-compliant"),  # Answered and non-compliant
    )

    status = models.CharField(max_length=1, choices=STATUS, default="P")
    item = models.ForeignKey(
        ChecklistItem, on_delete=models.CASCADE, related_name="responses"
    )
    checked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.item}"

    class Meta:
        verbose_name_plural = "Checklist Responses"
        ordering = ["checklist_item"]
