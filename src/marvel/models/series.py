from django.db import models


class Series(models.Model):
    marvel_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    start_year = models.PositiveSmallIntegerField(null=True, blank=True)
    end_year = models.PositiveSmallIntegerField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    characters = models.ManyToManyField('Character', blank=True)
    creators = models.ManyToManyField('Creator', blank=True)
    comics = models.ManyToManyField('Comic', blank=True)
    events = models.ManyToManyField('Event', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
