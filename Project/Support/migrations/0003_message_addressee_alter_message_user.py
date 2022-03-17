# Generated by Django 4.0.3 on 2022-03-13 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Support', '0002_user_is_support_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='addressee',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='message_addressee', to=settings.AUTH_USER_MODEL, verbose_name='Получатель'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
