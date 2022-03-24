from rest_framework import permissions


class IsSupportOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            return bool(request.user and request.user.is_support)
        else:
            if request.method in permissions.SAFE_METHODS:
                return True
