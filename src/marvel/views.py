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

    def get_queryset(self):
        queryset = Character.objects.all()
        starting = self.request.query_params.get('startWith', None)
        if starting is not None:
            queryset = queryset.filter(name__iregex=r'^{0}'.format(starting))
        return queryset


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

    def get_queryset(self):
        queryset = Comic.objects.all()
        starting = self.request.query_params.get('startWith', None)
        if starting is not None:
            queryset = queryset.filter(title__iregex=r'^{0}'.format(starting))
        return queryset


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

    def get_queryset(self):
        queryset = Creator.objects.all()
        starting = self.request.query_params.get('startWith', None)
        if starting is not None:
            queryset = queryset.filter(full_name__iregex=r'^{0}'.format(starting))
        return queryset


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

    def get_queryset(self):
        queryset = Event.objects.all()
        starting = self.request.query_params.get('startWith', None)
        if starting is not None:
            queryset = queryset.filter(title__iregex=r'^{0}'.format(starting))
        return queryset


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

    def get_queryset(self):
        queryset = Series.objects.all()
        starting = self.request.query_params.get('startWith', None)
        if starting is not None:
            queryset = queryset.filter(title__iregex=r'^{0}'.format(starting))
        return queryset
