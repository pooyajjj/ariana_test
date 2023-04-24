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
    path("api-token-auth/", CustomAuthToken.as_view()),
    path("user/all/", UserListView.as_view(), name="user_list"),
    path("user/", UserCreateView.as_view(), name="user_create"),
    path("user/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("user/delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
    # authentication
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path('token/login/', login, name='login'),
]

# {
# 	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjQxNjkyMSwiaWF0IjoxNjgyMzMwNTIxLCJqdGkiOiIxNjQ0NzQ3ZTA5Yjc0MDc4YWU0ZWZhN2VhYThkZjg0NSIsInVzZXJfaWQiOjZ9.r6_blfwLBw2EtazzVbnVHqJtca5JRzWmhYQg6Gkr-ag",
# 	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyMzMwODIxLCJpYXQiOjE2ODIzMzA1MjEsImp0aSI6ImI1OWFmOTVhMDViMTQ4ZTE5NmY3MTE0YWZkZGI4ZTMzIiwidXNlcl9pZCI6Nn0.LuZNTDbAHk0WMQkQbLg57ZiqBw7vBZVieEL_87o6B34"
# }
