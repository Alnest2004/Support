from rest_framework import serializers
from Support.models import Message, StatusMessage, CategoryMessage
from users.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        exclude = ("password", "groups", "user_permissions",)


class MessagesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.SlugRelatedField(slug_field="name", queryset=StatusMessage.objects.all())
    cat = serializers.SlugRelatedField(slug_field="name", queryset=CategoryMessage.objects.all())

    class Meta:
        model = Message
        exclude = ("addressee",)
