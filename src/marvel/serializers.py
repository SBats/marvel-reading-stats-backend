"""Marvel Serializers"""

from rest_framework import serializers
from marvel.models import Character, Comic, Creator, Event, Series


class CharacterSerializer(serializers.ModelSerializer):
    """Marvel Character DRF serializer"""
    class Meta:
        model = Character
        fields = (
            'marvel_id',
            'name',
            'description',
            'url',
            'image',
            'comics',
            'events',
            'series_list',
            )
        depth = 1


class CreatorSerializer(serializers.ModelSerializer):
    """Marvel Creator DRF serializer"""
    class Meta:
        model = Creator
        fields = (
            'marvel_id',
            'first_name',
            'last_name',
            'suffix',
            'full_name',
            'url',
            'image',
            'comics',
            'events',
            'series_list',
            )
        depth = 1


class EventSerializer(serializers.ModelSerializer):
    """Marvel Event DRF serializer"""
    class Meta:
        model = Event
        fields = (
            'marvel_id',
            'title',
            'description',
            'url',
            'start',
            'end',
            'image',
            'series_list',
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
            'marvel_id',
            'title',
            'description',
            'url',
            'start_year',
            'end_year',
            'image',
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
            'marvel_id',
            'title',
            'variant_description',
            'description',
            'page_count',
            'url',
            'date',
            'image',
            'image',
            'series_list',
            'creators',
            'characters',
            'events',
            )
        depth = 1
