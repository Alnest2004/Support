from __future__ import absolute_import
import os
from celery import Celery

# он установит модуль настроек по умолчанию Django для приложения 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

# здесь меняем имя
app = Celery("Project")

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# загрузка tasks.py в приложение django
app.autodiscover_tasks()


#  pip install eventlet
#     celery -A <mymodule> worker -l info -P eventlet