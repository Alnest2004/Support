from django.urls import path, include
from rest_framework import routers

from Support.views import UserProfileViewSet, MessagesDialog, MessagesViewSet

router = routers.SimpleRouter()
router.register(r'messages', MessagesViewSet)

router2 = routers.SimpleRouter()
router2.register(r'accounts', UserProfileViewSet)

urlpatterns = [
    path('support/', include(router.urls)),  # http://127.0.0.1:8000/support/messages/
    path('support/', include(router2.urls)),  # http://127.0.0.1:8000/support/accounts/

    path("dialog/<int:pk>/", MessagesDialog.as_view(), name="dialog"),
]
