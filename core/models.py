from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom User Manager

    Creates and saves a User with the given email and password.
    Creates and saves a Admin User with the given email and password.
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom User Model"""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    email = models.EmailField(unique=True, max_length=255)
    username = None
    password = models.CharField(max_length=256)

    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    history = HistoricalRecords()

    def get_full_name(self) -> str:
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"
