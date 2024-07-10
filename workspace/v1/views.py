from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions

from workspace.models import Workspace, WorkspaceMember
from workspace.v1.permissions import IsAdminOrPowerUser

class WorkspaceViewSet(viewsets.ModelViewSet):

    class WorkspaceSerializer(serializers.ModelSerializer):
        class Meta:
            model = Workspace
            fields = '__all__'

    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer()
    permission_classes = [permissions.IsAuthenticated, IsAdminOrPowerUser]

class WorkspaceMemberViewSet(viewsets.ModelViewSet):

    class WorkspaceMemberSerializer(serializers.ModelSerializer):
        class Meta:
            model = WorkspaceMember
            fields = '__all__'

    queryset = WorkspaceMember.objects.all()
    serializer_class = WorkspaceMemberSerializer()
    permission_classes = [permissions.IsAuthenticated, IsAdminOrPowerUser]
