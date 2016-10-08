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
    variantDescription = models.TextField()  # variantDescription
    description = models.TextField()  # description
    pageCount = models.PositiveSmallIntegerField()  # pageCount
    url = models.URLField()  # urls[0]
    date = models.DateField()  # dates[0]
    thumbnail = models.ImageField()  # thumbnail[0]
    image = models.ImageField()  # images[0]
    seriesList = models.ManyToManyField('Series', through='ComicSeries')  # series
    creators = models.ManyToManyField('Creator', through='CreatorComic')  # creators
    characters = models.ManyToManyField('Character', through='ComicCharacter')  # characters
    events = models.ManyToManyField('Event', through='ComicEvent')  # events

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
    description = models.TextField()  # description
    url = models.URLField()  # urls[0]
    thumbnail = models.ImageField()  # thumbnail[0]
    comics = models.ManyToManyField('Comic', through='ComicCharacter')  # comics
    events = models.ManyToManyField('Event', through='CharacterEvent')  # events
    seriesList = models.ManyToManyField('Series', through='CharacterSeries')  # series

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
    lastName = models.CharField(max_length=200)  # lastName
    suffix = models.CharField(max_length=200)  # suffix
    fullName = models.CharField(max_length=600)  # fullName
    url = models.URLField()  # urls[0]
    thumbnail = models.ImageField()  # thumbnail[0]
    comics = models.ManyToManyField('Comic', through='CreatorComic')  # comics
    events = models.ManyToManyField('Event', through='CreatorEvent')  # events
    seriesList = models.ManyToManyField('Series', through='CreatorSeries')  # series

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
    description = models.TextField()  # description
    url = models.URLField()  # urls[0]
    startYear = models.PositiveSmallIntegerField()  # startYear
    endYear = models.PositiveSmallIntegerField()  # endYear
    thumbnail = models.ImageField()  # thumbnail[0]
    characters = models.ManyToManyField('Character', through='CharacterSeries')  # characters
    creators = models.ManyToManyField('Creator', through='CreatorSeries')  # creators
    comics = models.ManyToManyField('Comic', through='ComicSeries')  # comics
    events = models.ManyToManyField('Event', 'SeriesEvent')  # events

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
    description = models.TextField()  # description
    url = models.URLField()  # urls[0]
    start = models.PositiveSmallIntegerField()  # start
    end = models.PositiveSmallIntegerField()  # end
    thumbnail = models.ImageField()  # thumbnail[0]
    seriesList = models.ManyToManyField('Series', through='SeriesEvent')  # series
    characters = models.ManyToManyField('Character', through='CharacterEvent')  # characters
    creators = models.ManyToManyField('Creator', through='CreatorEvent')  # creators
    comics = models.ManyToManyField('Comic', through='ComicEvent')  # comics

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

