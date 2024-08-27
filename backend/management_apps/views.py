import logging

from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import BlogPost, Service, Testimonial, Contact, FAQ, AboutUs, Portfolio
from .serializers import (
    BlogPostSerializer, ServiceSerializer, TestimonialSerializer, 
    ContactSerializer, FAQSerializer, AboutUsSerializer, PortfolioSerializer
)

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]  # Allow unrestricted access

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [AllowAny]

class CustomLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Log the login attempt
        logger.info(f"Attempting login with email: {email}")

        # Check if both email and password are provided
        if not email:
            return Response({"email": "This field is required."}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({"password": "This field is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            logger.info(f"User authenticated successfully: {email}")

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            logger.warning(f"Invalid credentials for email: {email}")
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


# The missing 'protected_view' to handle protected routes
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logger.info(f"Protected view accessed by user: {request.user.email}")
        return Response({"message": "You have access to this protected view!"}, status=status.HTTP_200_OK)