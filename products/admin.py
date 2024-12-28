from django.contrib import admin
from .models import *

admin.site.register(Comment)
admin.site.register(Hashtag)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author_nickname", "likes_count", "created_at")  # Admin에서 보여줄 필드
    search_fields = ("title", "author_nickname")  # 검색 가능
    ordering = ("-created_at", "likes_count")  # 정렬
    filter_horizontal = ("categories",)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")  # Admin에서 보여줄 필드
    search_fields = ("name",)  # 검색 가능
    ordering = ("-created_at",)  # 정렬
