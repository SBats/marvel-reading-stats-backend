from django.db import models


class Creator(models.Model):
    marvelId = models.IntegerField()
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200, blank=True)
    suffix = models.CharField(max_length=200, blank=True)
    fullName = models.CharField(max_length=600)
    url = models.URLField(blank=True)
    thumbnail = models.ImageField(blank=True)
    comics = models.ManyToManyField('Comic', through='Role', blank=True)
    events = models.ManyToManyField('Event', blank=True)
    seriesList = models.ManyToManyField('Series', blank=True)

    def __str__(self):
        return self.fullName

    class Meta:
        ordering = ('firstName',)
