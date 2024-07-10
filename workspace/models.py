from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Workspace(models.Model):
    class WorkspaceType(models.TextChoices):
        ADMIN = 'A', _("Admin")
        POWER_USER = 'PU', _("Power_User")

    name = models.CharField(max_length=100, db_index=True)
    workspace_type = models.CharField(choices=WorkspaceType.choices, max_length=1)
    description = models.TextField(blank=True, default="")
    members = models.ManyToManyField(User, through="WorkspaceMember")

    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.name}-{self.workspace_type}"


class WorkspaceMember(models.Model):
    class MemberType(models.TextChoices):
        MANAGER = "MGR", _("Manager")
        TEAM_LEAD = "TL", _("Team_Lead")
        TEAM_MEMBER = "TM", _("Member")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    member_type = models.CharField(
        choices=MemberType.choices, 
        max_length=2, 
        default=MemberType.MEMBER.value
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "workspace"], name="user_workspace_unique"
            )
        ]

    def __str__(self):
        return f"{self.workspace} - {self.user}"
