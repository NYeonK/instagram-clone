from django.db import models
from django.shortcuts import render


# Create your models here.

# database에 바로 반영X, class 생성으로 table를 만들거라는 걸 알려줌. 
# class 생성 후, $ python manage.py makemigrations 명령어를 통해 models.py의 변경 사항을 감지해서 
# migration 폴더를 만들어 저장해줌. -> $ python manage.py migrate 명령어를 통해 폴더를 실행시켜 database에 적용!

class Insta(models.Model):
  title = models.CharField(max_length=200)
  writer = models.CharField(max_length=100)
  pub_date = models.DateTimeField()
  body = models.TextField()

  # admin에 Insta object라고 뜨는 이름 변경
  def __str__(self):
      return self.title # 글의 제목이 뜨도록 변경함.
  
  def summary(self): # 본문 요약
    return self.body[:100]