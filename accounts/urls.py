from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path("", SignInOutAPIView.as_view(), name="signinout"),
    path("<str:username>", ProfileAPIView.as_view(), name='profile'),
    path("refresh_token", AuthAPIView.as_view(), name="refresh_token"),
    path("login/", AuthAPIView.as_view(), name="login"),
    path("logout/", AuthAPIView.as_view(), name="logout"),
    path("password/", PasswordAPIView.as_view(), name="password"),
    path('<str:username>/follow/', FollowAPIView.as_view(), name='follow_user'),
    path('<str:username>/unfollow/', UnfollowAPIView.as_view(), name='unfollow_user'),
]
