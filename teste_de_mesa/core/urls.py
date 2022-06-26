from django.urls import path
from .views import IndexView, TestesMesaView, DadosView,CasosTesteView, ProgramaOView, ProgramaPView, ValoresTesteView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('historico_casos_teste/', CasosTesteView.as_view(), name='historico_casos_teste'),
    path('historico_testes_mesa/<int:pk>', TestesMesaView.as_view(), name='historico_testes_mesa'),
    path('historico_dados/<int:pk>', DadosView.as_view(), name='historico_dados'),
    path('historico_programa_p/<int:pk>', ProgramaPView.as_view(), name='historico_programa_p'),
    path('historico_programa_o/<int:pk>', ProgramaOView.as_view(), name='historico_programa_o'),
    path('historico_valores_teste/<int:pk>', ValoresTesteView.as_view(), name='historico_valores_teste'),
]
