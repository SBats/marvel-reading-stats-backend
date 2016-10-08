"""
Marvel views
"""

from marvel.models import Character, Comic, Creator, Event, Series
from rest_framework import viewsets
import marvel.serializers


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows characters to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = marvel.serializers.CharacterSerializer


class ComicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comics to be viewed or edited
    """
    queryset = Comic.objects.all()
    serializer_class = marvel.serializers.ComicSerializer


class CreatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows creators to be viewed or edited
    """
    queryset = Creator.objects.all()
    serializer_class = marvel.serializers.CreatorSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited
    """
    queryset = Event.objects.all()
    serializer_class = marvel.serializers.EventSerializer


class SeriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows series to be viewed or edited
    """
    queryset = Series.objects.all()
    serializer_class = marvel.serializers.SeriesSerializer
