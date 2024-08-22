from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import BlogPost, Service, Testimonial, Contact, FAQ, AboutUs, Portfolio
from .serializers import (
    BlogPostSerializer, ServiceSerializer, TestimonialSerializer, 
    ContactSerializer, FAQSerializer, AboutUsSerializer, PortfolioSerializer
)

User = get_user_model()

class BlogPostViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )
        self.blog_post = BlogPost.objects.create(
            title='Test Blog Post',
            content='Content of the test blog post',
            author=self.user
        )
        self.url = reverse('blogpost-list')

    def test_list_blog_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Blog Post', str(response.content))

    def test_create_blog_post(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        data = {
            'title': 'New Blog Post',
            'content': 'Content of the new blog post',
            'author': self.user.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 2)
        self.assertEqual(BlogPost.objects.latest('id').title, 'New Blog Post')

class ServiceViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )
        self.service = Service.objects.create(
            title='Tailoring Service',
            description='Description of the tailoring service',
            price=100.00,
            created_by=self.user
        )
        self.url = reverse('service-list')

    def test_list_services(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Tailoring Service', str(response.content))

    def test_create_service(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        data = {
            'title': 'New Service',
            'description': 'Description of the new service',
            'price': 150.00,
            'created_by': self.user.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 2)
        self.assertEqual(Service.objects.latest('id').title, 'New Service')

class CustomLoginViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testlogin@example.com',
            password='testpassword',
            first_name='Test',
            last_name='Login'
        )
        self.url = reverse('custom-login')

    def test_login_success(self):
        data = {
            'email': 'testlogin@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Login successful', str(response.content))

    def test_login_failure(self):
        data = {
            'email': 'testlogin@example.com',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Invalid credentials', str(response.content))

# Similar tests can be written for TestimonialViewSet, ContactViewSet, FAQViewSet, AboutUsViewSet, and PortfolioViewSet
