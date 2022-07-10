from django.db import models

class Employee(models.Model):
    seu_codigo = models.CharField(max_length=100)

class ProgramaO(models.Model):
    dt_codificacao = models.DateTimeField(auto_now_add=True)
    codigo_o = models.CharField(max_length=1000)

class ProgramaP(models.Model):
    dt_codificacao = models.DateTimeField(auto_now_add=True)
    codigo_p = models.CharField(max_length=1000)

class CasoTeste(models.Model):
    data_caso_teste = models.DateTimeField(auto_now_add=True)
    programa_o = models.ForeignKey(ProgramaO, on_delete=models.CASCADE)
    programa_p = models.ForeignKey(ProgramaP, on_delete=models.CASCADE)

class TesteDeMesa(models.Model):
    data_teste = models.DateTimeField(auto_now_add=True)
    caso_teste = models.ForeignKey(CasoTeste, on_delete=models.CASCADE)

class DadosTeste(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    linha = models.CharField(max_length=1000)
    variavel_p = models.CharField(max_length=100)
    dado_hexa_p = models.CharField(max_length=100)
    teste = models.ForeignKey(TesteDeMesa, on_delete=models.CASCADE)

class Agrupamento(models.Model):
    linha = models.IntegerField()
    teste = models.ForeignKey(TesteDeMesa, on_delete=models.CASCADE)

class AgrupamentoIndex(models.Model):
    entrada = models.CharField(max_length=240, db_index=True)
    valor = models.CharField(max_length=240, db_index=True, null=True)
    agrupamento = models.ForeignKey(Agrupamento, db_index=True, on_delete=models.CASCADE)