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
    photo = models.ImageField(upload_to='books/images', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    file = models.FileField(upload_to='books/file/', null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookImage(models.Model):
    product = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='images')
    photo = models.ImageField(upload_to='books/')