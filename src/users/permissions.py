"""
Users permissions rules
"""
from rest_framework import permissions


class IsAccountAdminOrReadOnly(permissions.BasePermission):
    """
    Read only access if not admin.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise user must be admin.
        return request.user.is_staff


class IsSelfOrReadOnly(permissions.BasePermission):
    """
    User object-level permissions.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise user must be same user or admin.
        return request.user.is_staff or request.user.id == obj.id
