from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user  # check´s if the user is the author of the post
    def has_permission(self, request, view):
        return request.user.is_authenticated  # check´s if the user is loged
