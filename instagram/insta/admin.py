from django.contrib import admin
from .models import Insta  # models.py에 Insta를 등록했다는 것을 알려줌

# Register your models here.
admin.site.register(Insta) #Insta라는 table를 admin에 저장을 할 것임을 알려줌