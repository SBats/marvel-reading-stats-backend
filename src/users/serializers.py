"""Users App Serializers"""

from users.models import MarvelUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Django users serializer"""
    class Meta:
        """Meta"""
        model = MarvelUser
        fields = ('user', 'level', 'avatar')
        depth = 1
