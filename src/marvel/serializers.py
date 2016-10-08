"""Marvel Serializers"""

from rest_framework import serializers
from marvel.models import Character, Comic, Creator, Event, Series


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    """Marvel Character DRF serializer"""
    class Meta:
        model = Character
        fields = (
            'marvelId',
            'name',
            'description',
            'url',
            'thumbnail',
            'comics',
            'events',
            'seriesList',
            )


class CreatorSerializer(serializers.HyperlinkedModelSerializer):
    """Marvel Creator DRF serializer"""
    class Meta:
        model = Creator
        fields = (
            'marvelId',
            'firstName',
            'lastName',
            'suffix',
            'fullName',
            'url',
            'thumbnail',
            'comics',
            'events',
            'seriesList',
            )


class EventSerializer(serializers.HyperlinkedModelSerializer):
    """Marvel Event DRF serializer"""
    class Meta:
        model = Event
        fields = (
            'marvelId',
            'title',
            'description',
            'url',
            'start',
            'end',
            'thumbnail',
            'seriesList',
            'characters',
            'creators',
            'comics',
            )


class SeriesSerializer(serializers.HyperlinkedModelSerializer):
    """Marvel Series DRF serializer"""
    class Meta:
        model = Series
        fields = (
            'marvelId',
            'title',
            'description',
            'url',
            'startYear',
            'endYear',
            'thumbnail',
            'events',
            'characters',
            'creators',
            'comics',
            )


class ComicSerializer(serializers.HyperlinkedModelSerializer):
    """Marvel Comic DRF serializer"""
    class Meta:
        model = Comic
        fields = (
            'marvelId',
            'title',
            'variantDescription',
            'description',
            'pageCount',
            'url',
            'date',
            'thumbnail',
            'image',
            'seriesList',
            'creators',
            'characters',
            'events',
            )
