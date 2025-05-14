from django.db import models

from account.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)


class Books(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='books/')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookImage(models.Model):
    product = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='images')
    photo = models.ImageField(upload_to='books/')