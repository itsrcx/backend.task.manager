from rest_framework import permissions

from workspace.models import Workspace

class IsAdminOrPowerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.workspace_set.filter(
                workspace_type__in=[
                    Workspace.WorkspaceType.ADMIN.value,
                    Workspace.WorkspaceType.POWER_USER.value,
                ]
            ).exists()
        )

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.workspace_set.filter(workspace_type='A').exists()
        )
