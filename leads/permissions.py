from rest_framework.permissions import BasePermission


class LeadAccessPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        if view.action == "create":
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
