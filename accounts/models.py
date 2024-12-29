from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# 헬퍼 클래스
class UserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not username:
            raise ValueError('Users must have an email address')
        user = self.model(username=username, password=password, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, password=None, **extra_fields):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """
        superuser = self.create_user(username=username, password=password, **extra_fields)
        
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        
        superuser.save(using=self._db)
        return superuser

# AbstractBaseUser를 상속해서 유저 커스텀
class CustomUser(AbstractBaseUser, PermissionsMixin):
        
    username = models.CharField(max_length=150, unique=True, null=False, blank=False, default='Anonymous')
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False, default='test@gmail.com')
    first_name = models.CharField(max_length=50, null=False, blank=False, default='first')
    last_name = models.CharField(max_length=50, null=False, blank=False, default='last')
    nickname = models.CharField(max_length=30, null=False, blank=False, default='nick')
    birth_date = models.DateField(null=False, blank=False, default='2000-01-01')
        
    # 선택 입력
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    
    # 자동 입력
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
	
    # 헬퍼 클래스 사용
    objects = UserManager()
    USERNAME_FIELD = "username"
    
    # 팔로우 관계 설정 (ManyToMany)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    
    def follow(self, user):
        """ 다른 유저를 팔로우하는 메서드 """
        if user != self:
            self.followings.add(user)

    def unfollow(self, user):
        """ 팔로우 취소하는 메서드 """
        if user != self:
            self.followings.remove(user)

    def is_following(self, user):
        """ 현재 유저가 다른 유저를 팔로우하고 있는지 확인하는 메서드 """
        return self.followings.filter(id=user.id).exists()

    def is_followed_by(self, user):
        """ 다른 유저가 현재 유저를 팔로우하고 있는지 확인하는 메서드 """
        return self.followers.filter(id=user.id).exists()