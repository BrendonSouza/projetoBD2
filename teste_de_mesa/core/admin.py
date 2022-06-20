from django.contrib import admin
from .models import ProgramaO, ProgramaP, CasoTeste, DadosTesteMesa, TesteMesa, ValoresTeste


class TesteMesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_caso_teste', 'data_teste_mesa')


class ProgramaOAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_implementacao', 'codigo')


class ProgramaPAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_implementacao', 'codigo')


class DadosTesteMesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'linha', 'num_equacao', 'variavel_o',
                    'dado_hexa_o', 'variavel_p', 'dado_hexa_p', 'fk_teste_mesa')


class CasoTesteAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_programa_o', 'fk_programa_p')


class ValoresTesteAdmin(admin.ModelAdmin):
    list_display = ('id', 'parametro', 'valor', 'fk_caso_teste')


admin.site.register(ProgramaO, ProgramaOAdmin)
admin.site.register(ProgramaP, ProgramaPAdmin)
admin.site.register(DadosTesteMesa, DadosTesteMesaAdmin)
admin.site.register(CasoTeste, CasoTesteAdmin)
admin.site.register(TesteMesa, TesteMesaAdmin)
admin.site.register(ValoresTeste, ValoresTesteAdmin)
