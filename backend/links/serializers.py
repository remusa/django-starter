from django.contrib.auth import get_user_model

from rest_framework import request, serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Link

CustomUser = get_user_model()


class LinkSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="link-detail")
    current_user = serializers.CurrentUserDefault()
    owner = serializers.HiddenField(default=current_user)
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True, default=current_user)
    # owner_url = serializers.HyperlinkedRelatedField(view_name="customuser-detail", read_only=True)

    class Meta:
        model = Link
        fields = "__all__"
        # fields = [
        #     "id",
        #     "title",
        #     "description",
        #     "favorited",
        #     "article_url",
        #     "updated_at",
        #     "created_at",
        #     "owner",
        #     "owner_id",
        #     # "owner_url",
        #     "url",
        # ]
        # read_only_fields = [
        #     "id",
        #     "updated_at",
        #     "created_at",
        #     "owner_id",
        #     "url",
        # ]

    def get_serializer_class(self):
        if serializers.action == "retrieve":
            return serializers.LinkSerializer

        return self.serializer_class
