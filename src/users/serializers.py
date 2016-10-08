"""Users App Serializers"""

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerialize(serializers.HyperlinkedModelSerializer):
    """Django users serializer"""
    class Meta:
        """Meta"""
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Django groups serializer"""
    class Meta:
        """Meta"""
        model = Group
        fields = ('url', 'name')