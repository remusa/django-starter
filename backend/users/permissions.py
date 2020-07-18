from rest_framework import permissions


class IsUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.has_perm("IsAdmin"):
            return True

        # Write permissions are only allowed to the owner
        return obj.id == request.user.id
