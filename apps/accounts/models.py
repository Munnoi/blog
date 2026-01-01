from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import AccountsManager

"""
models → define DB fields

AbstractBaseUser → gives:
password hashing
last_login

PermissionsMixin → gives:
groups
permissions
is_superuser

timezone → timezone-aware timestamps

AccountsManager → custom logic to create users
"""


class Accounts(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"  # For using 'email' instead of 'username'
    REQUIRED_FIELDS = []  # Fields required when creating superusers (besides email). Empty = only email + password required

    objects = AccountsManager()  # Connects models.py to managers.py

    def __str__(self):
        return self.email
