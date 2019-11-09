from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''It handles permissions to access post request for user Profiles'''

    def has_object_permission(self, request, view, obj):
        '''Check user is trying to update their own Profile'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id