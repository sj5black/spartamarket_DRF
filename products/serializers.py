from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article", 'author')
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("article")
        return ret


class ArticleSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',  # 'name'을 기준으로 카테고리 연결
        many=True
    )
    
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ['author', 'created_at', 'updated_at']


class ArticleDetailSerializer(ArticleSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source="comment_set.count", read_only=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
