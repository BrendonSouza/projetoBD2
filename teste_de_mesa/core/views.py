from django.views.generic import TemplateView
from .models import CasoTeste, ProgramaO, ProgramaP, TesteMesa, DadosTesteMesa, ValoresTeste


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

        context['dados_testes_de_mesa'] = DadosTesteMesa.objects.filter(
            fk_teste_mesa=self.kwargs.get('pk'))

        return context


class CasosTesteView(TemplateView):
    template_name = 'historico_casos_teste.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['casos_teste'] = CasoTeste.objects.filter(
            fk_teste_mesa=self.kwargs.get('pk')
        )

        return context


class ProgramaOView(TemplateView):
    template_name = 'historico_programa_o.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['programa_o'] = ProgramaO.objects.get(id=self.kwargs.get('pk'))

        return context


class ProgramaPView(TemplateView):
    template_name = 'historico_programa_p.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['programa_p'] = ProgramaP.objects.get(id=self.kwargs.get('pk'))

        return context


class ValoresTesteView(TemplateView):
    template_name = 'historico_valores_teste.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['valores_teste'] = ValoresTeste.objects.filter(id=self.kwargs.get('pk'))

        return context


