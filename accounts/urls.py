from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path("", views.RegisterAPIView.as_view(), name="register"),
    path("<str:username>/", views.ProfileAPIView.as_view(), name='profile'),
    path("refresh_token", views.AuthAPIView.as_view(), name="refresh_token"),
    path("login", views.AuthAPIView.as_view(), name="login"),
    path("logout", views.AuthAPIView.as_view(), name="logout"),
]
