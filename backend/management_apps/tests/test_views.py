from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import BlogPost, Service, Testimonial, Contact, FAQ, AboutUs, Portfolio
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogPostViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('blogpost-list')

    def test_list_blogposts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_blogpost(self):
        data = {"title": "Test Blog", "content": "This is a test blog content"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ServiceViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('service-list')

    def test_list_services(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_service(self):
        data = {"name": "Test Service", "description": "This is a test service"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestimonialViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('testimonial-list')

    def test_list_testimonials(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_testimonial(self):
        data = {"author": "John Doe", "content": "This is a test testimonial"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ContactViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('contact-list')

    def test_list_contacts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_contact(self):
        data = {"name": "John Doe", "email": "johndoe@example.com", "message": "This is a test contact"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class FAQViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('faq-list')

    def test_list_faqs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_faq(self):
        data = {"question": "What is this?", "answer": "This is a test FAQ"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class AboutUsViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('aboutus-list')

    def test_list_aboutus(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_aboutus(self):
        data = {"description": "This is about us"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PortfolioViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('portfolio-list')

    def test_list_portfolios(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_portfolio(self):
        data = {"title": "Test Portfolio", "description": "This is a test portfolio"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CustomLoginViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('custom-login')
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass123')

    def test_login_success(self):
        data = {'email': 'testuser@example.com', 'password': 'testpass123'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)

    def test_login_failure(self):
        data = {'email': 'wronguser@example.com', 'password': 'wrongpass123'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)