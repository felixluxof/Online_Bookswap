from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()



class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    description = models.TextField()
    is_checked = models.BooleanField(default=False)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Inform(models.Model):
    tel = models.CharField(max_length=13)
    tel1 = models.CharField(max_length=13)
    description = models.TextField()
    telegram = models.URLField()