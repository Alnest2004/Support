from rest_framework.generics import (ListCreateAPIView, ListAPIView,
                                     RetrieveUpdateAPIView, )
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Message
from .permissions import IsSupportOrReadOnly
from .models import User

from .serializers import UserProfileSerializer, MessagesSerializer, MessagesSupportSerializer, UpdateSerializer


class UserProfileListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]


class UserProfileDetailView(ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsSupportOrReadOnly]

    def get_queryset(self):
        user = User.objects.filter(id=self.kwargs['pk'])
        return user


class MessagesListCreateView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [IsSupportOrReadOnly]


class MessagesForSupport(ListCreateAPIView):
    serializer_class = MessagesSupportSerializer
    permission_classes = [IsSupportOrReadOnly]

    def get_queryset(self):
        client = Message.objects.filter(user=self.kwargs['pk'])
        return client


class MessagesForClient(ListCreateAPIView):
    serializer_class = MessagesSupportSerializer
    permission_classes = [IsSupportOrReadOnly]

    def get_queryset(self):
        client = Message.objects.filter(addressee=self.request.user.id)
        return client


class MessagesAll(ListCreateAPIView):
    serializer_class = MessagesSupportSerializer
    permission_classes = [IsSupportOrReadOnly]

    def get_queryset(self):
        client = Message.objects.filter(user=self.kwargs['pk'])
        sup = Message.objects.filter(addressee=self.kwargs['pk'])
        return client | sup


class MessageDetail(ListAPIView):
    serializer_class = MessagesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = Message.objects.filter(id=self.kwargs['pk'])
        return user


class MessageUpdate(RetrieveUpdateAPIView):
    serializer_class = UpdateSerializer
    permission_classes = [IsSupportOrReadOnly]

    def get_queryset(self):
        queryset = Message.objects.filter(pk=self.kwargs['pk'])
        return queryset
