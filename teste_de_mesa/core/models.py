from django.db import models

class ProgramaO(models.Model):
    data_implementacao = models.DateField('Data de implementação', auto_now_add=True)
    codigo = models.TextField('Código')

    class Meta:
        verbose_name = 'Programa O'
        verbose_name_plural = 'Programas O'


class ProgramaP(models.Model):
    data_implementacao = models.DateField('Data de implementação', auto_now_add=True)
    codigo = models.TextField('Código')

    class Meta:
        verbose_name = 'Programa P'
        verbose_name_plural = 'Programas P'


class CasoTeste(models.Model):
    fk_programa_o = models.ForeignKey(ProgramaO, on_delete=models.CASCADE)
    fk_programa_p = models.ForeignKey(ProgramaP, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Caso de teste'
        verbose_name_plural = 'Casos de teste'


class ValoresTeste(models.Model):
    parametro = models.CharField('Parâmetro', max_length=100)
    valor = models.CharField('Valor', max_length=100)
    fk_caso_teste = models.ForeignKey(CasoTeste, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Valor caso de teste'
        verbose_name_plural = 'Valores casos de teste'


class DadosTesteMesa(models.Model):
    linha = models.CharField('Linha', max_length=5)
    num_equacao = models.CharField('Numero da equação', max_length=1)
    variavel_o = models.CharField('Variável O', max_length=100)
    dado_hexa_o = models.CharField('Dado hexadecimal O', max_length=100)
    variavel_p = models.CharField('Variável P', max_length=100)
    dado_hexa_p = models.CharField('Dado hexadecimal P', max_length=100)

    class Meta:
        verbose_name = 'Dado teste de mesa'
        verbose_name_plural = 'Dados testes de mesa'


class TesteMesa(models.Model):
    data_teste_mesa = models.DateField('Data de criação', auto_now_add=True)
    fk_caso_teste = models.ForeignKey(CasoTeste, on_delete=models.CASCADE)
    fk_dados = models.ForeignKey(DadosTesteMesa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Teste de mesa'
        verbose_name_plural = 'Testes de mesa'
