import uuid

from django.db import models


class Lead(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        CONTACTED = "contacted", "Contacted"
        CONVERTED = "converted", "Converted"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    pain_area = models.CharField(max_length=255)
    pain_severity = models.CharField(max_length=255)
    pain_duration = models.CharField(max_length=255)
    treatments = models.JSONField(default=list, blank=True)
    country = models.CharField(max_length=255)
    travel_date = models.DateField()
    urgency = models.CharField(max_length=255)
    stay_length = models.CharField(max_length=255)
    budget = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    notes = models.TextField(blank=True, default="")
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.full_name} ({self.email})"
