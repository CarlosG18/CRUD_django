# CRUD_django
Desenvolvendo um crud simples com django-Python + Desafio: Login Form CSS (rocketseat) - modificado

## aprendendo mais sobre templates do django
***gerando html dinamicamente***

- **variavies**: para usar variaveis no arquivo html deve-se coloca-los dentro de `{{ variavel }}`

- **etiquetas (tags)**: as tags são ultilizadas com o uso de `{% tag %}`. exemplos de tags:

```python
{% csrf_token %}
{% if user.is_authenticated %}
{% for i in range(5) %}
```

- **filtros(filters)**: os filtros transformam os valores da variaveis

- herança de modelos:
você pode criar um modelo base e exporta em outros arquivos

- para exportar uma base html basta usar a seguinte expressão no topo do arquivo html:

```python
{% extends "./base.html" %}
```

- você pode criar blocos para otimizar sua pagina html:

```python
{% block <nome do bloco> %}{% endblock %}
```

