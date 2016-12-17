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


class CharacterListSerializer(serializers.ModelSerializer):
    """Marvel Character DRF serializer"""
    class Meta:
        model = Character
        fields = (
            'marvel_id',
            'name',
            )


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


class CreatorListSerializer(serializers.ModelSerializer):
    """Marvel Creator DRF serializer"""
    class Meta:
        model = Creator
        fields = (
            'marvel_id',
            'full_name',
            )


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


class EventListSerializer(serializers.ModelSerializer):
    """Marvel Event DRF serializer"""
    class Meta:
        model = Event
        fields = (
            'marvel_id',
            'title',
            )


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


class SeriesListSerializer(serializers.ModelSerializer):
    """Marvel Series DRF serializer"""
    class Meta:
        model = Series
        fields = (
            'marvel_id',
            'title',
            )


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


class ComicListSerializer(serializers.ModelSerializer):
    """Marvel Comic DRF serializer"""
    class Meta:
        model = Comic
        fields = (
            'marvel_id',
            'title',
            )
