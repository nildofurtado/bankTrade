from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class CadUsuario(models.Model):
    id = models.AutoField
    nome = models.CharField(max_length=150)
    dtnasc = models.DateField()
    cpf = models.IntegerField()
    email = models.EmailField()
    senha = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome