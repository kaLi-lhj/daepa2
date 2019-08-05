"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, re_path, path
from django.contrib import admin
from myweb.views import mainIndex, regAccount, modiAccount, join1, join2, main, modi
from django.contrib.auth import views as auth_views



urlpatterns = [
    # 127.0.0.1:8000/
    re_path(r'^$', mainIndex, name='index'),

    # 127.0.0.1:8000/admin/...
    path('admin/', admin.site.urls),
    re_path(r'^account/register/$', regAccount, name='reg_account'),

    re_path(r'^account/modified/$', modiAccount, name='modi_account'),
    
    re_path(r'^account/register/join1/$', join1, name='join1'),

    re_path(r'^account/register/join2/$', join2, name='join2'),

    # 127.0.0.1:8000/board/...
    re_path(r'^board/', include(r'board.urls')),

    # 127.0.0.1:8000/news/...
    re_path(r'^news/', include(r'news.urls')),

    # 127.0.0.1:8000/webtoon/...
    re_path(r'^webtoon/', include(r'webtoon.urls')),

    # 127.0.0.1:8000/gonggo/...
    re_path(r'^gonggo/', include(r'gonggo.urls')),

    # /error/
    re_path(r'^error/', include(r'error.urls')),

    # 127.0.0.1:8000/modi/...
    re_path(r'^modi/', modi, name='modi'),
    
    # 로그인-로그아웃
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # 127.0.0.1:8000/main/...
    re_path(r'^main/', main, name='main'),
]
# 정규 표현식
# [0-9] : 정수값 0 ~ 9 까지 패턴
# [a-z] : 소문자 a ~ z 까지 패턴
# [A-Z] : 대문자 A ~ Z 까지 패턴
# + : 1자리 이상
# {n} : n자리
# {n,m} : n 자리 ~ m 자리 까지
# (...) : () 안에 값을 저장 후 함수의 인자로 전달