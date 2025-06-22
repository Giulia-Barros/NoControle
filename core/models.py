from doctest import master

from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Aitvo', default=True)

    class Meta:
        abstract = True

