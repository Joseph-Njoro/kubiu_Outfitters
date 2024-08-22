from rest_framework.test import APITestCase
from rest_framework.exceptions import ValidationError
from .models import BlogPost, Service, Testimonial, Contact, FAQ, AboutUs, Portfolio
from .serializers import (
    BlogPostSerializer, ServiceSerializer, TestimonialSerializer, 
    ContactSerializer, FAQSerializer, AboutUsSerializer, PortfolioSerializer
)

class BlogPostSerializerTest(APITestCase):
    def setUp(self):
        self.blog_post = BlogPost.objects.create(
            title='Test Blog Post',
            content='Content of the test blog post',
            author_id=1  # Ensure user ID exists or adjust as needed
        )
        self.serializer = BlogPostSerializer(instance=self.blog_post)

    def test_blog_post_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['title'], 'Test Blog Post')
        self.assertEqual(data['content'], 'Content of the test blog post')

    def test_blog_post_serializer_validation(self):
        invalid_data = {'title': '', 'content': ''}
        serializer = BlogPostSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

class ServiceSerializerTest(APITestCase):
    def setUp(self):
        self.service = Service.objects.create(
            title='Tailoring Service',
            description='Description of the tailoring service',
            price=100.00,
            created_by_id=1  # Ensure user ID exists or adjust as needed
        )
        self.serializer = ServiceSerializer(instance=self.service)

    def test_service_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['title'], 'Tailoring Service')
        self.assertEqual(data['description'], 'Description of the tailoring service')
        self.assertEqual(data['price'], '100.00')

    def test_service_serializer_validation(self):
        invalid_data = {'title': '', 'description': '', 'price': 'invalid_price'}
        serializer = ServiceSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

class TestimonialSerializerTest(APITestCase):
    def setUp(self):
        self.testimonial = Testimonial.objects.create(
            user_id=1,  # Ensure user ID exists or adjust as needed
            content='Testimonial content',
            rating=5
        )
        self.serializer = TestimonialSerializer(instance=self.testimonial)

    def test_testimonial_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['content'], 'Testimonial content')
        self.assertEqual(data['rating'], 5)

    def test_testimonial_serializer_validation(self):
        invalid_data = {'user': '', 'content': '', 'rating': 6}
        serializer = TestimonialSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

class ContactSerializerTest(APITestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            user_id=1,  # Ensure user ID exists or adjust as needed
            message='Contact message',
            email='contact@example.com'
        )
        self.serializer = ContactSerializer(instance=self.contact)

    def test_contact_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['message'], 'Contact message')
        self.assertEqual(data['email'], 'contact@example.com')

    def test_contact_serializer_validation(self):
        invalid_data = {'user': '', 'message': '', 'email': 'invalid_email'}
        serializer = ContactSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

class FAQSerializerTest(APITestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question='What is the meaning of life?',
            answer='42'
        )
        self.serializer = FAQSerializer(instance=self.faq)

    def test_faq_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['question'], 'What is the meaning of life?')
        self.assertEqual(data['answer'], '42')

    def test_faq_serializer_validation(self):
        invalid_data = {'question': '', 'answer': ''}
        serializer = FAQSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

class AboutUsSerializerTest(APITestCase):
    def setUp(self):
        self.about_us = AboutUs.objects.create(
            title='About Us',
            description='Description about us'
        )
        self.serializer = AboutUsSerializer(instance=self.about_us)

    def test_about_us_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['title'], 'About Us')
        self.assertEqual(data['description'], 'Description about us')

    def test_about_us_serializer_validation(self):
        invalid_data = {'title': '', 'description': ''}
        serializer = AboutUsSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

class PortfolioSerializerTest(APITestCase):
    def setUp(self):
        self.portfolio = Portfolio.objects.create(
            title='Portfolio Item',
            description='Description of the portfolio item',
            image_url='http://example.com/image.jpg',
            category='Category'
        )
        self.serializer = PortfolioSerializer(instance=self.portfolio)

    def test_portfolio_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['title'], 'Portfolio Item')
        self.assertEqual(data['description'], 'Description of the portfolio item')
        self.assertEqual(data['image_url'], 'http://example.com/image.jpg')
        self.assertEqual(data['category'], 'Category')

    def test_portfolio_serializer_validation(self):
        invalid_data = {'title': '', 'description': '', 'image_url': 'invalid_url', 'category': ''}
        serializer = PortfolioSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
