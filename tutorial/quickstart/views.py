# Group common behavior together using view set rather than creating multiple views
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets

from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    # Endpoint - User View or edit
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    # Endpoint - Group View or edit
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
