from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from management_apps.models import (
    BlogPost, Service, Testimonial, Contact, FAQ, AboutUs, Portfolio
)
from management_apps.serializers import (
    BlogPostSerializer, ServiceSerializer, TestimonialSerializer, 
    ContactSerializer, FAQSerializer, AboutUsSerializer, PortfolioSerializer
)

class BlogPostViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            password='password123'
        )
        self.blog_post = BlogPost.objects.create(
            title="Sample Blog Post",
            content="This is a sample blog post.",
            author=self.user
        )
        
    def test_list_blog_posts(self):
        url = reverse('blogpost-list')
        response = self.client.get(url)
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Extract the list of blog posts from the paginated response
        self.assertEqual(response.data['results'], serializer.data)

    def test_create_blog_post(self):
        url = reverse('blogpost-list')
        data = {
            'title': 'New Blog Post',
            'content': 'Content of the new blog post.',
            'author': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 2)
        self.assertEqual(BlogPost.objects.get(id=response.data['id']).title, 'New Blog Post')

    def test_retrieve_blog_post(self):
        url = reverse('blogpost-detail', args=[self.blog_post.id])
        response = self.client.get(url)
        serializer = BlogPostSerializer(self.blog_post)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_blog_post(self):
        url = reverse('blogpost-detail', args=[self.blog_post.id])
        data = {'title': 'Updated Blog Post', 'content': 'Updated content.'}
        response = self.client.patch(url, data, format='json')
        self.blog_post.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.blog_post.title, 'Updated Blog Post')

    def test_delete_blog_post(self):
        url = reverse('blogpost-detail', args=[self.blog_post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BlogPost.objects.count(), 0)

class PortfolioViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            password='password123'
        )
        self.portfolio = Portfolio.objects.create(
            title="Tailoring Portfolio",
            description="A showcase of our work.",
            image_url="http://example.com/image.jpg",
            created_by=self.user
        )
    
    def test_list_portfolios(self):
        url = reverse('portfolio-list')
        response = self.client.get(url)
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolios, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Extract the list of portfolios from the paginated response
        self.assertEqual(response.data['results'], serializer.data)

    def test_create_portfolio(self):
        url = reverse('portfolio-list')
        data = {
            'title': 'New Portfolio',
            'description': 'New description.',
            'image_url': 'http://example.com/new_image.jpg',
            'created_by': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Portfolio.objects.count(), 2)
        self.assertEqual(Portfolio.objects.get(id=response.data['id']).title, 'New Portfolio')

    def test_retrieve_portfolio(self):
        url = reverse('portfolio-detail', args=[self.portfolio.id])
        response = self.client.get(url)
        serializer = PortfolioSerializer(self.portfolio)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_portfolio(self):
        url = reverse('portfolio-detail', args=[self.portfolio.id])
        data = {'title': 'Updated Portfolio'}
        response = self.client.patch(url, data, format='json')
        self.portfolio.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.portfolio.title, 'Updated Portfolio')

    def test_delete_portfolio(self):
        url = reverse('portfolio-detail', args=[self.portfolio.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Portfolio.objects.count(), 0)

class CustomLoginViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            password='password123'
        )

    def test_login_success(self):
        url = reverse('custom-login')
        data = {'email': 'testuser@example.com', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_failure(self):
        url = reverse('custom-login')
        data = {'email': 'testuser@example.com', 'password': 'wrongpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Invalid credentials"})