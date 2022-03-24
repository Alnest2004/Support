from django.db import models
from django.urls import reverse

from users.models import User


class CategoryMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category_name")

    def __str__(self):
        return self.name


class StatusMessage(models.Model):
    name = models.CharField(max_length=30, verbose_name="Status_name")

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, related_name="message_user", on_delete=models.CASCADE, verbose_name="User")
    addressee = models.ForeignKey(User, related_name="message_addressee", default=2, on_delete=models.CASCADE,
                                  verbose_name="Recipient")
    title = models.CharField(max_length=255, verbose_name="The headline of the message")
    content = models.TextField(verbose_name="Article text")
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time of creation")
    cat = models.ForeignKey(CategoryMessage, default=4, on_delete=models.PROTECT, verbose_name="Categories")
    status = models.ForeignKey(StatusMessage, default=2, on_delete=models.CASCADE, verbose_name="Message status")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('message-detail', kwargs={'pk': self.pk})
