from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
  path('', views.index, name="index"),
  path('saveuser/', views.saveuser, name="saveuser"),
  path("registrer/", views.registrer, name="registrer"),
  path("save_cadastro/", views.save_cadastro, name="save_cadastro"),
  path("check_user/", views.check_user, name="check_user"),
  path("home/", views.home, name="home"),
]