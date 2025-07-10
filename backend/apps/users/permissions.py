from rest_framework.permissions import BasePermission


# custom permission class for super_user
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)