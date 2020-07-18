from django.urls import include, path

from links.views import LinkFavoriteAPIView, LinkViewSet
from rest_framework import routers
from users.views import ManageUserView, UserViewSet

router = routers.DefaultRouter()

router.register(r"users", viewset=UserViewSet, basename="user")
router.register(r"links", viewset=LinkViewSet, basename="link")

urlpatterns = [
    path("", include(router.urls)),
    path("users/me/", ManageUserView.as_view(), name="me"),
    path("links/<uuid:id>/favorite", LinkFavoriteAPIView.as_view(), name="favorite",),
]
