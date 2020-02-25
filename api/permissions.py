from rest_framework.permissions import BasePermission

class IsAddedBy(BasePermission):
    message = "did not add this!!!"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.added_by == request.user:
            return True
        return False
