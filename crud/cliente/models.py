from django.db import models
from django.utils import timezone

SEXO_CHOICE = [
        ["F", "Feminino"],
        ["M", "Masculino"],
]

class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    sobre_nome = models.CharField(max_length=20)
    idade = models.IntegerField(default=0)
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=2, choices=SEXO_CHOICE)
    dt_nasc = models.DateTimeField(blank=True, null=True)
    dt_cad = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.dt_cad = timezone.now()
        self.save()

