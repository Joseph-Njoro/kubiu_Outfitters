from django.test import TestCase
from django.contrib import admin
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.html import escape
from management_apps.models import CustomUser, Testimonial, Contact, FAQ, AboutUs, BlogPost, Service, Portfolio
from management_apps.admin import CustomUserAdmin, TestimonialAdmin, ContactAdmin, FAQAdmin, AboutUsAdmin, BlogPostAdmin, ServiceAdmin, PortfolioAdmin

class AdminSiteTests(TestCase):

    def setUp(self):
        # Create a superuser to access the admin site
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='testpass123'
        )
        self.client.force_login(self.admin_user)

        # Create a regular user
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@example.com',
            password='testpass123',
            first_name='John',
            last_name='Doe'
        )

        # Create sample instances of each model
        self.testimonial = Testimonial.objects.create(
            user=self.user,
            content='Great service!',
            rating=5
        )
        self.contact = Contact.objects.create(
            user=self.user,
            message='Hello!',
            email='jane@example.com'
        )
        self.faq = FAQ.objects.create(
            question='What is this?',
            answer='This is a FAQ.'
        )
        self.about_us = AboutUs.objects.create(
            title='About Us',
            description='We are awesome.'
        )
        self.blog_post = BlogPost.objects.create(
            title='Blog Post',
            content='This is a blog post.',
            author=self.user
        )
        self.service = Service.objects.create(
            title='Consulting',
            description='We provide consulting services.',
            price=100.00,
            created_by=self.user
        )
        self.portfolio = Portfolio.objects.create(
            title='Project 1',
            description='Description of Project 1.',
            image_url='http://example.com/image.jpg',
            created_by=self.user
        )

    def test_custom_user_admin_list_display(self):
        """Test CustomUserAdmin list display fields"""
        url = reverse('admin:management_apps_customuser_changelist')
        response = self.client.get(url)
        self.assertContains(response, escape(self.user.email))
        self.assertContains(response, escape(self.user.first_name))
        self.assertContains(response, escape(self.user.last_name))

    def test_custom_user_admin_change_form(self):
        """Test the custom user admin change form"""
        url = reverse('admin:management_apps_customuser_change', args=[self.user.id])
        response = self.client.get(url)
        self.assertContains(response, escape(self.user.email))
        self.assertContains(response, escape(self.user.first_name))
        self.assertContains(response, escape(self.user.last_name))

    def test_testimonial_admin(self):
        """Test TestimonialAdmin registration and list display"""
        url = reverse('admin:management_apps_testimonial_changelist')
        self.assertTrue(isinstance(admin.site._registry[Testimonial], TestimonialAdmin))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, escape(self.testimonial.content))

    def test_contact_admin(self):
        """Test ContactAdmin registration and list display"""
        url = reverse('admin:management_apps_contact_changelist')
        self.assertTrue(isinstance(admin.site._registry[Contact], ContactAdmin))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, escape(self.contact.message))

    def test_faq_admin(self):
        """Test FAQAdmin registration and list display"""
        url = reverse('admin:management_apps_faq_changelist')
        self.assertTrue(isinstance(admin.site._registry[FAQ], FAQAdmin))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, escape(self.faq.question))

    def test_aboutus_admin(self):
        """Test AboutUsAdmin registration and list display"""
        url = reverse('admin:management_apps_aboutus_changelist')
        self.assertTrue(isinstance(admin.site._registry[AboutUs], AboutUsAdmin))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, escape(self.about_us.description))

    def test_blogpost_admin(self):
        """Test BlogPostAdmin registration and list display"""
        url = reverse('admin:management_apps_blogpost_changelist')
        self.assertTrue(isinstance(admin.site._registry[BlogPost], BlogPostAdmin))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, escape(self.blog_post.title))

    def test_service_admin(self):
        """Test ServiceAdmin registration and list display"""
        url = reverse('admin:management_apps_service_changelist')
        self.assertTrue(isinstance(admin.site._registry[Service], ServiceAdmin))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, escape(self.service.title))

    def test_portfolio_admin(self):
        """Test PortfolioAdmin registration and list display"""
        url = reverse('admin:management_apps_portfolio_changelist')
        self.assertTrue(isinstance(admin.site._registry[Portfolio], PortfolioAdmin))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, escape(self.portfolio.title))
