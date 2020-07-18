from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_normalize_email(self):
        email = "testuser@test.com"
        password = "testuser123"

        User = get_user_model()
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email.lower())

    def test_create_user(self):
        email = "testuser@test.com"
        password = "testuser123"

        User = get_user_model()
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        email = "admin@admin.com"
        password = "admin123456"

        User = get_user_model()
        user = User.objects.create_superuser(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
