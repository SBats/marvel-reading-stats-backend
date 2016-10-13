"""
Users views
"""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from users.serializers import UserSerializer, GroupSerializer
from users.permissions import IsAccountAdminOrReadOnly, IsSelfOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAccountAdminOrReadOnly, IsSelfOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
