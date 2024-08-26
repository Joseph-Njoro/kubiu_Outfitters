import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_contact_form_submission():
    client = APIClient()
    contact_data = {
        "name": "Test User",
        "email": "testuser@example.com",
        "message": "This is a test message."
    }
    
    # Submit contact form
    response = client.post(reverse('contact-list'), contact_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    # Assuming you have a way to check the contact form submission
    # For example, you could query the database or use mock objects