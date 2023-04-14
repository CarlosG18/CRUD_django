# CRUD_django
Desenvolvendo um crud simples com django-Python + Desafio: Login Form CSS (rocketseat) - modificado

## usando o sistema de autenticação do Django
- Objetos User: você não precisa criar um model para user. só fazer a importação:

'''python
from django.contrib.auth.models import User
'''

- para criar um user basta usar o metodo `User.objects.create_user(<nome_usuario>, <senha>, <email>, <primeiro_nome>, <ultimo_nome>)`

- para mudar senha `.set_password()`

### autenticar usuários

- para realizar a autentificação use:
'''python
from django.contrib.auth import authenticate

user = authenticate(username="john", password="secret")
if user is not None:
    # foi autenticado com sucesso!
    ...
else:
    # Nao foi autenticado!
    ...
'''
