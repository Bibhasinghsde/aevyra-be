import django_filters

from .models import Lead


class LeadFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name="status")

    class Meta:
        model = Lead
        fields = ["status"]
