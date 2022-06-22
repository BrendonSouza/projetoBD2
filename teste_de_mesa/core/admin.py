from django.contrib import admin
from .models import ProgramaO, ProgramaP, CasoTeste, DadosTesteMesa, TesteMesa, ValoresTeste


@admin.register(TesteMesa)
class TesteMesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_teste_mesa', 'fk_caso_teste', 'fk_dados')


@admin.register(ProgramaO)
class ProgramaOAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_implementacao', 'codigo')


@admin.register(ProgramaP)
class ProgramaPAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_implementacao', 'codigo')


@admin.register(DadosTesteMesa)
class DadosTesteMesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'linha', 'num_equacao', 'variavel_o',
                    'dado_hexa_o', 'variavel_p', 'dado_hexa_p')

@admin.register(CasoTeste)
class CasoTesteAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_programa_o', 'fk_programa_p')


@admin.register(ValoresTeste)
class ValoresTesteAdmin(admin.ModelAdmin):
    list_display = ('id', 'parametro', 'valor', 'fk_caso_teste')
