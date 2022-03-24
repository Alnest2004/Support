from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('Support.urls')),
    path('app2/', include('users.urls')),
]
