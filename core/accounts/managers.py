from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
        Custom Usermanager where email is the uniq identifier
    """
    
    def create_user(self, email, password, **extra_fields):
        """
            create and save user with given email and password
        """

        if not email:
            raise ValueError(_('email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
            create and save a superuser with given email and password and extra_fields
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('superuser must be is_staff'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('supueruser must have is_superuser=True'))
        
        return self.create_user(email, password, **extra_fields)