from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Lead


class LeadApiTests(APITestCase):
    def setUp(self):
        self.list_url = reverse("lead-list")
        self.payload = {
            "full_name": "John Doe",
            "email": "john@example.com",
            "phone": "+1 234 567 890",
            "pain_area": "Stress Relief",
            "pain_severity": "Moderate",
            "pain_duration": "3 Months",
            "treatments": ["Yoga", "Meditation"],
            "country": "Thailand",
            "travel_date": "2026-04-20",
            "urgency": "Flexible",
            "stay_length": "1 Week",
            "budget": "$2,000 - $4,000",
        }

    def test_public_user_can_create_lead(self):
        response = self.client.post(self.list_url, self.payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lead.objects.count(), 1)
        self.assertEqual(Lead.objects.first().status, Lead.Status.NEW)

    def test_staff_user_can_list_leads(self):
        Lead.objects.create(**self.payload)
        user = get_user_model().objects.create_user(
            username="admin",
            email="admin@example.com",
            password="strong-password-123",
            is_staff=True,
        )
        self.client.force_authenticate(user=user)

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_anonymous_user_cannot_list_leads(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
