from django.urls import path
from .views import IndexView, HistoricoView, HistoricoDadosView,CasosTesteView, ProgramaOView, ProgramaPView, ValoresTesteView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('historico', HistoricoView.as_view(), name='historico'),
    path('historico_dados/<int:pk>', HistoricoDadosView.as_view(), name='historico_dados'),
    path('historico_casos_teste/<int:pk>', CasosTesteView.as_view(), name='historico_casos_teste'),
    path('historico_programa_p/<int:pk>', ProgramaPView.as_view(), name='historico_programa_p'),
    path('historico_programa_o/<int:pk>', ProgramaOView.as_view(), name='historico_programa_o'),
    path('historico_valores_teste/<int:pk>', ValoresTesteView.as_view(), name='historico_valores_teste'),
]
