from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import CadUsuario

class acesso():
    def index(request):
        r = CadUsuario.objects.filter(dtnasc__lte='1988-02-18').order_by('dtnasc')
        return render(request, 'painel/index.html', { 'base' : r })
    
    def cadastro(request):
        return render(request, 'painel/cadastro.html', {})

