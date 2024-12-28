from django.urls import path
from .views import *

appname = "products"
urlpatterns = [
    path("", ArticleListAPIView.as_view(), name="article_list"),
    path("search/", ArticleSearchAPIView.as_view(), name="article_search"),
    path("<int:pk>/", ArticleDetailAPIView.as_view(), name="article_detail"),
    path("<int:article_pk>/like/", ArticleLikeAPIView.as_view(), name="article_like"),
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
