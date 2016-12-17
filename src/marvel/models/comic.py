from django.db import models


class Comic(models.Model):
    marvel_id = models.IntegerField(primary_key=True)
    title = models.CharField(db_index=True, max_length=200)
    variant_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    issue_number = models.PositiveSmallIntegerField(null=True, blank=True)
    page_count = models.PositiveSmallIntegerField(default=0, blank=True)
    url = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    image = models.ForeignKey('MarvelImage', null=True, blank=True)
    series_list = models.ManyToManyField('Series', blank=True)
    creators = models.ManyToManyField('Creator', through='Role', blank=True)
    characters = models.ManyToManyField('Character', blank=True)
    events = models.ManyToManyField('Event', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
