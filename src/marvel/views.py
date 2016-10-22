"""
Marvel views
"""

from marvel.models import (
    Character,
    Comic,
    Creator,
    Event,
    Series
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
    BasicAuthentication,
)
from marvel.permissions import IsAccountAdminOrReadOnly
import marvel.serializers


class CharacterViewSet(ModelViewSet):
    """
    API endpoint that allows characters to be viewed or edited.
    """
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
        BasicAuthentication
    )
    permission_classes = [IsAccountAdminOrReadOnly]
    queryset = Character.objects.all()
    serializer_class = marvel.serializers.CharacterSerializer


class ComicViewSet(ModelViewSet):
    """
    API endpoint that allows comics to be viewed or edited
    """
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
        BasicAuthentication
    )
    permission_classes = [IsAccountAdminOrReadOnly]
    queryset = Comic.objects.all()
    serializer_class = marvel.serializers.ComicSerializer


class CreatorViewSet(ModelViewSet):
    """
    API endpoint that allows creators to be viewed or edited
    """
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
        BasicAuthentication
    )
    permission_classes = [IsAccountAdminOrReadOnly]
    queryset = Creator.objects.all()
    serializer_class = marvel.serializers.CreatorSerializer


class EventViewSet(ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited
    """
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
        BasicAuthentication
    )
    permission_classes = [IsAccountAdminOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = marvel.serializers.EventSerializer


class SeriesViewSet(ModelViewSet):
    """
    API endpoint that allows series to be viewed or edited
    """
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
        BasicAuthentication
    )
    permission_classes = [IsAccountAdminOrReadOnly]
    queryset = Series.objects.all()
    serializer_class = marvel.serializers.SeriesSerializer
