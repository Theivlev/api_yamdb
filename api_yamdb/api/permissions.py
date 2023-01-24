# from rest_framework import permissions


# class IsAdminOrSuperuser(permissions.BasePermission):
#     """
#     Доступ на изменение контента только для админа и суперюзера.
#     """
#     message = 'Нет прав доступа.'

#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         if not request.user.is_authenticated:
#             return False
#         if request.user.role == 'admin' or request.user.is_superuser:
#             return True
#         return False


# class IsAuthOrAdminOrModerator(permissions.BasePermission):
#     """
#     Доступ на изменение контента только для админа
#     для автора, администратора и модератора.
#     """
#     message = 'Изменение чужого контента запрещено!'

#     def has_permission(self, request, view):
#         return (request.method in permissions.SAFE_METHODS
#                 or request.user.is_authenticated)

#     def has_object_permission(self, request, view, obj):
#         return (request.method in permissions.SAFE_METHODS
#                 or request.user.role == 'admin'
#                 or request.user.role == 'moderator'
#                 or obj.author == request.user)