from allauth.socialaccount.forms import SignupForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
        )


class CustomGitHubSignupForm(SignupForm):
    def save(self):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomGitHubSignupForm, self).save()

        # Add your own processing here.

        # You must return the original result.
        return user
