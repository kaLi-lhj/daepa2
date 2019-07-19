from django.contrib import admin
from error.models import Error

# Register your models here.
class ErrorAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'code_name', 'note'
    )

admin.site.register(Error, ErrorAdmin)