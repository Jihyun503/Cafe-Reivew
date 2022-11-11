from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True, primary_key=True, verbose_name="이메일") # 이게 곧 아이디
    pwd = models.CharField(max_length=30, verbose_name="비밀번호")
    nickname = models.CharField(max_length=30, unique=True, verbose_name="닉네임")
    registerDttm = models.DateTimeField(auto_now_add=True)


# Create your models here.
