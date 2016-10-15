"""
Users views
"""

from rest_framework import viewsets
from users.models import MarvelUser
from users.serializers import UserSerializer
from users.permissions import IsAccountAdminOrReadOnly, IsSelfOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MarvelUser.objects.all().order_by('level')
    serializer_class = UserSerializer
    permission_classes = [IsAccountAdminOrReadOnly, IsSelfOrReadOnly]
