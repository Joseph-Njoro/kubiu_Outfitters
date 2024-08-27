import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from management_apps.models import Service
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # Correct import for Token

@pytest.mark.django_db
def test_services_crud_operations():
    client = APIClient()

    # Create a user and get an auth token
    User = get_user_model()
    user = User.objects.create_user(
        email='testuser@example.com',
        password='testpassword',
        first_name='Test',
        last_name='User'
    )
    token = Token.objects.create(user=user)  # Ensure the Token model is correctly used
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    service_data = {
        "name": "Test Service",
        "description": "This is a test service description."
    }
    
    # Create a service
    response = client.post(reverse('service-list'), service_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Service.objects.count() == 1
    assert Service.objects.get().name == "Test Service"

    # Retrieve the service
    service_id = Service.objects.get().id
    response = client.get(reverse('service-detail', kwargs={'pk': service_id}))
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == "Test Service"

    # Update the service
    updated_data = {
        "name": "Updated Service",
        "description": "This is an updated service description."
    }
    response = client.put(reverse('service-detail', kwargs={'pk': service_id}), updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert Service.objects.get().name == "Updated Service"

    # Delete the service
    response = client.delete(reverse('service-detail', kwargs={'pk': service_id}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Service.objects.count() == 0
