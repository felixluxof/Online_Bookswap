from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='account/')

