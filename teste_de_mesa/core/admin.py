from django.contrib import admin
from .models import ProgramaO, ProgramaP, CasoTeste, DadosTesteMesa, TesteMesa, ValoresTeste


class ProgramaOAdmin(admin.ModelAdmin):
    list_display = ('data_implementacao', 'codigo')


class ProgramaPAdmin(admin.ModelAdmin):
    list_display = ('data_implementacao', 'codigo')


class DadosTesteMesaAdmin(admin.ModelAdmin):
    list_display = ('linha', 'num_equacao', 'variavel_o',
                    'dado_hexa_o', 'variavel_p', 'dado_hexa_p')


class CasoTesteAdmin(admin.ModelAdmin):
    list_display = ('fk_programa_o', 'fk_programa_p')


class TesteMesaAdmin(admin.ModelAdmin):
    list_display = ('data_teste_mesa', 'fk_caso_teste', 'fk_dados_teste_mesa')


class ValoresTesteAdmin(admin.ModelAdmin):
    list_display = ('parametro', 'valor', 'fk_caso_teste')


admin.site.register(ProgramaO, ProgramaOAdmin)
admin.site.register(ProgramaP, ProgramaPAdmin)
admin.site.register(DadosTesteMesa, DadosTesteMesaAdmin)
admin.site.register(CasoTeste, CasoTesteAdmin)
admin.site.register(TesteMesa, TesteMesaAdmin)
admin.site.register(ValoresTeste, ValoresTesteAdmin)
