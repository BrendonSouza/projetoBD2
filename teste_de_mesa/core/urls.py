from django.urls import path
from .views import DicionarioView, IndexView, TestesMesaView, DadosView, CasosTesteView, ProgramaOView, ProgramaPView, ValoresParametrosView

# Este arquivo contem as rotas do programa

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('historico_testes_mesa/', TestesMesaView.as_view(),
         name='historico_testes_mesa'),
    path('historico_casos_teste/<int:pk>',
         CasosTesteView.as_view(), name='historico_casos_teste'),
    path('historico_dados/<int:pk>', DadosView.as_view(), name='historico_dados'),
    path('historico_dicionario/<int:pk>',
         DicionarioView.as_view(), name='historico_dicionario'),
    path('historico_valores_parametros/<int:pk>',
         ValoresParametrosView.as_view(), name='historico_valores_parametros'),
    path('historico_programa_p/<int:pk>',
         ProgramaPView.as_view(), name='historico_programa_p'),
    path('historico_programa_o/<int:pk>',
         ProgramaOView.as_view(), name='historico_programa_o'),
]
