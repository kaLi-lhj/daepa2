from django.urls import include, re_path
from . import views
app_name='dict'
urlpatterns = (
    re_path(r'^$', views.mainIndex, name='index'),
)
