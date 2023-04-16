from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
  path('', views.index, name="index"),
  path('home/list_user/', views.List_userView.as_view(), name="list_user"),
  path('home/editar/', views.editar, name="editar"),
  path('home/delete/', views.DeleteView.as_view(), name="delete"),
  path("registrer/", views.registrer, name="registrer"),
  path("save_cadastro/", views.save_cadastro, name="save_cadastro"),
  path("check_user/", views.check_user, name="check_user"),
  path("home/", views.home, name="home"),
  path("home/delete/<int:id>/", views.delete_user, name="delete_user"),
  path("home/editar/<int:id>/", views.editar_user, name="editar_user"),
]