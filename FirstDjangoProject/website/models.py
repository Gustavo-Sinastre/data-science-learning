from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=14)

    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.matricula}"
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} - {self.codigo}"