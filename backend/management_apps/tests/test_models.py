from django.test import TestCase
from django.utils import timezone
from management_apps.models import CustomUser, BlogPost, Service, Testimonial, Contact, FAQ, AboutUs, Portfolio, Booking

class CustomUserModelTest(TestCase):
    def setUp(self):
        # Updated to exclude username and use only email and other required fields
        self.user = CustomUser.objects.create_user(
            email='johndoe@example.com',
            first_name='John',
            last_name='Doe',
            password='testpassword123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'johndoe@example.com')
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')
        self.assertTrue(self.user.check_password('testpassword123'))

class TestimonialModelTest(TestCase):
    def setUp(self):
        # Updated to exclude username and use only email and other required fields
        self.user = CustomUser.objects.create_user(
            email='janedoe@example.com',
            first_name='Jane',
            last_name='Doe',
            password='testpassword123'
        )
        self.testimonial = Testimonial.objects.create(
            user=self.user,
            content='Great service!',
            rating=5
        )

    def test_testimonial_creation(self):
        self.assertEqual(self.testimonial.user.email, 'janedoe@example.com')
        self.assertEqual(self.testimonial.content, 'Great service!')
        self.assertEqual(self.testimonial.rating, 5)

class ContactModelTest(TestCase):
    def setUp(self):
        # Updated to exclude username and use only email and other required fields
        self.user = CustomUser.objects.create_user(
            email='alice@example.com',
            first_name='Alice',
            last_name='Smith',
            password='testpassword123'
        )
        self.contact = Contact.objects.create(
            user=self.user,
            message='I need more information about your services.',
            email='alice@example.com'
        )

    def test_contact_creation(self):
        self.assertEqual(self.contact.user.email, 'alice@example.com')
        self.assertEqual(self.contact.message, 'I need more information about your services.')
        self.assertEqual(self.contact.email, 'alice@example.com')

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question='What are your working hours?',
            answer='We are open from 9 AM to 5 PM.'
        )

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, 'What are your working hours?')
        self.assertEqual(self.faq.answer, 'We are open from 9 AM to 5 PM.')

class AboutUsModelTest(TestCase):
    def setUp(self):
        self.about_us = AboutUs.objects.create(
            title='About Kubiu Outfitters',
            description='We provide custom tailoring services for all occasions.'
        )

    def test_about_us_creation(self):
        self.assertEqual(self.about_us.title, 'About Kubiu Outfitters')
        self.assertEqual(self.about_us.description, 'We provide custom tailoring services for all occasions.')

class BlogPostModelTest(TestCase):
    def setUp(self):
        # Updated to exclude username and use only email and other required fields
        self.user = CustomUser.objects.create_user(
            email='bob@example.com',
            first_name='Bob',
            last_name='Jones',
            password='testpassword123'
        )
        self.blog_post = BlogPost.objects.create(
            title='Tailoring Tips',
            content='Here are some useful tips for custom tailoring.',
            author=self.user
        )

    def test_blog_post_creation(self):
        self.assertEqual(self.blog_post.title, 'Tailoring Tips')
        self.assertEqual(self.blog_post.content, 'Here are some useful tips for custom tailoring.')
        self.assertEqual(self.blog_post.author.email, 'bob@example.com')

class ServiceModelTest(TestCase):
    def setUp(self):
        # Updated to exclude username and use only email and other required fields
        self.user = CustomUser.objects.create_user(
            email='charlie@example.com',
            first_name='Charlie',
            last_name='Brown',
            password='testpassword123'
        )
        self.service = Service.objects.create(
            title='Tailoring',
            description='Custom tailoring services',
            price=100.00,
            created_by=self.user
        )

    def test_service_creation(self):
        self.assertEqual(self.service.title, 'Tailoring')
        self.assertEqual(self.service.description, 'Custom tailoring services')
        self.assertEqual(self.service.price, 100.00)
        self.assertEqual(self.service.created_by.email, 'charlie@example.com')

class PortfolioModelTest(TestCase):
    def setUp(self):
        # Updated to exclude username and use only email and other required fields
        self.user = CustomUser.objects.create_user(
            email='david@example.com',
            first_name='David',
            last_name='Goliath',
            password='testpassword123'
        )
        self.portfolio = Portfolio.objects.create(
            title='Wedding Suit',
            description='A custom-tailored wedding suit.',
            image_url='http://example.com/image.jpg',
            created_by=self.user
        )

    def test_portfolio_creation(self):
        self.assertEqual(self.portfolio.title, 'Wedding Suit')
        self.assertEqual(self.portfolio.description, 'A custom-tailored wedding suit.')
        self.assertEqual(self.portfolio.image_url, 'http://example.com/image.jpg')
        self.assertEqual(self.portfolio.created_by.email, 'david@example.com')

class BookingModelTest(TestCase):
    def setUp(self):
        # Updated to exclude username and use only email and other required fields
        self.user = CustomUser.objects.create_user(
            email='eve@example.com',
            first_name='Eve',
            last_name='Doe',
            password='testpassword123'
        )
        self.service = Service.objects.create(
            title='Suit Fitting',
            description='Tailoring and fitting of custom suits',
            price=200.00,
            created_by=self.user
        )
        self.booking = Booking.objects.create(
            user=self.user,
            service=self.service,
            booking_date=timezone.now()
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.user.email, 'eve@example.com')
        self.assertEqual(self.booking.service.title, 'Suit Fitting')
        self.assertEqual(self.booking.status, Booking.PENDING)