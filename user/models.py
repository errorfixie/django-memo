from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(verbose_name="별명", max_length=30,  blank=True)
    # createdate = models.DateTimeField(verbose_name="생성일자", auto_now_add=True)
    #  ** date_joined이라고 db에 등록되어있다

    first_name = None
    last_name = None
    # 쓸데없는 항목 삭제
    
    def __str__(self):
        return self.username
