from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
  return render(request, 'crud/Index.html')

def saveuser(request):
  email = request.POST["email"]
  senha = request.POST["password"]
  return render(request, 'crud/home.html', 
  {
    "email": email,
    "senha": senha
  })

def registrer(request):
  return render(request, 'crud/registrer.html')

def save_cadastro(request):
  nome = request.POST["nome"]
  idade = request.POST["idade"]
  email = request.POST["email"]
  senha = request.POST["password"]
  user = User(name=nome,age=idade,email=email,password=senha)
  user.save()
  return render(request, 'crud/home.html')