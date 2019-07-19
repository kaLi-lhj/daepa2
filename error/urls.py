from django.urls import include, re_path
from . import views
app_name='error'
urlpatterns = [
    re_path(r'^([a-zA-Z]+)/$', views.errMessage, name='message')
]