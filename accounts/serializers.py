from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import InvalidToken
import pdb

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = "__all__"

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("이미 사용중인 이메일입니다.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.save()
        return user


class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "nickname", "birth_date", "gender", "intro"]
        
    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.nickname = validated_data.get("nickname", instance.nickname)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.intro = validated_data.get("intro", instance.intro)
        instance.save()
        return instance
        
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token