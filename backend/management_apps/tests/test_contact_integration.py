import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from management_apps.models import CustomUser  # Make sure this import matches your actual path

@pytest.mark.django_db
def test_contact_form_submission():
    client = APIClient()
    
    # Create and log in a user with all required fields
    user = CustomUser.objects.create_user(
        email='testuser@example.com',
        first_name='Test',
        last_name='User',
        password='testpass'
    )
    client.login(username='testuser@example.com', password='testpass')
    
    contact_data = {
        "name": "Test User",
        "email": "testuser@example.com",
        "message": "This is a test message."
    }
    
    # Submit contact form
    response = client.post(reverse('contact-list'), contact_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    # Additional assertions can be added here if needed