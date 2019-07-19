from django.urls import include, re_path
from . import views

app_name='board'
urlpatterns = [
    # 모든 게시물 리스트
    re_path(r'^$', views.mainIndex, name='index'),

    # 특정 게시물(id)의 세부 정보
    re_path(r'^([0-9]+)/$', views.boardDetail, name='detail'),

    # 게시물 추가
    re_path(r'^add/$', views.boardAdd, name='add'),

    # 게시물 수정
    re_path(r'^update/([0-9]+)/$', views.boardUpdate, name='update'),

    # 게시물 삭제
    re_path(r'^delete/([0-9]+)/$', views.boardDelete, name='delete'),

    re_path(r'^updown/$', views.boardLikeHate, name='like_hate'),
]