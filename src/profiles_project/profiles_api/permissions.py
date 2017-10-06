from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_objest_permission(self,request,view,obj):
        """check the user which is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id
