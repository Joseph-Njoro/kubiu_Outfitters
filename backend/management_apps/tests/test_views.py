from django.test import TestCase, Client
from django.urls import reverse
from management_apps.models import CustomUser, Testimonial, Contact, BlogPost, Service

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.testimonial = Testimonial.objects.create(author=self.user, content="Great service!")
        self.contact = Contact.objects.create(name="John Doe", email="john@example.com", message="Hello!")
        self.blog_post = BlogPost.objects.create(title="New Post", content="This is a new blog post.")
        self.service = Service.objects.create(name="Tailoring", description="Custom tailoring service")

    def test_home_view_get(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_view_get(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contact_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_view_post(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'message': 'Hi there!'
        })
        self.assertEqual(response.status_code, 302)  # Assuming you redirect after POST

    def test_services_view_get(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services.html')

    def test_portfolio_view_get(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio.html')

    def test_testimonials_view_get(self):
        response = self.client.get(reverse('testimonials'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testimonials.html')

    def test_faq_view_get(self):
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq.html')

    def test_blog_view_get(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')

    def test_blog_post_view(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog_post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_detail.html')
        self.assertContains(response, self.blog_post.title)

    # Add more tests as needed for other views in your project
