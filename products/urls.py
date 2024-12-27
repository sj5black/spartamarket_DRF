from django.urls import path
from .views import *

appname = "products"
urlpatterns = [
    path("", ArticleListAPIView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailAPIView.as_view(), name="article_detail"),
    path(
        "<int:article_pk>/comments/",
        CommentListAPIView.as_view(),
        name="comment_list",
    ),
    path(
        "comments/<int:comment_pk>/",
        CommentDetailAPIView.as_view(),
        name="comment_detail",
    ),
]
