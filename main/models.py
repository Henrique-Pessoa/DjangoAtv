from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum

class Funcao(Enum):
    TECNICO = 'Técnico'
    GERENTE = 'Gerente'
    OUTRO = 'Outro'

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    funcao = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.username
    
class Comentarios(models.Model):
    usuario = models.ForeignKey(CustomUser,related_name="usuario", on_delete=models.CASCADE,blank=False,null=False)
    comentario = models.CharField(max_length=2000,blank=False,null=False)
    data = models.DateField(default=timezone.now)

    def __str__(self):
        return self.comentario

class Equipamentos(models.Model):
    nome = models.CharField(max_length=150,blank=False,null=False)
    image = models.CharField(max_length=2000,blank=False,null=False)
    descricao = models.CharField(max_length=2000,blank=False,null=False)
    ativo = models.BooleanField(default=False,null=False,blank=False)
    comentarios = models.ManyToManyField(Comentarios, related_name="equipamentos")
    
    def __str__(self):
        return self.nome