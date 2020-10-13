from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(verbose_name="별명", max_length=30)
    createdate = models.DateTimeField(verbose_name="생성일자", auto_now_add=True)

    def __str__(self):
        return self.nickname
