from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
  return render(request, 'crud/Index.html')