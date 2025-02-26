"""
URL configuration for primeiro_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from primeira_aplicacao import views #como temos o init na pasta da primeira aplicação, podemos importá-la como módulo


urlpatterns = [ #mapeamento das urls -> o mais certo é fazer o mapeamentos das urls na aplicação e depois incluir no projeto
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('primeira_aplicacao/', include('primeira_aplicacao.urls')) #para colocar a raiz no django, só colocamos a cadeia vazia. temos que importar o views para colocar o nosso view aqui na raiz
]
