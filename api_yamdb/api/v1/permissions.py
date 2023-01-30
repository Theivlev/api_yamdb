from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Права для чтения или авторизованного пользователя"""
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.author == (
            request.user)

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated and request.user.is_user)


class ReadOnly(permissions.BasePermission):
    """Права только для чтения"""
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAdminOrSuperuser(permissions.BasePermission):
    """Права только для администратора и суперюзера"""
    def has_permission(self, request, view):
        return ((
            request.user.is_authenticated and request.user.is_admin)
            or request.user.is_superuser)

    def has_objects_permission(self, request, view, obj):
        return (request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser))


class IsAdmin(permissions.BasePermission):
    """Права только администратора"""
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_admin)

    def has_objects_permission(self, request, view, obj):
        return (request.user.is_authenticated and (request.user.is_admin))


class IsModerator(permissions.BasePermission):
    """Права только для модератора"""
    def has_permission(self, request, view):
        return (request.user.is_authenticated and (
            request.user.is_moderator or request.user.is_staff))

    def has_objects_permission(self, request, view, obj):
        return (request.user.is_authenticated and (
            request.user.is_moderator or request.user.is_staff))


class IsReviewAndComment(permissions.IsAuthenticatedOrReadOnly):
    """Права для работы с отзывами и комментариями."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_admin
            or obj.author == request.user
            or request.user.is_moderator
            or request.user.is_superuser
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Права для работы с категориями и жанрами."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
        )
