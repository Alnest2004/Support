from django.db import models
from django.contrib.auth.models import AbstractUser


class CategoryMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория")

    def __str__(self):
        return self.name


class StatusMessage(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя статуса")

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_support = models.BooleanField(default=False, verbose_name="Поддержка ли он")


class Message(models.Model):
    user = models.ForeignKey(User, related_name="message_user", on_delete=models.CASCADE, verbose_name="Пользователь")
    addressee = models.ForeignKey(User, related_name="message_addressee", default=2, on_delete=models.CASCADE,
                                  verbose_name="Получатель")
    title = models.CharField(max_length=255, verbose_name="Заголовок сообщения")
    content = models.TextField(verbose_name="Текст статьи")
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    cat = models.ForeignKey(CategoryMessage, default=4, on_delete=models.PROTECT, verbose_name="Категории")
    status = models.ForeignKey(StatusMessage, default=2, on_delete=models.CASCADE, verbose_name="Статус сообщения")

    def __str__(self):
        return self.title


# class Dialog(models.Model):
#     client = models.ForeignKey(User, related_name="dialog_user", on_delete=models.CASCADE, verbose_name="Пользователь")
#     support = models.ForeignKey(User, related_name="dialog_support", default=2, on_delete=models.CASCADE,
#                                   verbose_name="Помощник")