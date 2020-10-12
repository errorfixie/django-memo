from django.db import models
import user.models
# Create your models here.
class Memo(models.Model):
    title = models.CharField(verbose_name="메모제목",max_length=30) #메모제목
    contents = models.TextField(verbose_name="메모내용") # 메모내용
    memodate = models.DateField(verbose_name="기사등록날짜", auto_now_add=True) #기사등록날짜

    def __str__(self):
        return self.title

class Usermemo(models.Model):
    userNUM = models.ForeignKey(
        user.models.User,
        verbose_name="사용자번호",
        on_delete=models.CASCADE,
    )
    memoNUM = models.ForeignKey(
        Memo,
        verbose_name="메모번호",
        on_delete=models.CASCADE,
    )

    