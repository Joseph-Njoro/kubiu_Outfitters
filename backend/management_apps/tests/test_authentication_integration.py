from datetime import timedelta
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class ProtectedViewTests(APITestCase):
    def setUp(self):
        # Create a user and obtain a JWT token for authenticated requests
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass',
            first_name='Test',
            last_name='User'
        )
        self.token = RefreshToken.for_user(self.user).access_token
        # Use the correct URL name
        self.protected_url = reverse('protected-endpoint')

    def test_protected_view_access(self):
        # Test accessing the protected view with a valid token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'You have access to this protected view!')

    def test_protected_view_no_auth(self):
        # Test accessing the protected view without a token
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_protected_view_invalid_token(self):
        # Test accessing the protected view with an invalid token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer invalidtoken')
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_protected_view_expired_token(self):
        # Create a refresh token for the user
        refresh = RefreshToken.for_user(self.user)
        access_token = refresh.access_token
        
        # Set token's expiration to the past
        expired_time = timezone.now() - timedelta(minutes=1)
        access_token.set_exp(from_time=expired_time, lifetime=timedelta(minutes=0))
        
        expired_token = str(access_token)
        
        # Add the expired token to the request
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {expired_token}')
        response = self.client.get(self.protected_url)
        
        # Assert that the response status code is 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)