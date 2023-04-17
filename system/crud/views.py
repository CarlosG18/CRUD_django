from django.shortcuts import render
# from .models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.hashers import check_password

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
  if request.method == "POST":
    username = request.POST["nome"]
    senha_check = request.POST["password"]
    user = authenticate(username=username, password=senha_check)

    if user is not None:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect(reverse('crud:home'))
      else:
        error = {
          "error":"usuário inativo"
        }
    else:
      error = {
        "error":"usuário ou senha incorretos!"
      }
  return render(request, 'crud/Index.html', error)

@login_required(login_url='/crud/')
def home(request):
  return render(request, 'crud/home.html')
  
class List_userView(generic.ListView):
  template_name = "crud/list_user.html"
  context_object_name = "list"
  def get_queryset(self):
    return User.objects.all()
    
class DeleteView(generic.ListView):
  template_name = "crud/delete.html"
  context_object_name = "users"
  
  def get_queryset(self):
    return User.objects.all()

def editar(request):
  return render(request, "crud/editar.html")
    
def delete_user(request, id):
  User.objects.filter(id=id).delete()
  users = User.objects.all()
  contagem = users.count()
  return render(request, "crud/delete.html", {"users": users, "cont": contagem})

def editar_user(request, id):
  new_username = request.POST["new_name"]
  new_email = request.POST["new_email"]
  password_check = request.POST["password"]
  
  user = User.objects.get(id=id)
  
  if check_password(password_check,user.password):
    user.username = new_username
    user.email = new_email
    user.save()
  
  return HttpResponseRedirect(reverse('crud:editar'))


# @login_required
# def logout(request):
#   logout(request)
#   return HttpResponseRedirect(reverse('crud:index'))