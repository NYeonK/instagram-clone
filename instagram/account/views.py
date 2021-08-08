import django
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  
# 로그인과 회원가입을 도와주는 form
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# 로그인
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data = request.POST)
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = authenticate(request=request, username=username, password=password)
      if user is not None:
        login(request, user)
    return redirect("profile")

  else:
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

# 로그아웃
def logout_view(request):
  logout(request)
  return redirect("home")

# 회원가입
def register_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
    return redirect("home")

  else:
    form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})


def profile(request):
  return render (request, 'profile.html')
  
