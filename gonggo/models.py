from django.db import models
from django.contrib.auth.models import User

class Gonggo(models.Model):
    
    title=models.CharField(max_length=100)
    INTEREST_CHOICES = (
        ('1','디자인'),
        ('2','번역'),
        ('3','연구보조'),
        ('4','프로그래밍')
    )
    interest=models.CharField(max_length=2, choices=INTEREST_CHOICES,default="a")
    workDetail=models.TextField(max_length=100,default="a")
    person=models.CharField(max_length=2, default="a")
    serviceAddr2=models.CharField(max_length=100,default="a")
    salary=models.CharField(max_length=100,default="a")
    minMoney=models.CharField(max_length=100,default="a")
    highMoney=models.CharField(max_length=100,default="a")
    workTimeDetailContent=models.TextField(max_length=300,default="a")
    manager1=models.CharField(max_length=100,default="a")
    phonenum=models.CharField(max_length=20,default="a")
    email=models.CharField(max_length=30,default="a")



