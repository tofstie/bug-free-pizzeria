from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    current_classes = models.JSONField(null=True, blank=True)
    previous_classes = models.JSONField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects= CustomUserManager()

    def save(self, *args, **kwargs):
        self.username = self.email.split('@')[0]
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.email