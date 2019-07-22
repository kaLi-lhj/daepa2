from django.contrib import admin
from myweb.models import Myweb

class MywebAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'password', 'first_name', 'last_name', 'email', 'job'
    )

admin.site.register(Myweb, MywebAdmin)