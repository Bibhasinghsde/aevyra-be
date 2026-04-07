from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "country",
        "status",
        "score",
        "created_at",
    )
    list_filter = ("status", "country", "created_at")
    search_fields = ("full_name", "email", "phone", "country")
    ordering = ("-created_at",)
