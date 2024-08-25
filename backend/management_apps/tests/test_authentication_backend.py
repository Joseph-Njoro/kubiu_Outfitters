from django.test import TestCase
from management_apps.authentication_backend import EmailBackend
from management_apps.models import CustomUser

class TestAuthenticationBackend(TestCase):
    def setUp(self):
        # Update create_user to include first_name and last_name
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            first_name='Test',
            last_name='User',
            password='12345'
        )

    def test_authenticate_valid_user(self):
        backend = EmailBackend()
        user = backend.authenticate(request=None, email='test@example.com', password='12345')
        self.assertEqual(user, self.user)

    def test_authenticate_invalid_user(self):
        backend = EmailBackend()
        user = backend.authenticate(request=None, email='invalid@example.com', password='wrongpassword')
        self.assertIsNone(user)

    def test_get_user(self):
        backend = EmailBackend()
        user = backend.get_user(self.user.pk)
        self.assertEqual(user, self.user)

    def test_get_user_invalid_id(self):
        backend = EmailBackend()
        user = backend.get_user(999)  # Assuming 999 is an invalid ID
        self.assertIsNone(user)
