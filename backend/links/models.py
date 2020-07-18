import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

CustomUser = get_user_model()


class Link(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        # db_index=False,
        editable=False,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True)
    article_url = models.CharField(max_length=255, null=False, blank=False)
    favorited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pages:dashboard-detail", kwargs={"pk": str(self.id)})

    class Meta:
        permissions = [
            ("special_status", "Can view all links"),
        ]
        indexes = [
            # models.Index(fields=["id"], name="id_index"),
        ]
