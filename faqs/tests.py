import pytest
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    client = APIClient()
    FAQ.objects.create(question="What is Django?", answer="A web framework", language="en")

    response = client.get("/api/faqs/?lang=hi")
    assert response.status_code == 200
    assert "Django" in response.data[0]["question"]
