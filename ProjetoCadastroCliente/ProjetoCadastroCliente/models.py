from django.db import models

class Cliente(models.Model):
    
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    telefone = models.CharField(
        max_length=15,
        null=False,
        blank=False
    )
    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    cidade = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    estado = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    valorcredito = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    objetos = models.Manager()