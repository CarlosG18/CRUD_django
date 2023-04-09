from django.db import models

class User(models.Model):
  name = models.CharField(max_length=200)
  age = models.IntegerField()
  email = models.EmailField(max_length=75)
  password = models.CharField(max_length=8)