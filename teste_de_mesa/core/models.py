from django.db import models

# Este arquivo contem a definição dos modelos de dados do projeto
# nas classes definimos os atributos do modelo e seu tipo


class ProgramaO(models.Model):
    '''Modelo do programa original que será avaliado.
    '''

    data_implementacao = models.DateField(
        'Data de implementação', auto_now_add=True)
    codigo = models.TextField('Código')

    class Meta:
        verbose_name = 'Programa O'
        verbose_name_plural = 'Programas O'


class ProgramaP(models.Model):
    '''Modelo do programa digitado que será avaliado.
    '''

    data_implementacao = models.DateField(
        'Data de implementação', auto_now_add=True)
    codigo = models.TextField('Código')

    class Meta:
        verbose_name = 'Programa P'
        verbose_name_plural = 'Programas P'


class CasoTeste(models.Model):
    '''Modelo do caso de teste do teste de mesa.
    '''

    add = models.DateTimeField('Adicionado', auto_now_add=True)
    fk_programa_o = models.ForeignKey(ProgramaO, on_delete=models.CASCADE)
    fk_programa_p = models.ForeignKey(ProgramaP, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Caso de teste'
        verbose_name_plural = 'Casos de teste'


class TesteMesa(models.Model):
    '''Modelo do teste de mesa.
    '''

    data_teste_mesa = models.DateTimeField(
        'Data de criação', auto_now_add=True)
    fk_caso_teste = models.ForeignKey(CasoTeste, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Teste de mesa'
        verbose_name_plural = 'Testes de mesa'


class DicionarioParametros(models.Model):
    '''Modelo do dicionário de parâmetros do programa.
    '''

    linha = models.IntegerField()
    fk_teste = models.ForeignKey(TesteMesa, on_delete=models.CASCADE)


class ValorParametro(models.Model):
    '''Modelo do valor de parâmetros do programa.
    '''

    parametro = models.CharField(max_length=240, db_index=True)
    valor = models.CharField(max_length=240, db_index=True, null=True)
    container = models.ForeignKey(
        DicionarioParametros, db_index=True, on_delete=models.CASCADE)


class DadosTesteMesa(models.Model):
    '''Modelo dos dados do teste de mesa.
    '''

    add = models.DateTimeField('Adicionado', auto_now_add=True)
    linha = models.CharField('Linha', max_length=1000)
    variavel_p = models.CharField('Variável P', max_length=100)
    dado_hexa_p = models.CharField('Dado hexadecimal P', max_length=100)
    fk_teste = models.ForeignKey(TesteMesa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Dado teste de mesa'
        verbose_name_plural = 'Dados testes de mesa'
