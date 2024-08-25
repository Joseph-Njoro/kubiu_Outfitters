from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

CustomUser = get_user_model()

class CustomUserManagerTest(TestCase):
    
    def setUp(self):
        self.user_data = {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpass123'
        }
        self.superuser_data = {
            'email': 'admin@example.com',
            'first_name': 'Admin',
            'last_name': 'User',
            'password': 'adminpass123'
        }

    def test_create_user(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertEqual(user.last_name, self.user_data['last_name'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError) as context:
            # Explicitly pass only the required fields, omitting email from self.user_data
            CustomUser.objects.create_user(email=None, first_name=self.user_data['first_name'], 
                                           last_name=self.user_data['last_name'], password=self.user_data['password'])
        self.assertEqual(str(context.exception), 'The Email field must be set')


    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(**self.superuser_data)
        self.assertEqual(superuser.email, self.superuser_data['email'])
        self.assertEqual(superuser.first_name, self.superuser_data['first_name'])
        self.assertEqual(superuser.last_name, self.superuser_data['last_name'])
        self.assertTrue(superuser.check_password(self.superuser_data['password']))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_superuser_without_is_staff(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_superuser(is_staff=False, **self.superuser_data)
        self.assertEqual(str(context.exception), 'Superuser must have is_staff=True.')

    def test_create_superuser_without_is_superuser(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_superuser(is_superuser=False, **self.superuser_data)
        self.assertEqual(str(context.exception), 'Superuser must have is_superuser=True.')
