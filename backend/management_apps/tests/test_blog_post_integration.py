import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from management_apps.models import BlogPost

@pytest.mark.django_db
def test_blog_post_crud_operations():
    # Create a user for the blog post
    User = get_user_model()
    user = User.objects.create_user(
        email='testuser@example.com',
        first_name='Test',
        last_name='User',
        password='testpass'
    )

    client = APIClient()
    client.login(email='testuser@example.com', password='testpass')  # Log in the user

    blog_post_data = {
        "title": "Test Blog Post",
        "content": "This is a test blog post content.",
        "author": user.id  # Assign the created user as the author
    }
    
    # Create a blog post
    response = client.post(reverse('blogpost-list'), blog_post_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert BlogPost.objects.count() == 1
    assert BlogPost.objects.get().title == "Test Blog Post"

    # Retrieve the blog post
    response = client.get(reverse('blogpost-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == "Test Blog Post"

    # Update the blog post
    updated_data = {
        "title": "Updated Blog Post",
        "content": "This is an updated blog post content.",
        "author": user.id  # Ensure the author field is included in the update
    }
    response = client.put(reverse('blogpost-detail', kwargs={'pk': 1}), updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert BlogPost.objects.get().title == "Updated Blog Post"

    # Delete the blog post
    response = client.delete(reverse('blogpost-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert BlogPost.objects.count() == 0