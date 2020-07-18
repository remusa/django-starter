import datetime
import uuid
from datetime import date

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        verbose_name="username", max_length=150, unique=True, null=True, blank=True,
    )
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True, null=False, blank=False,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_id(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("user-detail", args=[str(self.id)])
