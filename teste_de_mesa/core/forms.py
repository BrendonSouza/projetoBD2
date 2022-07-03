from django import forms
from .models import CasoTeste, DadosTesteMesa, DicionarioParametros, ProgramaO, ProgramaP, TesteMesa, ValorParametro, ValoresTeste
from .separator import separate, run_code


class TesteMesaForm(forms.Form):
    code_editor_o = forms.CharField(
        label='Codigo do programa O', widget=forms.Textarea())
    code_editor_p = forms.CharField(
        label='Codigo do programa P', widget=forms.Textarea())

    def save_variables(self):
        text_o = self.cleaned_data['code_editor_o']
        text_p = self.cleaned_data['code_editor_p']

        p_o = ProgramaO(codigo=text_o)
        p_o.save()
        p_p = ProgramaP(codigo=text_p)
        p_p.save()

        caso_teste = CasoTeste(fk_programa_o=p_o, fk_programa_p=p_p)
        caso_teste.save()
        teste_mesa = TesteMesa(fk_caso_teste=caso_teste)
        teste_mesa.save()

        tokens = separate(text_p)
        for token in tokens:
            if token['type'] == 'name':
                db_token = DadosTesteMesa.objects.filter(
                    variavel_p=token['name'], fk_teste=teste_mesa)

                if not db_token:
                    dados = DadosTesteMesa(fk_teste=teste_mesa,
                                            linha=token['line'], variavel_p=token['name'], dado_hexa_p=token['name'].encode('utf-8').hex())
                    dados.save()


        code_tokens = dict()

        for token in tokens:
            if token['type'] == 'name':
                code_tokens[token['name']] = None 
        res = run_code(text_p, code_tokens)

        for i in range(len(res)):
            dicionario_parametros = DicionarioParametros(fk_teste=teste_mesa, linha=i)
            dicionario_parametros.save()
            for key in res[i]:
                valores_teste = ValorParametro(container=dicionario_parametros, parametro=key, valor=res[i][key])
                valores_teste.save()
