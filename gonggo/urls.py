from django.urls import include, re_path
from . import views

app_name='gonggo'
urlpatterns = (
    re_path(r'^$', views.mainIndex, name='index'),

    re_path(r'^main/$', views.Indexmain, name='mainindex'),

     # 공고 게시물(id)의 세부 정보
    re_path(r'^([0-9]+)/$', views.gonggoDetail, name='detail'),

    # 공고 추가
    re_path(r'^add/$', views.gonggoAdd, name='add'),

    # 공고 수정
    re_path(r'^update/([0-9]+)/$', views.gonggoUpdate, name='update'),

    # 공고 삭제
    re_path(r'^delete/([0-9]+)/$', views.gonggoDelete, name='delete'),

    # 공고 폼
    re_path(r'^form/$', views.gonggoForm, name='form'),
    
)
