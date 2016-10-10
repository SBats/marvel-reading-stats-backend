"""Marvel Serializers"""

from rest_framework import serializers
from marvel.models import Character, Comic, Creator, Event, Series


class CharacterSerializer(serializers.ModelSerializer):
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
        depth = 1


class CreatorSerializer(serializers.ModelSerializer):
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
        depth = 1


class EventSerializer(serializers.ModelSerializer):
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
        depth = 1


class SeriesSerializer(serializers.ModelSerializer):
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
        depth = 1


class ComicSerializer(serializers.ModelSerializer):
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
        depth = 1
