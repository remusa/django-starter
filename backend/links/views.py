from django.core.serializers import get_serializer
from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Link
from .permissions import IsOwnerOrReadOnly
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [
        IsOwnerOrReadOnly,
        IsAuthenticated,
    ]
    pagination_classes = [PageNumberPagination]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "description", "favorite", "article_url"]
    ordering_fields = [
        "title",
        "description",
        "article_url",
        "processed",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]

    def get_queryset(self):
        user = self.request.user

        # if user.has_perm("IsAdmin"):
        #     return Link.objects.all()

        return Link.objects.filter(owner=user)


class LinkFavoriteAPIView(APIView):
    serializer_class = LinkSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [
        IsOwnerOrReadOnly,
    ]

    def get_object(self, id):
        return Link.objects.get(id=id)

    def patch(self, request, id):
        link = self.get_object(id=id)

        if request.method == "POST":
            favorited = True
        elif request.method == "DELETE":
            favorited = False
        else:
            return Response(
                "Only POST and DELETE requests accepted", status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(
            link, data={"favorited": favorited}, partial=True, context={"request": request},
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id=None):
        try:
            link = self.get_object(id=id)
        except Link.DoesNotExist:
            raise NotFound(
                "A link with this id was not found.", status=status.HTTP_404_NOT_FOUND,
            )

        return self.patch(request, id)

    def delete(self, request, id=None):
        try:
            link = self.get_object(id=id)
        except Link.DoesNotExist:
            raise NotFound(
                "A link with this id was not found.", status=status.HTTP_404_NOT_FOUND,
            )

        return self.patch(request, id)
