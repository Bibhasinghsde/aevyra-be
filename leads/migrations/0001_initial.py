# Generated manually for initial project scaffold

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lead",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("full_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=255)),
                ("pain_area", models.CharField(max_length=255)),
                ("pain_severity", models.CharField(max_length=255)),
                ("pain_duration", models.CharField(max_length=255)),
                ("treatments", models.JSONField(blank=True, default=list)),
                ("country", models.CharField(max_length=255)),
                ("travel_date", models.DateField()),
                ("urgency", models.CharField(max_length=255)),
                ("stay_length", models.CharField(max_length=255)),
                ("budget", models.CharField(max_length=255)),
                ("status", models.CharField(choices=[("new", "New"), ("contacted", "Contacted"), ("converted", "Converted")], default="new", max_length=20)),
                ("notes", models.TextField(blank=True, default="")),
                ("score", models.IntegerField(default=0)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
