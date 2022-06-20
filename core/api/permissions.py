from curses.ascii import DEL
from rest_framework import permissions
from core.models import Cars


class IsOwnerPermission(permissions.BasePermission):

    def has_permission(self, request, *args, **kwargs):
       def has_object_permission(self, request, view, obj):
            # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # obj here is a UserProfile instance
        return obj.owner == request.user


class IsOwnerImagePermission(permissions.BasePermission):
    
    def has_permission(self, request, *args, **kwargs):
       def has_object_permission(self, request, view, obj):
            # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # obj here is a UserProfile instance
        return obj.cars.first().owner== request.user
