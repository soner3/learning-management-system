import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from core_apps.users.managers import UserManager


class User(AbstractUser):

    pkid: models.BigAutoField = models.BigAutoField(primary_key=True, editable=False)
    id: models.UUIDField = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False
    )
    first_name: models.CharField = models.CharField(
        verbose_name=_("First name"), max_length=60
    )
    last_name: models.CharField = models.CharField(
        verbose_name=_("Last name"), max_length=60
    )
    email: models.EmailField = models.EmailField(
        verbose_name=_("Email Address"), unique=True, db_index=True
    )
    username: models.CharField = models.CharField(
        verbose_name=_("Username"),
        unique=True,
        max_length=60,
        validators=[UnicodeUsernameValidator],
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
    ]

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]

    @property
    def get_full_name(self) -> str:
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
