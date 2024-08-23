from decimal import Decimal
from rest_framework import serializers
from rest_framework.test import APITestCase
from management_apps.models import BlogPost,CustomUser, Service, Testimonial, Contact, FAQ, AboutUs, Portfolio
from management_apps.serializers import (
    BlogPostSerializer, ServiceSerializer, TestimonialSerializer, 
    ContactSerializer, FAQSerializer, AboutUsSerializer, PortfolioSerializer
)

class BlogPostSerializerTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')

    def test_blogpost_serialization(self):
        blogpost = BlogPost.objects.create(
            title="Test Blog",
            content="This is a test blog content",
            author=self.user
        )
        serializer = BlogPostSerializer(blogpost)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'content', 'summary', 'author', 'published_at', 'created_at', 'updated_at']))
        self.assertEqual(data['title'], blogpost.title)
        self.assertEqual(data['content'], blogpost.content)
        self.assertEqual(data['author'], self.user.id)

    def test_blogpost_deserialization(self):
        data = {
            "title": "Test Blog",
            "content": "This is a test blog content",
            "author": self.user.id
        }
        serializer = BlogPostSerializer(data=data)
        if not serializer.is_valid():
            print(serializer.errors)  # Print errors for debugging
        self.assertTrue(serializer.is_valid())
        blogpost = serializer.save()
        self.assertEqual(blogpost.title, data['title'])
        self.assertEqual(blogpost.content, data['content'])
        self.assertEqual(blogpost.author, self.user)

class ServiceSerializerTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')

    def test_service_serialization(self):
        service = Service.objects.create(
            title="Test Service",
            description="This is a test service",
            price=Decimal('19.99'),
            created_by=self.user
        )
        serializer = ServiceSerializer(service)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'description', 'price', 'created_at', 'updated_at', 'created_by']))
        self.assertEqual(data['title'], service.title)
        self.assertEqual(data['description'], service.description)
        self.assertEqual(data['price'], str(service.price))  # Decimal values are serialized as strings
        self.assertEqual(data['created_by'], self.user.id)

    def test_service_deserialization(self):
        data = {
            "title": "Test Service",
            "description": "This is a test service",
            "price": "19.99",
            "created_by": self.user.id
        }
        serializer = ServiceSerializer(data=data)
        is_valid = serializer.is_valid()  # Validate the serializer data
        print(serializer.errors)  # Print errors if any after validation
        self.assertTrue(is_valid)  # Check if the serializer is valid
        service = serializer.save()
        self.assertEqual(service.title, data['title'])
        self.assertEqual(service.description, data['description'])
        self.assertEqual(service.price, Decimal(data['price']))
        self.assertEqual(service.created_by.id, self.user.id)

class TestimonialSerializerTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')

    def test_testimonial_serialization(self):
        testimonial = Testimonial.objects.create(
            user=self.user,
            content="This is a test testimonial",
            rating=5
        )
        serializer = TestimonialSerializer(testimonial)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'user', 'content', 'rating', 'created_at', 'updated_at']))
        self.assertEqual(data['user'], self.user.id)
        self.assertEqual(data['content'], testimonial.content)
        self.assertEqual(data['rating'], testimonial.rating)

    def test_testimonial_deserialization(self):
        data = {
            "user": self.user.id,
            "content": "This is a test testimonial",
            "rating": 5
        }
        serializer = TestimonialSerializer(data=data)
        if not serializer.is_valid():
            print(serializer.errors)  # Print errors for debugging
        self.assertTrue(serializer.is_valid())
        testimonial = serializer.save()
        self.assertEqual(testimonial.user, self.user)
        self.assertEqual(testimonial.content, data['content'])
        self.assertEqual(testimonial.rating, data['rating'])

class ContactSerializerTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')

    def test_contact_serialization(self):
        contact = Contact.objects.create(user=self.user, email="johndoe@example.com", message="This is a test contact")
        serializer = ContactSerializer(contact)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'user', 'email', 'message', 'created_at', 'updated_at']))
        self.assertEqual(data['user'], self.user.id)
        self.assertEqual(data['email'], contact.email)
        self.assertEqual(data['message'], contact.message)

    def test_contact_deserialization(self):
        data = {
            "user": self.user.id,
            "email": "johndoe@example.com",
            "message": "This is a test contact"
        }
        serializer = ContactSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        contact = serializer.save()
        self.assertEqual(contact.user, self.user)
        self.assertEqual(contact.email, data['email'])
        self.assertEqual(contact.message, data['message'])

    # Example for Service Model Test
    def test_service_deserialization(self):
        data = {"name": "Test Service", "description": "This is a test service"}
        serializer = ServiceSerializer(data=data)
        print(serializer.errors)  # Print errors if any
        self.assertTrue(serializer.is_valid()) # Check if the serializer is valid
        service = serializer.save()
        self.assertEqual(service.name, data['name'])
        self.assertEqual(service.description, data['description'])

class FAQSerializerTest(APITestCase):
    def test_faq_serialization(self):
        faq = FAQ.objects.create(question="What is this?", answer="This is a test FAQ")
        serializer = FAQSerializer(faq)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'question', 'answer', 'created_at', 'updated_at']))
        self.assertEqual(data['question'], faq.question)
        self.assertEqual(data['answer'], faq.answer)

    def test_faq_deserialization(self):
        data = {"question": "What is this?", "answer": "This is a test FAQ"}
        serializer = FAQSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        faq = serializer.save()
        self.assertEqual(faq.question, data['question'])
        self.assertEqual(faq.answer, data['answer'])

class AboutUsSerializerTest(APITestCase):
    def test_aboutus_serialization(self):
        about_us = AboutUs.objects.create(
            title="About Us Title",
            description="Description of About Us"
        )
        serializer = AboutUsSerializer(about_us)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'description', 'created_at', 'updated_at']))
        self.assertEqual(data['title'], about_us.title)
        self.assertEqual(data['description'], about_us.description)

    def test_aboutus_deserialization(self):
        data = {
            "title": "About Us Title",
            "description": "Description of About Us"
        }
        serializer = AboutUsSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        about_us = serializer.save()
        self.assertEqual(about_us.title, data['title'])
        self.assertEqual(about_us.description, data['description'])

class PortfolioSerializerTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')

    def test_portfolio_serialization(self):
        portfolio = Portfolio.objects.create(
            title="Test Portfolio",
            description="This is a test portfolio",
            created_by=self.user,
            image_url="http://example.com/image.jpg",
            category="Category A"
        )
        serializer = PortfolioSerializer(portfolio)
        print(serializer.errors)  # Print errors if any
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'description', 'image_url', 'category', 'created_at', 'updated_at', 'created_by']))
        self.assertEqual(data['title'], portfolio.title)
        self.assertEqual(data['description'], portfolio.description)
        self.assertEqual(data['image_url'], portfolio.image_url)
        self.assertEqual(data['category'], portfolio.category)
        self.assertEqual(data['created_by'], self.user.id)

    def test_portfolio_deserialization(self):
        data = {
            "title": "Test Portfolio",
            "description": "This is a test portfolio",
            "image_url": "http://example.com/image.jpg",
            "category": "Category A",
            "created_by": self.user.id
        }
        serializer = PortfolioSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        portfolio = serializer.save()
        self.assertEqual(portfolio.title, data['title'])
        self.assertEqual(portfolio.description, data['description'])
        self.assertEqual(portfolio.image_url, data['image_url'])
        self.assertEqual(portfolio.category, data['category'])
        self.assertEqual(portfolio.created_by.id, self.user.id)