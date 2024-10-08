from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    BlogPostViewSet, ServiceViewSet, TestimonialViewSet, ContactViewSet, FAQViewSet,
    AboutUsViewSet, PortfolioViewSet, CustomLoginView, ProtectedView
)

# Initialize the router for automatically generating URLs
router = DefaultRouter()

# Register viewsets with the router
router.register(r'blogposts', BlogPostViewSet, basename='blogpost')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'faqs', FAQViewSet, basename='faq')
router.register(r'aboutus', AboutUsViewSet, basename='aboutus')
router.register(r'portfolios', PortfolioViewSet, basename='portfolio')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    
    # Include router-generated URLs under 'api/'
    path('api/', include(router.urls)),

    # Custom login endpoint
    path('api/login/', CustomLoginView.as_view(), name='custom-login'),

    # Protected endpoint
    path('api/protected/', ProtectedView.as_view(), name='protected-endpoint'),
]