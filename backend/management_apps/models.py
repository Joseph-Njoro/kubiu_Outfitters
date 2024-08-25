from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator, MaxValueValidator
from .managers import CustomUserManager  # Importing the custom user manager

class CustomUser(AbstractUser):
    """
    CustomUser model that extends the default Django user model.
    Additional fields can be added as needed.
    """
    username = None # Override the default username field with a blank or null value

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Ensure email field is used for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()  # Use the custom user manager

    def __str__(self):
        return f"{self.email}"

    # Specify related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.'
    )

class Testimonial(models.Model):
    """
    Testimonial model to store user testimonials.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='testimonials')
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Testimonial by {self.user.username} (Rating: {self.rating})"

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['created_at']),
        ]

class Contact(models.Model):
    """
    Contact model to store contact messages submitted by users.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='contacts')
    message = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message from {self.email}"

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['created_at']),
        ]

class FAQ(models.Model):
    """
    FAQ model to store frequently asked questions and their answers.
    """
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]

class AboutUs(models.Model):
    """
    AboutUs model to store information about the organization.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['title']),
        ]

class BlogPost(models.Model):
    """
    BlogPost model to store blog posts written by users.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    summary = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_posts')
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['author']),
            models.Index(fields=['published_at']),
        ]

class Service(models.Model):
    """
    Service model to store the details of services offered.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['created_by']),
            models.Index(fields=['created_at']),
        ]

class Portfolio(models.Model):
    """
    Portfolio model to store portfolio items.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='portfolio')

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['created_by']),
            models.Index(fields=['created_at']),
        ]

class Booking(models.Model):
    """
    Booking model to store service bookings by users.
    """
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.title} on {self.booking_date}"

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['service']),
            models.Index(fields=['booking_date']),
        ]
