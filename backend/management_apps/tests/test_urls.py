from django.test import SimpleTestCase
from django.urls import reverse, resolve
from management_apps.views import (
    BlogPostViewSet, ServiceViewSet, TestimonialViewSet, 
    ContactViewSet, FAQViewSet, AboutUsViewSet, PortfolioViewSet
)

class TestUrls(SimpleTestCase):
    def test_blog_url_resolves(self):
        url = reverse('blogposts-list')  # Viewset URL pattern
        self.assertEqual(resolve(url).view_name, 'blogposts-list')

    def test_services_url_resolves(self):
        url = reverse('services-list')
        self.assertEqual(resolve(url).view_name, 'services-list')

    def test_testimonials_url_resolves(self):
        url = reverse('testimonials-list')
        self.assertEqual(resolve(url).view_name, 'testimonials-list')

    def test_contact_url_resolves(self):
        url = reverse('contacts-list')
        self.assertEqual(resolve(url).view_name, 'contacts-list')

    def test_faq_url_resolves(self):
        url = reverse('faqs-list')
        self.assertEqual(resolve(url).view_name, 'faqs-list')

    def test_about_url_resolves(self):
        url = reverse('aboutus-list')
        self.assertEqual(resolve(url).view_name, 'aboutus-list')

    def test_portfolio_url_resolves(self):
        url = reverse('portfolio-list')
        self.assertEqual(resolve(url).view_name, 'portfolio-list')
