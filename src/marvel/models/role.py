"""
Rôle of the Creator in making the Comic
"""
from django.db import models


class Role(models.Model):
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    comic = models.ForeignKey('Comic', on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
