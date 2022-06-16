from django.urls import path
from .views import IndexView, HistoricoView, HistoricoDadosView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('historico', HistoricoView.as_view(), name='historico'),
    path('historico_dados/<int:pk>', HistoricoDadosView.as_view(), name='historico_dados'),
]
