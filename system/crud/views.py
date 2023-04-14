from django.shortcuts import render
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
  aproved = 1
  return render(request, 'crud/index.html',{
    "aproved": aproved
  })
  
def check_user(request):
  email_check = request.POST["email"]
  senha_check = request.POST["password"]
  users = User.objects.all()
  
  for user in users:
    if email_check == user.email and senha_check == user.password:
      return render(request, 'crud/home.html', {"user":user, "users": users})
  error = {
    "email": email_check,
    "error": "usuário não cadastrado"
  }
  return render(request, 'crud/index.html', error)