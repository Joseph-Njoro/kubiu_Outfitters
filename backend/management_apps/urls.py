# management_apps/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BlogPostViewSet, ServiceViewSet, TestimonialViewSet, 
    ContactViewSet, FAQViewSet, AboutUsViewSet, PortfolioViewSet,
    CustomLoginView  # Import CustomLoginView
)

# Initialize the DefaultRouter and register viewsets with it
router = DefaultRouter()

# Register each ViewSet with the router, mapping them to a URL endpoint
router.register(r'blogposts', BlogPostViewSet, basename='blogposts')
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'testimonials', TestimonialViewSet, basename='testimonials')
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'faqs', FAQViewSet, basename='faqs')
router.register(r'aboutus', AboutUsViewSet, basename='aboutus')
router.register(r'portfolio', PortfolioViewSet, basename='portfolio')

# The urlpatterns list routes URLs to views provided by the router
urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs under the root path
    path('login/', CustomLoginView.as_view(), name='custom_login'),  # Correctly adds the custom login endpoint
]