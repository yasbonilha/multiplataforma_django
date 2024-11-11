from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#gerar uma httpRequest -> fase de processamento -> httpResponse
def index(request):
    variaveis = {
        'minha_primeira_variavel': "hello, variaveis depois de alterar o diretório",
    }
    #poderiamos acessar o modelo aqui, para acessar regras de negocio
    return render(request, 'primeira_aplicacao/index.html', context=variaveis) #esta mandando coisas para o template!!
