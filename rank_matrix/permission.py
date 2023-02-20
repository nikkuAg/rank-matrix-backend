from rest_framework import permissions


class CustomApiPermission(permissions.BasePermission):

    message = 'You dont have permission to perform this action!!'

    allow_permissions = ["GET"]

    def has_permission(self, request, view):
        if request.method in self.allow_permissions or (request.user.is_staff and request.user.is_superuser):
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in self.allow_permissions or (request.user.is_staff and request.user.is_superuser):
            return True
