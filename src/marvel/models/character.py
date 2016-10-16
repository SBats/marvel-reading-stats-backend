from django.db import models


class Character(models.Model):
    marvelId = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    thumbnail = models.ImageField(blank=True)
    comics = models.ManyToManyField('Comic', blank=True)
    events = models.ManyToManyField('Event', blank=True)
    seriesList = models.ManyToManyField('Series', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
