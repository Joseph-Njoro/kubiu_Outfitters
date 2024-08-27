import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from management_apps.models import Service
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_services_crud_operations():
    client = APIClient()

    # Create a user and get a JWT
    User = get_user_model()
    user = User.objects.create_user(
        email='testuser@example.com',
        password='testpassword',
        first_name='Test',
        last_name='User'
    )
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))

    # Provide all necessary fields as required by the serializer
    service_data = {
        "title": "Test Service",          # Correct field name
        "description": "This is a test service description.",
        "price": "9.99",                  # Ensure price is in string format for decimal fields
        "created_by": user.id             # Correct field name
    }

    # Create a service
    response = client.post(reverse('service-list'), service_data, format='json')
    print(f"Create Response: {response.status_code} - {response.data}")
    assert response.status_code == status.HTTP_201_CREATED
    assert Service.objects.count() == 1
    assert Service.objects.get().title == "Test Service"  # Ensure we're checking the correct field

    # Retrieve the service
    service_id = Service.objects.get().id
    response = client.get(reverse('service-detail', kwargs={'pk': service_id}))
    print(f"Retrieve Response: {response.status_code} - {response.data}")
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == "Test Service"  # Ensure we're checking the correct field

    # Update the service
    updated_data = {
        "title": "Updated Service",         # Correct field name
        "description": "This is an updated service description.",
        "price": "19.99",                   # Ensure price is in string format for decimal fields
        "created_by": user.id              # Correct field name
    }
    response = client.put(reverse('service-detail', kwargs={'pk': service_id}), updated_data, format='json')
    print(f"Update Response: {response.status_code} - {response.data}")
    assert response.status_code == status.HTTP_200_OK
    assert Service.objects.get().title == "Updated Service"  # Ensure we're checking the correct field

    # Delete the service
    response = client.delete(reverse('service-detail', kwargs={'pk': service_id}))
    print(f"Delete Response: {response.status_code}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Service.objects.count() == 0