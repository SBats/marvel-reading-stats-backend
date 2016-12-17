"""
Marvel views
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
    BasicAuthentication,
)
import marvel.serializers
from marvel.models import (
    Character,
    Comic,
    Creator,
    Event,
    Series
)
from marvel.permissions import IsAccountAdminOrReadOnly


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
    list_serializer = marvel.serializers.CharacterListSerializer
    serializer_class = marvel.serializers.CharacterSerializer

    def get_queryset(self):
        queryset = Character.objects.all()
        starting = self.request.query_params.get('startWith', None)
        if starting is not None:
            queryset = queryset.filter(name__iregex=r'^{0}'.format(starting))
        return queryset

    def get_serializer_class(self):
        if (self.request.path == '/characters/'):
            return self.list_serializer
        else:
            return self.serializer_class


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
    list_serializer = marvel.serializers.ComicListSerializer
    serializer_class = marvel.serializers.ComicSerializer

    def get_queryset(self):
        queryset = Comic.objects.all()
        starting = self.request.query_params.get('startWith', None)
        if starting is not None:
            queryset = queryset.filter(title__iregex=r'^{0}'.format(starting))
        return queryset

    def get_serializer_class(self):
        if (self.request.path == '/comics/'):
            return self.list_serializer
        else:
            return self.serializer_class


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
    list_serializer = marvel.serializers.CreatorListSerializer
    serializer_class = marvel.serializers.CreatorSerializer

    def get_queryset(self):
        queryset = Creator.objects.all()
        starting = self.request.query_params.get('startWith', None)
        if starting is not None:
            queryset = queryset.filter(
                full_name__iregex=r'^{0}'.format(starting)
            )
        return queryset

    def get_serializer_class(self):
        if (self.request.path == '/creators/'):
            return self.list_serializer
        else:
            return self.serializer_class


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
    list_serializer = marvel.serializers.EventListSerializer
    serializer_class = marvel.serializers.EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        starting = self.request.query_params.get('startWith', None)
        if starting is not None:
            queryset = queryset.filter(title__iregex=r'^{0}'.format(starting))
        return queryset

    def get_serializer_class(self):
        if (self.request.path == '/events/'):
            return self.list_serializer
        else:
            return self.serializer_class


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
    list_serializer = marvel.serializers.SeriesListSerializer
    serializer_class = marvel.serializers.SeriesSerializer

    def get_queryset(self):
        queryset = Series.objects.all()
        starting = self.request.query_params.get('startWith', None)
        if starting is not None:
            queryset = queryset.filter(title__iregex=r'^{0}'.format(starting))
        return queryset

    def get_serializer_class(self):
        if (self.request.path == '/series/'):
            return self.list_serializer
        else:
            return self.serializer_class
