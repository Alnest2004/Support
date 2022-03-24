from rest_framework import viewsets, mixins
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import GenericViewSet

from users.models import User
from Support.models import Message
from Support.permissions import IsSupportOrReadOnly
from Support.serializers import UserProfileSerializer, MessagesSerializer


class UserProfileViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsSupportOrReadOnly]


class MessagesDialog(ListCreateAPIView):
    serializer_class = MessagesSerializer
    permission_classes = [IsSupportOrReadOnly]

    def get_queryset(self):
        client = Message.objects.filter(user=self.kwargs['pk'])
        sup = Message.objects.filter(addressee=self.kwargs['pk'])
        return client | sup


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [IsSupportOrReadOnly]
