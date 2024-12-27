from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *


class ArticleListAPIView(APIView):
    # 목록 조회의 경우, 비로그인 상태에서도 가능하도록 get_permissions() 오버라이딩
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailAPIView(APIView):
    # 상세 조회의 경우, 비로그인 상태에서도 가능하도록 get_permissions() 오버라이딩
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        if article.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ArticleDetailSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        article = self.get_object(pk)
        if article.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, article_pk):
        # 정참조
        # comments = Comment.objects.filter(article_id=article_pk)
        # serializer = CommentSerializer(comments, many=True)
        # return Response(serializer.data)

        # 역참조
        article = get_object_or_404(Article, pk=article_pk)
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, author=request.user)
            # serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk)

    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# @api_view(["GET", "POST"])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(["GET", "PUT", "DELETE"])
# def article_detail(request, pk):
#     if request.method == "GET":
#         article = get_object_or_404(Article, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         article = get_object_or_404(Article, pk=pk)
#         serializer = ArticleSerializer(article, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

#     elif request.method == "DELETE":
#         article = get_object_or_404(Article, pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)