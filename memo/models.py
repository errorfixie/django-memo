from django.db import models
import user.models
# Create your models here.
class Memo(models.Model):
    title = models.CharField(verbose_name="메모제목",max_length=254, blank = True) #메모제목
    contents = models.TextField(verbose_name="메모내용", blank=True) # 메모내용
    memodate = models.DateTimeField(verbose_name="메모등록날짜", auto_now_add=True) #메모등록날짜
    memoupdate = models.DateTimeField(verbose_name="메모수정날짜", auto_now =True, blank=True) #메모수정날짜

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
    # models.CASCADE => 원본데이터가 삭제되면 자동으로 foreign키 받은 모델의 데이터도 삭제


