from django.test import SimpleTestCase
from django.urls import reverse, resolve
from management_apps.views import (
    BlogPostViewSet, ServiceViewSet, TestimonialViewSet, 
    ContactViewSet, FAQViewSet, AboutUsViewSet, PortfolioViewSet
)

class TestUrls(SimpleTestCase):
    def test_blog_url_resolves(self):
        url = reverse('blogpost-list')  # Updated basename to match 'blogpost'
        self.assertEqual(resolve(url).view_name, 'blogpost-list')

    def test_services_url_resolves(self):
        url = reverse('service-list')  # Updated basename to match 'service'
        self.assertEqual(resolve(url).view_name, 'service-list')

    def test_testimonials_url_resolves(self):
        url = reverse('testimonial-list')  # Updated basename to match 'testimonial'
        self.assertEqual(resolve(url).view_name, 'testimonial-list')

    def test_contact_url_resolves(self):
        url = reverse('contact-list')  # Updated basename to match 'contact'
        self.assertEqual(resolve(url).view_name, 'contact-list')

    def test_faq_url_resolves(self):
        url = reverse('faq-list')  # Updated basename to match 'faq'
        self.assertEqual(resolve(url).view_name, 'faq-list')

    def test_about_url_resolves(self):
        url = reverse('aboutus-list')  # Updated basename to match 'aboutus'
        self.assertEqual(resolve(url).view_name, 'aboutus-list')

    def test_portfolio_url_resolves(self):
        url = reverse('portfolio-list')  # Updated basename to match 'portfolio'
        self.assertEqual(resolve(url).view_name, 'portfolio-list')