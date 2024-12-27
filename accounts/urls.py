from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path("", RegisterAPIView.as_view(), name="register"),
    path("<str:username>/", ProfileAPIView.as_view(), name='profile'),
    path("refresh_token", AuthAPIView.as_view(), name="refresh_token"),
    path("login", AuthAPIView.as_view(), name="login"),
    path("logout", AuthAPIView.as_view(), name="logout"),
]
