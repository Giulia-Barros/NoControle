from django.db import models
from django.contrib.auth.models import User #Usuário autenticados no sistema

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Relação entre a tarefa e usuário, ou seja, cada tarefa pertence a um usuário.
    descricao = models.CharField(max_length=255)
    concluida = models.BooleanField(default=False)
    criada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao
