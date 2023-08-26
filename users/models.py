from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=13, unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']
    objects = UserManager()

    def __str__(self):
        return self.name
