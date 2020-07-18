from django.contrib.auth import get_user_model

from links.models import Link
from rest_framework import serializers

CustomUser = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "last_login",
            "date_joined",
            "url",
        ]
        read_only_fields = ["id", "last_login", "date_joined", "url"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8, "style": {"input_type": "password"},},
        }

    def create(self, validated_data):
        """Create and return a new user"""
        return CustomUser.objects.create_user(**validated_data)
