from django.contrib import admin
from .models import Message, CategoryMessage, StatusMessage, User


admin.site.register(Message)
admin.site.register(CategoryMessage)
admin.site.register(StatusMessage)
admin.site.register(User)


