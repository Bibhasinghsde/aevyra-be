from rest_framework import serializers

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            "id",
            "created_at",
            "updated_at",
            "full_name",
            "email",
            "phone",
            "pain_area",
            "pain_severity",
            "pain_duration",
            "treatments",
            "country",
            "travel_date",
            "urgency",
            "stay_length",
            "budget",
            "status",
            "notes",
            "score",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_treatments(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Treatments must be a list.")
        if any(not isinstance(item, str) for item in value):
            raise serializers.ValidationError("Each treatment must be a string.")
        return value
