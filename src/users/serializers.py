from django.contrib.auth.models import User
from users.models import MarvelUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'date_joined')


class MarvelUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MarvelUser
        fields = ('id', 'user', 'level', 'avatar')
