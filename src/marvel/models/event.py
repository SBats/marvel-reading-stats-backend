from django.db import models


class Event(models.Model):
    marvel_id = models.IntegerField(primary_key=True)
    title = models.CharField(db_index=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    image = models.ForeignKey('MarvelImage', null=True, blank=True)
    series_list = models.ManyToManyField('Series', blank=True)
    characters = models.ManyToManyField('Character', blank=True)
    creators = models.ManyToManyField('Creator', blank=True)
    comics = models.ManyToManyField('Comic', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
