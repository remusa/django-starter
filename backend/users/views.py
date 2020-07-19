import json

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils import translation
from django.utils.html import escape
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.views import generic

from links.models import Link
from rest_framework import generics, status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .permissions import IsUserOrAdmin
from .serializers import UserSerializer

CustomUser = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["id", "email", "username"]

    def get_queryset(self):
        user = self.request.user

        if user.has_perm("IsAdmin"):
            return self.queryset

        return self.queryset.filter(id=user.id)

    def get(self, request, pk=None, format=None):
        user = self.request.user
        serializer_context = {
            "request": request,
        }
        serializer = UserSerializer(user, context=serializer_context)
        return Response(serializer.data)


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self):
        return self.request.user
