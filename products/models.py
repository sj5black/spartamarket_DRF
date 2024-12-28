from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 카테고리 이름 (유일해야 함)
    created_at = models.DateField(auto_now_add=True)  # 생성날짜 자동 기록
    
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_nickname = models.CharField(max_length=30, null=False, blank=False, default='Anonymous')
    categories = models.ManyToManyField(Category, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL , related_name="like_articles", blank=True)
    likes_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_nickname = models.CharField(max_length=30, null=False, blank=False, default='Anonymous')
    
    def __str__(self):
        return self.content
    
    
