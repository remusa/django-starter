from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from links.models import Link

from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()


class LinksInline(admin.TabularInline):
    model = Link
    extra = 0
    max_num = 2
    prepopulated_fields = {"title": ("description",)}
    fieldsets = (
        ("Basic info", {"classes": ("collapse",), "fields": ("title", "description")}),
        ("Some other fields", {"classes": ("collapse",), "fields": ("article_url",)},),
    )
    classes = ("collapse",)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser

    ordering = ["-is_staff"]
    list_display = [
        "email",
        "username",
        "is_staff",
    ]

    fieldsets = (
        (None, {"fields": ("email", "password",)}),
        ("Personal info", {"fields": ("username", "first_name", "last_name",)},),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",),},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined",)}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2",),},),
    )

    inlines = [LinksInline]
