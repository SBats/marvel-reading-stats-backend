from django.contrib.auth.models import User
from users.models import MarvelUser, Avatar
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'date_joined')


class AvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avatar
        fields = ('id', 'name', 'thumbnail', 'image')


class MarvelUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    avatar = AvatarSerializer()

    class Meta:
        model = MarvelUser
        fields = ('id', 'user', 'level', 'rank', 'avatar', 'collection')
