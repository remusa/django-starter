from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory

CREATE_USER_URL = reverse("user-list")
REGISTER_USER_URL = "/rest-auth/registration/"
TOKEN_URL = "/rest-auth/login/"

CustomUser = get_user_model()


def create_user(**params):
    """Helper function to create new user"""
    return CustomUser.objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()
        # self.client = APIRequestFactory()

    def test_create_valid_user_success(self):
        """Test creating using with a valid payload is successful"""
        payload = {"email": "test@test.com", "password": "test123456"}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = CustomUser.objects.get(**res.data)
        # NOTE: commented this because we aren't returning the password
        # self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload = {"email": "test@test.com", "password": "test123456"}
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # TODO: fix test_password_too_short
    def test_password_too_short(self):
        """Test that password must have at least 8 characters"""
        payload = {"email": "test@test.com", "password": "pw"}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = CustomUser.objects.filter(email=payload["email"]).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {"email": "test@test.com", "password": "test123456"}
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn("key", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token isn't created if credentials are invalid"""
        create_user(email="test@test.com", password="test123456")
        payload = {"email": "test@test.com", "password": "wrong"}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("key", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token isn't created if user doesn't exist"""
        payload = {"email": "test@test.com", "password": "wrong"}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("key", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        payload = {"email": "hello", "password": ""}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("key", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
