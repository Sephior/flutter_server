from django.db import models

# Create your models here.

class Task(models.Model):
    # 할 일의 고유 id primary_key=True
    # AutoField는 자동 생성된 모델
    id = models.AutoField(primary_key=True)
    # 아무 값도 없을 때 null, 최대 길이 400의 char모델
    work = models.CharField(max_length=400, default='null')
    # 참 거짓으로 나뉘는 모델
    isComplete = models.BooleanField(default=False)