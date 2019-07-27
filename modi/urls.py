from django.urls import include, re_path
from . import views
app_name='modi'
urlpatterns = (
    re_path(r'^$', views.mainIndex, name='index'),
)
