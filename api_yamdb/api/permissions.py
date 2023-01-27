from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.author == (
            request.user)

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated and request.user.is_user)

class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAdminOrSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and (request.user.is_admin or request.user.is_superuser))
    
    def has_objects_permission(self, request, view, obj):
        return (request.user.is_authenticated and (request.user.is_admin or request.user.is_superuser))


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and (request.user.is_moderator or request.user.is_staff))

    def has_objects_permission(self, request, view, obj):
        return (request.user.is_authenticated and (request.user.is_moderator or request.user.is_staff))
