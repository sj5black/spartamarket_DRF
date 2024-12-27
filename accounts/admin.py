from django.contrib import admin
from .models import CustomUser

# admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in CustomUser._meta.fields] # 모든 필드 표시
    list_display = ("id", "username", "nickname", "email", "is_superuser", "is_staff", "created_at")
    search_fields = ("username", "nickname",)  # 검색 가능
    ordering = ("-created_at", "is_superuser", "is_staff", )  # 정렬