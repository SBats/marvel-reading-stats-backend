"""
Illustation of a marvel element
"""
from django.db import models


class MarvelImage(models.Model):
    path = models.CharField(max_length=800)
    extension = models.CharField(max_length=10)

    def __str__(self):
        return self.path

    class Meta:
        unique_together = ('path', 'extension',)
        ordering = ('path',)
