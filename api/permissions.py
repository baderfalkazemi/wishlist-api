from rest_framework.permissions import BasePermission

class IsCreator(BasePermission):
    message = "You must be the person who added this product!"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.added_by == request.user):
            return True
        else:
            return False