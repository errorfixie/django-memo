from django.contrib import admin
from .models import Memo, Usermemo
# Register your models here.



class MemoAdmin(admin.ModelAdmin):
    fields = ['title', 'contents',]
    list_display = ['title', 'contents', 'memodate', 'memoupdate']
    list_filter = ['memodate']
    search_fields = ['title']

class UsermemoAdmin(admin.ModelAdmin):
    list_display = ['userNUM', 'memoNUM']
    search_fields = ['userNUM']


admin.site.register(Memo, MemoAdmin)
admin.site.register(Usermemo,UsermemoAdmin)