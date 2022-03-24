from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_support = models.BooleanField(default=False, verbose_name="It's support")
