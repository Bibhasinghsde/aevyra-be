from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from .filters import LeadFilter
from .models import Lead
from .serializers import LeadSerializer


class LeadListCreateApiView(APIView):
    filterset_class = LeadFilter
    search_fields = ["full_name", "email", "phone", "country"]
    ordering_fields = ["created_at", "score"]
    ordering = ["-created_at"]

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAdminUser()]

    def _build_queryset(self, request):
        queryset = Lead.objects.all()

        filter_backend = DjangoFilterBackend()
        queryset = filter_backend.filter_queryset(request, queryset, self)

        search_backend = filters.SearchFilter()
        queryset = search_backend.filter_queryset(request, queryset, self)

        ordering_backend = filters.OrderingFilter()
        return ordering_backend.filter_queryset(request, queryset, self)

    def get(self, request):
        queryset = self._build_queryset(request)
        paginator_class = api_settings.DEFAULT_PAGINATION_CLASS

        if paginator_class is None:
            serializer = LeadSerializer(queryset, many=True)
            return Response(serializer.data)

        paginator = paginator_class()
        page = paginator.paginate_queryset(queryset, request, view=self)
        serializer = LeadSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LeadDetailApiView(APIView):
    def get_permissions(self):
        return [IsAdminUser()]

    def get(self, request, lead_id):
        lead = get_object_or_404(Lead, id=lead_id)
        serializer = LeadSerializer(lead)
        return Response(serializer.data)

    def patch(self, request, lead_id):
        lead = get_object_or_404(Lead, id=lead_id)
        serializer = LeadSerializer(lead, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
