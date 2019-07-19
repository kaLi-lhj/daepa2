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
from myweb.views import mainIndex, regAccount, modiAccount


urlpatterns = [
    # 127.0.0.1:8000/
    re_path(r'^$', mainIndex, name='index'),

    # 127.0.0.1:8000/admin/...
    
    path('admin/', admin.site.urls),
    re_path(r'^account/register/$', regAccount, name='reg_account'),
    re_path(r'^account/modified/$', modiAccount, name='modi_account'),

    # 127.0.0.1:8000/board/...
    re_path(r'^board/', include(r'board.urls')),

    # 127.0.0.1:8000/news/...
    re_path(r'^news/', include(r'news.urls')),

    # 127.0.0.1:8000/webtoon/...
    re_path(r'^webtoon/', include(r'webtoon.urls')),

    # 127.0.0.1:8000/dict/...
    re_path(r'^dict/', include(r'dict.urls')),

    # /error/
    re_path(r'^error/', include(r'error.urls')),
    
    re_path(r'^login')
]
# 정규 표현식
# [0-9] : 정수값 0 ~ 9 까지 패턴
# [a-z] : 소문자 a ~ z 까지 패턴
# [A-Z] : 대문자 A ~ Z 까지 패턴
# + : 1자리 이상
# {n} : n자리
# {n,m} : n 자리 ~ m 자리 까지
# (...) : () 안에 값을 저장 후 함수의 인자로 전달