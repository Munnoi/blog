from django.contrib.auth.models import BaseUserManager

"""
BaseUserManager:
email normalization
standard user creation hooks
"""


class AccountsManager(BaseUserManager):
    # This method is called when a user registers
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email)  # Creates a user instance
        user.set_password(password)  # Hashing
        user.save(using=self._db)  # Saves user to database
        return user

    # This method is called when a superuser is created
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
