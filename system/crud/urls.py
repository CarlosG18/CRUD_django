from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
  path('', views.index, name="index"),
  path('saveuser/', views.saveuser, name="saveuser"),
]