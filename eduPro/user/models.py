from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=40, unique=False)
    email = models.EmailField(('email address'), unique=True)
    phone = models.CharField(max_length=40, unique=False, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

