from django.contrib import admin

from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        # "description",
        "article_url",
        "favorited",
        "created_at",
        "updated_at",
        "owner",
    ]
