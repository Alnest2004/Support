from rest_framework import serializers
from .models import Message, StatusMessage, CategoryMessage, User


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.SlugRelatedField(slug_field="name", read_only=True)
    cat = serializers.SlugRelatedField(slug_field="name", queryset=CategoryMessage.objects.all())

    class Meta:
        model = Message
        exclude = ("addressee",)


class UpdateSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(slug_field="name", queryset=StatusMessage.objects.all())
    content = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    photo = serializers.ImageField(read_only=True)
    cat = serializers.SlugRelatedField(slug_field="name", read_only=True)
    addressee = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Message
        fields = "__all__"


class MessagesSupportSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.SlugRelatedField(slug_field="name", queryset=StatusMessage.objects.all())
    cat = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
