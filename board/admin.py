from django.contrib import admin
from board.models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'sub_title', 'author', 'context',
        'view_cnt', 'like_cnt', 'hate_cnt', 'create_date',
        'update_date', 'no_del'
    )

admin.site.register(Board, BoardAdmin)