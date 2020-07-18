from django.conf.urls import url
from django.urls import include, path

from allauth.account.views import confirm_email

from . import views

app_name = "users"

urlpatterns = [
    url(
        r"^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$",
        confirm_email,
        name="account_confirm_email",
    ),
    # path("", include("allauth.urls")),
]
