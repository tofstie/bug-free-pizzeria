from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=50)
    university = models.CharField(max_length=100, blank=False)
    email = models.EmailField(_('email adress'), unique=True)
    current_classes = models.JSONField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects= CustomUserManager()

    def save(self, *args, **kwargs):
        self.username = self.university.split('@')[0]
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.email