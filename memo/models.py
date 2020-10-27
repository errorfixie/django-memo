from django.db import models
import user.models
# Create your models here.
class Memo(models.Model):
    title = models.CharField(verbose_name="메모제목",max_length=30) #메모제목
    contents = models.TextField(verbose_name="메모내용", blank=True) # 메모내용
    memodate = models.DateTimeField(verbose_name="메모등록날짜", auto_now_add=True) #메모등록날짜
    memoupdate = models.DateTimeField(verbose_name="메모수정날짜", auto_now =True, null=True) #메모수정날짜

    def __str__(self):
        return self.contents

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


