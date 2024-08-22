from rest_framework import serializers
from rest_framework.test import APITestCase
from .models import BlogPost, Service, Testimonial, Contact, FAQ, AboutUs, Portfolio
from .serializers import (
    BlogPostSerializer, ServiceSerializer, TestimonialSerializer, 
    ContactSerializer, FAQSerializer, AboutUsSerializer, PortfolioSerializer
)

class BlogPostSerializerTest(APITestCase):
    def test_blogpost_serialization(self):
        blogpost = BlogPost.objects.create(title="Test Blog", content="This is a test blog content")
        serializer = BlogPostSerializer(blogpost)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'content', 'created_at', 'updated_at']))
        self.assertEqual(data['title'], blogpost.title)
        self.assertEqual(data['content'], blogpost.content)

    def test_blogpost_deserialization(self):
        data = {"title": "Test Blog", "content": "This is a test blog content"}
        serializer = BlogPostSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        blogpost = serializer.save()
        self.assertEqual(blogpost.title, data['title'])
        self.assertEqual(blogpost.content, data['content'])

class ServiceSerializerTest(APITestCase):
    def test_service_serialization(self):
        service = Service.objects.create(name="Test Service", description="This is a test service")
        serializer = ServiceSerializer(service)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'description', 'created_at', 'updated_at']))
        self.assertEqual(data['name'], service.name)
        self.assertEqual(data['description'], service.description)

    def test_service_deserialization(self):
        data = {"name": "Test Service", "description": "This is a test service"}
        serializer = ServiceSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        service = serializer.save()
        self.assertEqual(service.name, data['name'])
        self.assertEqual(service.description, data['description'])

class TestimonialSerializerTest(APITestCase):
    def test_testimonial_serialization(self):
        testimonial = Testimonial.objects.create(author="John Doe", content="This is a test testimonial")
        serializer = TestimonialSerializer(testimonial)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'author', 'content', 'created_at', 'updated_at']))
        self.assertEqual(data['author'], testimonial.author)
        self.assertEqual(data['content'], testimonial.content)

    def test_testimonial_deserialization(self):
        data = {"author": "John Doe", "content": "This is a test testimonial"}
        serializer = TestimonialSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        testimonial = serializer.save()
        self.assertEqual(testimonial.author, data['author'])
        self.assertEqual(testimonial.content, data['content'])

class ContactSerializerTest(APITestCase):
    def test_contact_serialization(self):
        contact = Contact.objects.create(name="John Doe", email="johndoe@example.com", message="This is a test contact")
        serializer = ContactSerializer(contact)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'email', 'message', 'created_at']))
        self.assertEqual(data['name'], contact.name)
        self.assertEqual(data['email'], contact.email)
        self.assertEqual(data['message'], contact.message)

    def test_contact_deserialization(self):
        data = {"name": "John Doe", "email": "johndoe@example.com", "message": "This is a test contact"}
        serializer = ContactSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        contact = serializer.save()
        self.assertEqual(contact.name, data['name'])
        self.assertEqual(contact.email, data['email'])
        self.assertEqual(contact.message, data['message'])

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
        aboutus = AboutUs.objects.create(description="This is about us")
        serializer = AboutUsSerializer(aboutus)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'description', 'created_at', 'updated_at']))
        self.assertEqual(data['description'], aboutus.description)

    def test_aboutus_deserialization(self):
        data = {"description": "This is about us"}
        serializer = AboutUsSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        aboutus = serializer.save()
        self.assertEqual(aboutus.description, data['description'])

class PortfolioSerializerTest(APITestCase):
    def test_portfolio_serialization(self):
        portfolio = Portfolio.objects.create(title="Test Portfolio", description="This is a test portfolio")
        serializer = PortfolioSerializer(portfolio)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'description', 'created_at', 'updated_at']))
        self.assertEqual(data['title'], portfolio.title)
        self.assertEqual(data['description'], portfolio.description)

    def test_portfolio_deserialization(self):
        data = {"title": "Test Portfolio", "description": "This is a test portfolio"}
        serializer = PortfolioSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        portfolio = serializer.save()
        self.assertEqual(portfolio.title, data['title'])
        self.assertEqual(portfolio.description, data['description'])
