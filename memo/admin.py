from django.contrib import admin
from .models import Memo, Usermemo
# Register your models here.

admin.site.register(Memo)
admin.site.register(Usermemo)