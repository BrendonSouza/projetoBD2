from django import forms
from .models import CasoTeste, DadosTesteMesa, DicionarioParametros, ProgramaO, ProgramaP, TesteMesa, ValorParametro
from .separator import separate, run_code


class TesteMesaForm(forms.Form):
    '''Formulário para a execução do teste.
    '''

    # Definição dos atributos do formulário
    code_editor_o = forms.CharField(
        label='Codigo do programa O', widget=forms.Textarea())
    code_editor_p = forms.CharField(
        label='Codigo do programa P', widget=forms.Textarea())

    def save_variables(self):
        # Recuperação do valores do formulário
        text_o = self.cleaned_data['code_editor_o']
        text_p = self.cleaned_data['code_editor_p']

        # Cria as instancias dos programas o e p e os salva no banco de dados
        p_o = ProgramaO(codigo=text_o)
        p_o.save()
        p_p = ProgramaP(codigo=text_p)
        p_p.save()

        # Cria das instancias do teste de mesa e do caso de teste e salva
        # no banco de dados
        caso_teste = CasoTeste(fk_programa_o=p_o, fk_programa_p=p_p)
        caso_teste.save()
        teste_mesa = TesteMesa(fk_caso_teste=caso_teste)
        teste_mesa.save()

        # Separa os tokens dos códigos e salva seus dados no banco de dados
        tokens = separate(text_p)
        for token in tokens:
            # Cria a instancia dos dados e o salva no banco
            dados = DadosTesteMesa(fk_teste=teste_mesa, linha=token['line'], variavel_p=token['name'],
                                   dado_hexa_p=token['name'].encode('utf-8').hex())
            dados.save()

        # Para cada token que representa uma variável,
        # o adiciona no dicionario para executar o código
        code_tokens = dict()
        for token in tokens:
            if token['type'] == 'name':
                code_tokens[token['name']] = None

        # Executa o código
        res = run_code(text_p, code_tokens)

        # Após a execução do código, cria os dicionários
        # no banco de salva seus valores
        for i in range(len(res)):

            # Cria o dicionário e o salva no banco
            dicionario_parametros = DicionarioParametros(
                fk_teste=teste_mesa, linha=i)
            dicionario_parametros.save()

            # Cria a variável e a salva no banco para cada linha
            for key in res[i]:
                valores_teste = ValorParametro(
                    container=dicionario_parametros, parametro=key, valor=res[i][key])
                valores_teste.save()
