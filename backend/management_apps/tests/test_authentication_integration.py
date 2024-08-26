import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_user_authentication_flow():
    client = APIClient()
    credentials = {
        "username": "testuser",
        "password": "testpassword"
    }
    
    # Authenticate user
    response = client.post(reverse('token_obtain_pair'), credentials, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data

    # Test authenticated endpoint
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])
    response = client.get(reverse('protected-endpoint'))
    assert response.status_code == status.HTTP_200_OK