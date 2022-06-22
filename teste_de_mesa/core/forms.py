from django import forms
from .models import CasoTeste, DadosTesteMesa, PalavraReservada, ProgramaO, ProgramaP, TesteMesa


class TesteMesaForm(forms.Form):
    code_editor_o = forms.CharField(
        label='Codigo do programa O', widget=forms.Textarea())
    code_editor_p = forms.CharField(
        label='Codigo do programa P', widget=forms.Textarea())

    def save_code(self):
        text_o = self.cleaned_data['code_editor_o']
        text_p = self.cleaned_data['code_editor_p']

        lines_p = text_p.split('\n')

        p_o = ProgramaO(codigo=text_o)
        p_o.save()
        p_p = ProgramaP(codigo=text_p)
        p_p.save()

        caso_teste = CasoTeste(fk_programa_o=p_o, fk_programa_p=p_p)
        caso_teste.save()

        for line in lines_p:
            dados = DadosTesteMesa(linha=line)
            dados.save()
            teste_mesa = TesteMesa(fk_dados=dados, fk_caso_teste=caso_teste)
            teste_mesa.save()


