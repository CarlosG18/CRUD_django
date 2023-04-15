
from django.shortcuts import render
# from .models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def index(request):
  return render(request, 'crud/Index.html')

def registrer(request):
  if request.method == "GET":
    return render(request, 'crud/registrer.html', {"error_username": None, "error_email": None})

def save_cadastro(request):
  if request.method == "GET":
    return render(request, 'crud/registrer.html')
  else:
    nome = request.POST["nome"]
    email = request.POST["email"]
    senha = request.POST["password"]
    
    test_username = User.objects.filter(username=nome)
    test_email = User.objects.filter(email=email)
    
    if test_username:
      return render(request, 'crud/registrer.html', {
        "error_username": "username não disponível!"
      })
    elif test_email:
      return render(request, 'crud/registrer.html', {
        "error_email": "email já cadastrado!"
      })
    else:
      user = User.objects.create_user(username=nome, email=email, password=senha)
      user.save()
      return render(request, 'crud/Index.html',{
      "aproved": "usuário cadastrado com sucesso!"
      })
  
def check_user(request):
  if request.method == "GET":
    return render(request, 'crud/index.html', {"error": None})
  else:
    username = request.POST["nome"]
    senha_check = request.POST["password"]
    user = authenticate(username=username, password=senha_check)

    if user is not None:
      return HttpResponseRedirect(reverse('crud:home'))
    else:
      error = {
        "error": "usuário ou senha invalidos"
      }
      return render(request, 'crud/Index.html', error)

def home(request):
  return render(request, 'crud/home.html')