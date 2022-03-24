from django.contrib import admin
from Support.models import Message, CategoryMessage, StatusMessage

admin.site.register(Message)
admin.site.register(CategoryMessage)
admin.site.register(StatusMessage)
