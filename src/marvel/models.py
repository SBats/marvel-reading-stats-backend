"""
Marvel models
"""
from django.db import models


class Comic(models.Model):
    """
    Marvel Comic model
    """
    marvelId = models.IntegerField()  # marvelId
    title = models.CharField(max_length=200)  # title
    variantDescription = models.TextField(blank=True)  # variantDescription
    description = models.TextField(blank=True)  # description
    pageCount = models.PositiveSmallIntegerField(default=0, blank=True)  # pageCount
    url = models.URLField(blank=True)  # urls[0]
    date = models.DateField(null=True, blank=True)  # dates[0]
    thumbnail = models.ImageField(blank=True)  # thumbnail[0]
    image = models.ImageField(blank=True)  # images[0]
    seriesList = models.ManyToManyField('Series', through='ComicSeries', blank=True)  # series
    creators = models.ManyToManyField('Creator', through='CreatorComic', blank=True)  # creators
    characters = models.ManyToManyField('Character', through='ComicCharacter', blank=True)  # characters
    events = models.ManyToManyField('Event', through='ComicEvent', blank=True)  # events

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Character(models.Model):
    """
    Marvel Character model
    """
    marvelId = models.IntegerField()  # marvelId
    name = models.CharField(max_length=200)  # name
    description = models.TextField(blank=True)  # description
    url = models.URLField(blank=True)  # urls[0]
    thumbnail = models.ImageField(blank=True)  # thumbnail[0]
    comics = models.ManyToManyField('Comic', through='ComicCharacter', blank=True)  # comics
    events = models.ManyToManyField('Event', through='CharacterEvent', blank=True)  # events
    seriesList = models.ManyToManyField('Series', through='CharacterSeries', blank=True)  # series

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Creator(models.Model):
    """
    Marvel Creator model
    """
    marvelId = models.IntegerField()  # marvelId
    firstName = models.CharField(max_length=200)  # firstName
    lastName = models.CharField(max_length=200, blank=True)  # lastName
    suffix = models.CharField(max_length=200, blank=True)  # suffix
    fullName = models.CharField(max_length=600)  # fullName
    url = models.URLField(blank=True)  # urls[0]
    thumbnail = models.ImageField(blank=True)  # thumbnail[0]
    comics = models.ManyToManyField('Comic', through='CreatorComic', blank=True)  # comics
    events = models.ManyToManyField('Event', through='CreatorEvent', blank=True)  # events
    seriesList = models.ManyToManyField('Series', through='CreatorSeries', blank=True)  # series

    def __str__(self):
        return self.fullName

    class Meta:
        ordering = ('firstName',)


class Series(models.Model):
    """
    Marvel Series model
    """
    marvelId = models.IntegerField()  # marvelId
    title = models.CharField(max_length=200)  # title
    description = models.TextField(blank=True)  # description
    url = models.URLField(blank=True)  # urls[0]
    startYear = models.PositiveSmallIntegerField(null=True, blank=True)  # startYear
    endYear = models.PositiveSmallIntegerField(null=True, blank=True)  # endYear
    thumbnail = models.ImageField(blank=True)  # thumbnail[0]
    characters = models.ManyToManyField('Character', through='CharacterSeries', blank=True)  # characters
    creators = models.ManyToManyField('Creator', through='CreatorSeries', blank=True)  # creators
    comics = models.ManyToManyField('Comic', through='ComicSeries', blank=True)  # comics
    events = models.ManyToManyField('Event', through='SeriesEvent', blank=True)  # events

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Event(models.Model):
    """
    Marvel Event model
    """
    marvelId = models.IntegerField()  # marvelId
    title = models.CharField(max_length=200)  # title
    description = models.TextField(blank=True)  # description
    url = models.URLField(blank=True)  # urls[0]
    start = models.PositiveSmallIntegerField(null=True, blank=True)  # start
    end = models.PositiveSmallIntegerField(null=True, blank=True)  # end
    thumbnail = models.ImageField(blank=True)  # thumbnail[0]
    seriesList = models.ManyToManyField('Series', through='SeriesEvent', blank=True)  # series
    characters = models.ManyToManyField('Character', through='CharacterEvent', blank=True)  # characters
    creators = models.ManyToManyField('Creator', through='CreatorEvent', blank=True)  # creators
    comics = models.ManyToManyField('Comic', through='ComicEvent', blank=True)  # comics

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class CreatorComic(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)


class CreatorEvent(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class CreatorSeries(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    seriesList = models.ForeignKey(Series, on_delete=models.CASCADE)


class SeriesEvent(models.Model):
    seriesList = models.ForeignKey(Series, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class CharacterEvent(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class CharacterSeries(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    seriesList = models.ForeignKey(Series, on_delete=models.CASCADE)


class ComicEvent(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class ComicSeries(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    seriesList = models.ForeignKey(Series, on_delete=models.CASCADE)


class ComicCharacter(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

