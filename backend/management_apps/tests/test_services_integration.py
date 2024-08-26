import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from management_apps.models import Service

@pytest.mark.django_db
def test_services_crud_operations():
    client = APIClient()
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
    response = client.get(reverse('service-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == "Test Service"

    # Update the service
    updated_data = {
        "name": "Updated Service",
        "description": "This is an updated service description."
    }
    response = client.put(reverse('service-detail', kwargs={'pk': 1}), updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert Service.objects.get().name == "Updated Service"

    # Delete the service
    response = client.delete(reverse('service-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Service.objects.count() == 0