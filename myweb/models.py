from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 회원가입 공통 질문
    name = models.TextField(max_length=10)
    job = models.TextField(max_length=20)
    address = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone_num=models.TextField(blank=True)
    # 회원가입 개인 질문
    gender = models.TextField(blank=True, default="0")
    date_of_birth=models.TextField(blank=True, default="0000-00-00")
    # 회원가입 기업 질문
    company=models.TextField(blank=True, default="company")