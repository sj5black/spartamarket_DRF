from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",)
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("article")
        return ret


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        # author 필드를 읽기 전용으로 설정
        read_only_fields = ['author', 'created_at', 'updated_at']
        # exclude = ['author_id']
        
    # def create(self, validated_data):
    #     user = self.context['request'].user  # 로그인한 유저 정보 가져오기
    #     validated_data['author_id'] = user  # author 필드에 유저 정보 추가

    #     # 기본 create 메서드처럼 validated_data를 사용하여 객체 생성
    #     article = Article.objects.create(**validated_data)
    #     return article


class ArticleDetailSerializer(ArticleSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source="comment_set.count", read_only=True)

