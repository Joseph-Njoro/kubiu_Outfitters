from django.test import SimpleTestCase
from django.urls import reverse, resolve
from management_apps import views

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home_view)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, views.about_view)

    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, views.contact_view)

    def test_services_url_resolves(self):
        url = reverse('services')
        self.assertEqual(resolve(url).func, views.services_view)

    def test_portfolio_url_resolves(self):
        url = reverse('portfolio')
        self.assertEqual(resolve(url).func, views.portfolio_view)

    def test_testimonials_url_resolves(self):
        url = reverse('testimonials')
        self.assertEqual(resolve(url).func, views.testimonials_view)

    def test_faq_url_resolves(self):
        url = reverse('faq')
        self.assertEqual(resolve(url).func, views.faq_view)

    def test_blog_url_resolves(self):
        url = reverse('blog')
        self.assertEqual(resolve(url).func, views.blog_view)

    # Add more tests as needed for other URLs in your project
