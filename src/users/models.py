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
    rank = models.IntegerField(default=0, blank=True)
    avatar = models.ForeignKey('Avatar', blank=True)
    color = models.CharField(max_length=8, blank=True, default='#d61212')
    collection = models.ManyToManyField('marvel.Comic', blank=True)


class Avatar(models.Model):
    name = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
