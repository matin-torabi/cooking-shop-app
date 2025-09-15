from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    '''
    Admins permission
    '''
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name="admin").exists()