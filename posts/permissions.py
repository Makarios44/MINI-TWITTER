from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user  # Verifica se o usuário é o autor do post

    def has_permission(self, request, view):
        return request.user.is_authenticated  # Verifica se o usuário está autenticado
