from django.db import models


class Comic(models.Model):
    marvelId = models.IntegerField()
    title = models.CharField(max_length=200)
    variantDescription = models.TextField(blank=True)
    description = models.TextField(blank=True)
    pageCount = models.PositiveSmallIntegerField(default=0, blank=True)
    url = models.URLField(blank=True)
    date = models.DateField(null=True, blank=True)
    thumbnail = models.ImageField(blank=True)
    image = models.ImageField(blank=True)
    seriesList = models.ManyToManyField('Series', blank=True)
    creators = models.ManyToManyField('Creator', through='Role', blank=True)
    characters = models.ManyToManyField('Character', blank=True)
    events = models.ManyToManyField('Event', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
