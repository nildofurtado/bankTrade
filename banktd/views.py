from django.shortcuts import render
from django.http import HttpResponse

class acesso():
    def index(request):
        return HttpResponse('BankTrade')
    
    def cadastro(request):
        return render(request, 'painel/cadastro.html', {})

