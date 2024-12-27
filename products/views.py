from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from django.db.models import Q


# 검색 기능(제목, 내용, 작성자 닉네임)
class ArticleSearchAPIView(APIView):
    def get(self, request):
        # 검색어 가져오기
        search_query = request.query_params.get('q', None)

        print("\n\n")
        print(search_query)
        print("\n\n")
        # 검색어가 있을 경우 필터링
        if search_query:
            articles = Article.objects.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query) | 
                Q(author_nickname__icontains=search_query)
            )
        else:
            articles = Article.objects.all()
        
        paginator = ArticlePagination()
        result_page = paginator.paginate_queryset(articles, request)
        serializer = ArticleSerializer(result_page, many=True)
        
        return paginator.get_paginated_response(serializer.data)


class ArticlePagination(PageNumberPagination):
    page_size = 20  # 한 페이지에 보여줄 항목 수
    page_size_query_param = 'page_size'  # 클라이언트가 요청 시 페이지 크기 지정 가능
    max_page_size = 50  # 최대 페이지 크기
    

class ArticleListAPIView(APIView):
    # 목록 조회의 경우, 비로그인 상태에서도 가능하도록 get_permissions() 오버라이딩
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get(self, request):
        articles = Article.objects.all()
        
        # 페이지네이션 적용
        paginator = ArticlePagination()
        result_page = paginator.paginate_queryset(articles, request)
        serializer = ArticleSerializer(result_page, many=True)
        
        # 페이지네이션된 응답 반환
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, author_nickname=request.user.nickname)
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
            serializer.save(article=article, author=request.user, author_nickname=request.user.nickname)
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