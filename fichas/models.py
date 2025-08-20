from django.db import models

class Ficha(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
