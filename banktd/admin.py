from django.contrib import admin
from .models import CadUsuario, DadosTipoConta, DadosAgencia, CadContaUsuario
# Register your models here.

admin.site.register(CadUsuario)
admin.site.register(DadosTipoConta)
admin.site.register(DadosAgencia)
admin.site.register(CadContaUsuario)