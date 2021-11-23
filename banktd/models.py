from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class CadUsuario(models.Model):
    id              = models.AutoField(primary_key=True)
    nome            = models.CharField(max_length=150)
    dtnasc          = models.DateField()
    cpf             = models.IntegerField()
    email           = models.EmailField()
    senha           = models.CharField(max_length=200)
    created_date    = models.DateTimeField(default=timezone.now)
    updated_date    = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
    
class DadosAgencia(models.Model):
    id              = models.AutoField(primary_key=True)
    NomeAgencia     = models.CharField(max_length=150)
    NumAgencia      = models.IntegerField()
    EstadoAgencia   = models.CharField(max_length=150)
    Created_date    = models.DateTimeField(default=timezone.now)
    Updated_date    = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.NomeAgencia
       
class DadosTipoConta(models.Model):
    id              = models.AutoField(primary_key=True)
    NomeTipoConta   = models.CharField(max_length=50)
    NumTipoConta    = models.IntegerField()
    Created_date    = models.DateTimeField(default=timezone.now)
    Updated_date    = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.NomeTipoConta
    
class CadContaUsuario(models.Model):
    id              = models.AutoField(primary_key=True)
    idusuario       = models.OneToOneField(CadUsuario, on_delete=models.CASCADE)
    Agencia         = models.IntegerField()
    Conta           = models.IntegerField()
    Tipo            = models.OneToOneField(DadosTipoConta, on_delete=models.CASCADE)
    Created_date    = models.DateTimeField(default=timezone.now)
    Updated_date    = models.DateTimeField(blank=True, null=True)
    