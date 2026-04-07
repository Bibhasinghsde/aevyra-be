from django.urls import path

from .views import LeadDetailApiView, LeadListCreateApiView

urlpatterns = [
    path("", LeadListCreateApiView.as_view(), name="lead-list"),
    path("<uuid:lead_id>/", LeadDetailApiView.as_view(), name="lead-detail"),
]