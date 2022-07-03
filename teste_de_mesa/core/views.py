from email import contentmanager
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .models import CasoTeste, DicionarioParametros, ProgramaO, ProgramaP, TesteMesa, DadosTesteMesa, ValorParametro, ValoresTeste
from django.contrib import messages
from .forms import TesteMesaForm
from django.template.defaulttags import register


@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)


class IndexView(FormView):
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

            print(context['linhas'])

        return context


class TestesMesaView(TemplateView):
    template_name = 'historico_testes_mesa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['testes_de_mesa'] = TesteMesa.objects.filter(
            fk_caso_teste=self.kwargs.get('pk'))

        return context


class DadosView(TemplateView):
    template_name = 'historico_dados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['dados_teste_de_mesa'] = DadosTesteMesa.objects.get(
            id=self.kwargs.get('pk'))

        return context


class CasosTesteView(TemplateView):
    template_name = 'historico_casos_teste.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['casos_teste'] = CasoTeste.objects.all()

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

        context['valores_teste'] = ValoresTeste.objects.filter(
            id=self.kwargs.get('pk'))

        return context
