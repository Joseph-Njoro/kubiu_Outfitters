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
            CustomUser.objects.create_user(email=None, first_name=self.user_data['first_name'], 
                                           last_name=self.user_data['last_name'], password=self.user_data['password'])
        self.assertEqual(str(context.exception), 'The Email field must be set')

    def test_create_user_without_first_name(self):
        with self.assertRaises(TypeError):  # TypeError raised because the required argument is missing
            CustomUser.objects.create_user(email=self.user_data['email'], last_name=self.user_data['last_name'], password=self.user_data['password'])

    def test_create_user_without_last_name(self):
        with self.assertRaises(TypeError):  # TypeError raised because the required argument is missing
            CustomUser.objects.create_user(email=self.user_data['email'], first_name=self.user_data['first_name'], password=self.user_data['password'])

    def test_create_user_with_duplicate_email(self):
        CustomUser.objects.create_user(**self.user_data)
        with self.assertRaises(ValidationError):
            CustomUser.objects.create_user(**self.user_data)  # Try creating another user with the same email

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

    def test_create_superuser_without_first_name(self):
        with self.assertRaises(TypeError):
            CustomUser.objects.create_superuser(email=self.superuser_data['email'], last_name=self.superuser_data['last_name'], password=self.superuser_data['password'])

    def test_create_superuser_without_last_name(self):
        with self.assertRaises(TypeError):
            CustomUser.objects.create_superuser(email=self.superuser_data['email'], first_name=self.superuser_data['first_name'], password=self.superuser_data['password'])

    def test_create_superuser_with_missing_is_staff_and_is_superuser(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_superuser(is_staff=False, is_superuser=False, **self.superuser_data)
        self.assertEqual(str(context.exception), 'Superuser must have is_staff=True. Superuser must have is_superuser=True.')
