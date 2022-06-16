from django.db import models


class ProgramaO(models.Model):
    data_implementacao = models.DateField()
    codigo = models.TextField()


class ProgramaP(models.Model):
    data_implementacao = models.DateField()
    codigo = models.TextField()


class DadosTesteMesa(models.Model):
    linha = models.CharField(max_length=5)
    num_equacao = models.CharField(max_length=1)
    variavel_o = models.CharField(max_length=100)
    dado_hexa_o = models.CharField(max_length=100)
    variavel_p = models.CharField(max_length=100)
    dado_hexa_p = models.CharField(max_length=100)


class CasoTeste(models.Model):
    fk_programa_o = models.ForeignKey(ProgramaO, on_delete=models.CASCADE)
    fk_programa_p = models.ForeignKey(ProgramaP, on_delete=models.CASCADE)


class TesteMesa(models.Model):
    data_teste_mesa = models.DateField()
    fk_caso_teste = models.ForeignKey(CasoTeste, on_delete=models.CASCADE)
    fk_dados_teste_mesa = models.ForeignKey(
        DadosTesteMesa, on_delete=models.CASCADE)


class ValoresTeste(models.Model):
    parametro = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    fk_caso_teste = models.ForeignKey(CasoTeste, on_delete=models.CASCADE)
