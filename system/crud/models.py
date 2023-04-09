from django.db import models

class User(models.Model):
  name = models.CharField(max_length=200)
  age = models.IntegerField()
  cpf = models.CharField(max_length=11)
  email = models.EmailField(max_length=75)
  password = models.CharField(max_length=200)
  def __str__(self):
    return self.name
  