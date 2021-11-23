from django.urls import path
from .views import acesso

urlpatterns = [
    path('', acesso.index, name='index'),
    path('cadastro', acesso.cadastro, name='cadastro.index'),
]