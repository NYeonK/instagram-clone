from django.shortcuts import render

# Create your views here.

def login(request): 
 return render(request, 'login.html') 

def sign(request): 
 return render(request, 'sign-up.html') 