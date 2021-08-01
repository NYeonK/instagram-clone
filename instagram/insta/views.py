from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Insta 

# Create your views here.
def home(request):
  instas = Insta.objects.all()  # Insta에 있는 데이터를 다 가져와서 instas에  저장
  return render(request, 'home.html', {'instas':instas})

def detail(request, id):
  insta = get_object_or_404(Insta, pk=id) # 서버에 존재하지않는 페이지에 대한 요청이 있을 경우 사이트가 이 코드를 제공
  return render(request, 'detail.html', {'insta':insta})

def new(request):
  return render(request, 'new.html')

def create(request):
  new_insta = Insta()
  new_insta.title = request.POST['title']
  new_insta.writer = request.POST['writer']
  new_insta.body = request.POST['body']
  new_insta.pub_date = timezone.now()
  new_insta.save()
  
  # 기능을 수행하고 원래 페이지로 돌아가기 때문에 render대신, redirect 사용
  return redirect('detail', new_insta.id)