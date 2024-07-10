from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workspace.v1.views import WorkspaceViewSet, WorkspaceMemberViewSet

router = DefaultRouter()
router.register(r'workspaces', WorkspaceViewSet)
router.register(r'workspace-members', WorkspaceMemberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
