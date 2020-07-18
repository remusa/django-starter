from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

ME_URL = reverse("me")
# ME_URL = "/rest-auth/user/"

CustomUser = get_user_model()


def create_user(**params):
    """Helper function to create new user"""
    return CustomUser.objects.create_user(**params)


class PrivateUserApiTests(TestCase):
    """Test the users API (private)"""

    def setUp(self):
        self.user = create_user(email="test@test.com", password="test123456",)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_user_unauthorized(self):
        """Test that authentication required for users"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in user"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn({"email": self.user.email,}, res.data)

    def test_post_me_not_allowed(self):
        """Test that POST is not allowed on the me URL"""
        res = self.client.post(ME_URL, {})

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """Test updating the user profile for authenticated user"""
        payload = {"username": "new name", "password": "newpassword123"}

        res = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, payload["username"])
        self.assertTrue(self.user.check_password(payload["password"]))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
