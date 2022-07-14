# Importando bibliotecas
import io
from keyword import kwlist
import tokenize
import copy
# Importando todas as models necessárias
from .models import ProgramaO, ProgramaP, DadosTeste
from .models import CasoTeste, TesteDeMesa, Agrupamento, AgrupamentoIndex
# Importando função em outro arquivo local
from .prog import exec_script

# Função que gera os tokens, serapa, e grava no banco.
def save_test(prog_o, prog_p):
    # Convertendo string com código do programa p para StringIO
    script_string = io.StringIO(prog_p).readline
    # Gerando a lista de tokens com a biblioteca tokenize
    generate_tk = tokenize.generate_tokens(script_string)
    # Criando um dicionário com o número e seu tipo de dado.
    type_token_list = {1: 'name', 2: 'number', 3: 'keyword', 54: 'operator'}

    list_tokens = []
    # Criando instância do programa o com os dados já setados.
    o = ProgramaO(codigo_o=str(prog_o))
    # Salvando a instância com os dados direto no banco de dados.
    o.save()
    # Criando instância do programa p com os dados já setados.
    p = ProgramaP(codigo_p=str(prog_p))
    # Salvando a instância com os dados direto no banco de dados.
    p.save()
    # Criando uma instância da tabela caso teste já preenchida.
    ct = CasoTeste(programa_o=o, programa_p=p)
    # Salvando a instância.
    ct.save()
    # Criando a instância da tabela TesteDeMesa. 
    teste_mesa = TesteDeMesa(caso_teste=ct)
    # Salvando a instância.
    teste_mesa.save()
    # Percorrendo a lista de tokens gerados 
    for tk in generate_tk:
        # Verficando se o tipo do token está em [1,2,3] e se o token é o "=".
        if tk.type in [1, 2, 54] and '=' in tk.line:
            # Caso seja 1 verifica se pertence a lista de palavras chaves 
            # do python em kwlist adicionando 1 ou 3 no dict_value.
            if tk.type == 1:
                if tk.string not in kwlist: dict_value = 1
                else: dict_value = 3
            # Caso contrário dict_value reebe o token convertido para inteiro 
            else: dict_value = int(tk.type)      
            # Adicionando o teken e seus dados na nova lista de tokens formatados.   
            list_tokens.append({'name': tk.string, 'type': type_token_list[dict_value], 'line': tk.line})
    # Percorrendo a nova lista de tokens 
    for tk in list_tokens:
        # Verificando se é uma variável, pois as variáveis tem o tipo igual a name 
        if tk['type'] == 'name':
            # Buscando os dados no banco a partir da variável_p e o id doteste dessa variável.
            db_token = DadosTeste.objects.filter(variavel_p=tk['name'], teste=teste_mesa)
            # Verificando se a busca teve algum resultado.
            if not db_token:
                # Criando uma instância de DadosTeste, preenchendo e salvando no banco.
                dados = DadosTeste(teste=teste_mesa, linha=tk['line'], variavel_p=tk['name'], 
                    dado_hexa_p=tk['name'].encode('utf-8').hex())
                dados.save()
    # Criando uma nova dict. 
    code_tokens = dict()
    # Varrendo a lista de tokens e adicionando na dict code_tokens apenas as variáveis,
    # setando-as com None. 
    for tk in list_tokens:
        if tk['type'] == 'name':
            code_tokens[tk['name']] = None 

    # Criando novas variáveis a partir de prog_p e code_tokens. 
    code = prog_p
    variables = code_tokens
    # Criando uma cópia do código com um espaço para identação. 
    copy_script = copy.copy(code).replace('\t', '    ')
    exec_code = []
    end = ''
    # Separando o copy_script por linha. 
    lines = copy_script.split('\n')
    # Adicionando salto de linha no final.
    lines.append('\n')
    # Criando uma cópia de variables. 
    create_var = copy.deepcopy(variables)
    # Percorrendo lista create_var e adicionando em end a key setada com none. 
    for key, item in create_var.items():
        end += f'{key} = None\n'
    # Executando o script.
    lines = exec_script(lines, create_var, exec_code)
    # Adicionando o retorno da execução em end. 
    for line in lines:
        end += line
    # Executando o script no python.
    exec(end)

    res = exec_code
    # Percorrendo o resultado e salvando os dados no banco. 
    for i in range(len(res)):
        # Criando instância com os daos e salvando. 
        agrup = Agrupamento(teste=teste_mesa, linha=i)
        agrup.save()
        # Percorrendo só que agora salvando com base nas key. 
        for key in res[i]:
            # Criando instância com os daos e salvando. 
            agrup_index = AgrupamentoIndex(agrupamento=agrup, entrada=key, valor=res[i][key])
            agrup_index.save()
