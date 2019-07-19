from django.urls import include, re_path
from . import views
app_name='news'
urlpatterns = (
    re_path(r'^$', views.mainIndex, name='index'),
)
