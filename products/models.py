import os
from django.conf import settings
from django.db import models
from .utils import parse_hashtags


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 카테고리 이름 (유일해야 함)
    created_at = models.DateField(auto_now_add=True)  # 생성날짜 자동 기록

    def __str__(self):
        return self.name


class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_nickname = models.CharField(
        max_length=30, null=False, blank=False, default="Anonymous"
    )

    categories = models.ManyToManyField(Category, blank=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles", blank=True
    )
    likes_count = models.PositiveIntegerField(default=0)
    hashtags = models.ManyToManyField(Hashtag, related_name="articles", blank=True)
    hashtags_input = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        # 이미지 수정 시 이전 이미지 삭제
        if self.pk:  # 이미 존재하는 Article을 수정하는 경우
            old_article = Article.objects.get(pk=self.pk)
            if old_article.image and old_article.image != self.image:  # 이미지가 변경되었을 때
                # 기존 이미지 파일 삭제
                old_image_path = old_article.image.path
                if os.path.isfile(old_image_path):
                    os.remove(old_image_path)

        super().save(*args, **kwargs)  # 부모 클래스의 save() 호출

    def delete(self, *args, **kwargs):
        # Article 삭제 시 이미지 파일도 삭제
        if self.image:
            image_path = self.image.path
            if os.path.isfile(image_path):
                os.remove(image_path)
                
    def add_hashtag(self):
        parsed_hashtags = parse_hashtags(self.hashtags_input)
        for hashtag in parsed_hashtags:
            hashtag_obj, created = Hashtag.objects.get_or_create(name=hashtag)
            self.hashtags.add(hashtag_obj)

    def remove_hashtag(self):
        self.hashtags.clear()
        
    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_nickname = models.CharField(
        max_length=30, null=False, blank=False, default="Anonymous"
    )

    def __str__(self):
        return self.content
