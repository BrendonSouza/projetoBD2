from email import contentmanager
from django.views.generic import TemplateView
from .models import TesteMesa, DadosTesteMesa

class IndexView(TemplateView):
    template_name = 'index.html'


class HistoricoView(TemplateView):
    template_name = 'historico.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['testes_de_mesa'] = TesteMesa.objects.all()

        return context


class HistoricoDadosView(TemplateView):
    template_name = 'historico_dados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['dados_testes_de_mesa'] = DadosTesteMesa.objects.filter(id=self.kwargs.get('pk'))

        return context

if __name__ == '__main__':
    teste = HistoricoView()

    teste.get_context_data()