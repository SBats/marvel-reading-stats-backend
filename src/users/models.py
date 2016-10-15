"""
Users models
"""
from django.db import models
from django.contrib.auth.models import User


class MarvelUser(models.Model):
    """
    Marvel users
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default=0, blank=True)
    avatar = models.ImageField(blank=True)
