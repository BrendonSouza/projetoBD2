from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .models import CasoTeste, DicionarioParametros, ProgramaO, ProgramaP, TesteMesa, DadosTesteMesa, ValorParametro
from django.contrib import messages
from .forms import TesteMesaForm
from django.template.defaulttags import register

# Este arquivo contém a definição das views do projeto


@register.filter
def get_value(dictionary, key):
    '''Retorna para o frontend o valor de um dicionário.
    '''

    return dictionary.get(key)


class IndexView(FormView):
    '''View para o index do site.
    '''

    template_name = 'index.html'
    form_class = TesteMesaForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        form.save_variables()
        messages.success(self.request, 'Código salvo com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao salvar')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if TesteMesa.objects.all():
            teste = TesteMesa.objects.latest('data_teste_mesa')
            context['dados'] = DadosTesteMesa.objects.filter(fk_teste=teste)

            dicionarios_parametros = DicionarioParametros.objects.filter(
                fk_teste=teste)

            context['linhas'] = dicionarios_parametros
            context['valores'] = ValorParametro.objects.all()

        return context


class TestesMesaView(TemplateView):
    '''View para o histórico do teste de mesa.
    '''

    template_name = 'historico_testes_mesa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['testes_de_mesa'] = TesteMesa.objects.all()

        return context


class DicionarioView(TemplateView):
    '''View para o histórico do dicionário.
    '''

    template_name = 'historico_dicionario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['dicionarios'] = DicionarioParametros.objects.filter(
            fk_teste=self.kwargs.get('pk'))

        return context


class ValoresParametrosView(TemplateView):
    '''View para o histórico dos valores do dicionário.
    '''

    template_name = 'historico_valores_parametros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['parametros'] = ValorParametro.objects.filter(
            container=self.kwargs.get('pk'))

        return context


class DadosView(TemplateView):
    '''View para o histórico dos dados do programa.
    '''

    template_name = 'historico_dados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['dados_teste_de_mesa'] = DadosTesteMesa.objects.filter(
            fk_teste=self.kwargs.get('pk'))

        return context


class CasosTesteView(TemplateView):
    '''View para o histórico dos casos de teste.
    '''

    template_name = 'historico_casos_teste.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['casos_teste'] = CasoTeste.objects.filter(
            id=self.kwargs.get('pk'))

        return context


class ProgramaOView(TemplateView):
    '''View para o histórico dos programas originais.
    '''

    template_name = 'historico_programa_o.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['programa_o'] = ProgramaO.objects.get(id=self.kwargs.get('pk'))

        return context


class ProgramaPView(TemplateView):
    '''View para o histórico dos programas digitados.
    '''

    template_name = 'historico_programa_p.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['programa_p'] = ProgramaP.objects.get(id=self.kwargs.get('pk'))

        return context
