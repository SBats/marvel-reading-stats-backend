from django.db import models


class Character(models.Model):
    marvel_id = models.IntegerField(primary_key=True)
    name = models.CharField(db_index=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    image = models.ForeignKey('MarvelImage', null=True, blank=True)
    comics = models.ManyToManyField('Comic', blank=True)
    events = models.ManyToManyField('Event', blank=True)
    series_list = models.ManyToManyField('Series', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
