from django.db import models

# Create your models here.

class Employee(models.Model):
    seu_codigo = models.CharField(max_length=100)

class Programas(models.Model):
    programa_p = models.CharField(max_length=1000)
    programa_o = models.CharField(max_length=1000)

class ProgramaO(models.Model):
    dt_codificacao = models.DateField()
    codigo_o = models.CharField(max_length=1000)

class ProgramaP(models.Model):
    dt_codificacao = models.DateField()
    codigo_p = models.CharField(max_length=1000)

class TesteMesa(models.Model):
    dt_teste_mesa = models.DateField()

# class CasoTeste(models.Model):
#     id_programa_o = 
#     id_programa_p = 

class DadosTm(models.Model):
    # id_teste_mesa
    linha = models.IntegerField()
    variavel_o = models.CharField(max_length=50)
    variavel_p =  models.CharField(max_length=50)
    codigo_linha = models.CharField(max_length=1000)
    # num_equacao = 
    # valor_o =
    # dado_hexa_o = 
    # valor_p =
    # dado_hexa_p =