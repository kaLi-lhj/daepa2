from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 회원가입 공통 질문
    # 이름 / 대표자 이름
    name = models.TextField(max_length=10)
    # employee / employer
    job = models.TextField(max_length=20)
    # 주소
    address = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phonenum=models.TextField(blank=True)
    # 회원가입 개인 질문
    gender = models.TextField(blank=True, default="0")
    date_of_birth=models.TextField(blank=True, default="0000-00-00")
    INTEREST_CHOICES = (
        ('1','디자인'),
        ('2','번역'),
        ('3','연구보조'),
        ('4','프로그래밍')
    )
    interest=models.CharField(max_length=2, choices=INTEREST_CHOICES)
    # 회원가입 기업 질문
    company=models.TextField(blank=True, default="company")