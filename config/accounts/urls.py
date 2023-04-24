from django.urls import path
from .views import (
    UserCreateView,
    UserListView,
    UserUpdateView,
    UserDeleteView,
    CustomAuthToken,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = "accounts"
urlpatterns = [
    path("user/all/", UserListView.as_view(), name="user_list"),
    path("user/", UserCreateView.as_view(), name="user_create"),
    path("user/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("user/delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
    # authentication
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api-token-auth/", CustomAuthToken.as_view()),
]
