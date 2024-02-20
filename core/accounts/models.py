from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    """
        Reprenent custom User model where email is the unique identifier
    """

    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # is_veryfied = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
    
class Profile(models.Model):
    """
        Represent a profile for each user
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
    

@receiver(post_save, sender=User)
def save_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)