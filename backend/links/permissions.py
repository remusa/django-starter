from django.contrib.auth import get_user_model

from rest_framework import permissions

CustomUser = get_user_model()


class IsOwnerOrReadOnly(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     owner = pk = view.kwargs["owner"]
    #     user = CustomUser.objects.get(owner)

    #     if request.user != user:
    #         return False

    #     return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner
        return obj.owner.id == request.user.id
