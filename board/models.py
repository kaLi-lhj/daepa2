from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    context = models.TextField(default='')
    view_cnt = models.IntegerField(default=0)
    like_cnt = models.IntegerField(default=0)
    hate_cnt = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    no_del = models.BooleanField(default=False)
