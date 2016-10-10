"""
Marvel views
"""

from marvel.models import Character, Comic, Creator, Event, Series
from rest_framework import viewsets
from marvel.permissions import IsAccountAdminOrReadOnly
import marvel.serializers


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows characters to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = marvel.serializers.CharacterSerializer
    permission_classes = [IsAccountAdminOrReadOnly]


class ComicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comics to be viewed or edited
    """
    queryset = Comic.objects.all()
    serializer_class = marvel.serializers.ComicSerializer
    permission_classes = [IsAccountAdminOrReadOnly]


class CreatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows creators to be viewed or edited
    """
    queryset = Creator.objects.all()
    serializer_class = marvel.serializers.CreatorSerializer
    permission_classes = [IsAccountAdminOrReadOnly]


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited
    """
    queryset = Event.objects.all()
    serializer_class = marvel.serializers.EventSerializer
    permission_classes = [IsAccountAdminOrReadOnly]


class SeriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows series to be viewed or edited
    """
    queryset = Series.objects.all()
    serializer_class = marvel.serializers.SeriesSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
