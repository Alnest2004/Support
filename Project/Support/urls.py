from django.urls import path, include
from .views import UserProfileListView, UserProfileDetailView, MessagesListCreateView, MessagesForSupport, \
    MessagesForClient, MessagesAll, MessageUpdate, MessageDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("accounts/all-profiles", UserProfileListView.as_view(), name="all-profiles"),
    path("accounts/<int:pk>", UserProfileDetailView.as_view(), name="profile"),

    path("all-messages", MessagesListCreateView.as_view(), name="all-messages"),
    path("message/<int:pk>/", MessageDetail.as_view(), name="message"),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("answer_for_support/<int:pk>", MessagesForSupport.as_view(), name="answer_for_support"),
    path("answer_for_client/", MessagesForClient.as_view(), name="answer_for_client"),
    path("dialog/<int:pk>/", MessagesAll.as_view(), name="all"),

    path("change_status/<int:pk>", MessageUpdate.as_view(), name="change"),

    # Регистрация пользователя auth/users/ С методом POST
]
