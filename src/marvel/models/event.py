from django.db import models


class Event(models.Model):
    marvelId = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    start = models.PositiveSmallIntegerField(null=True, blank=True)
    end = models.PositiveSmallIntegerField(null=True, blank=True)
    thumbnail = models.ImageField(blank=True)
    seriesList = models.ManyToManyField('Series', blank=True)
    characters = models.ManyToManyField('Character', blank=True)
    creators = models.ManyToManyField('Creator', blank=True)
    comics = models.ManyToManyField('Comic', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
