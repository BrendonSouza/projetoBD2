import io
from keyword import kwlist
import tokenize
import copy
from .models import ProgramaO, ProgramaP, DadosTeste
from .models import CasoTeste, TesteDeMesa, Agrupamento, AgrupamentoIndex
from .prog import exec_script

def save_test(prog_o, prog_p):

    script_string = io.StringIO(prog_p).readline
    generate_tk = tokenize.generate_tokens(script_string)
    type_token_list = {1: 'name', 2: 'number', 3: 'keyword', 54: 'operator'}
    list_tokens = []

    o = ProgramaO(codigo_o=str(prog_o))
    o.save()
    p = ProgramaP(codigo_p=str(prog_p))
    p.save()

    ct = CasoTeste(programa_o=o, programa_p=p)
    ct.save()
    
    teste_mesa = TesteDeMesa(caso_teste=ct)
    teste_mesa.save()
    
    for tk in generate_tk:
        if tk.type in [1, 2, 54] and '=' in tk.line:
            if tk.type == 1:
                if tk.string not in kwlist: dict_value = 1
                else: dict_value = 3
            else: dict_value = int(tk.type)            
            list_tokens.append({'name': tk.string, 'type': type_token_list[dict_value], 'line': tk.line})

    for tk in list_tokens:
        if tk['type'] == 'name':
            db_token = DadosTeste.objects.filter(variavel_p=tk['name'], teste=teste_mesa)

            if not db_token:
                dados = DadosTeste(teste=teste_mesa, linha=tk['line'], variavel_p=tk['name'], 
                    dado_hexa_p=tk['name'].encode('utf-8').hex())
                dados.save()

    code_tokens = dict()

    for tk in list_tokens:
        if tk['type'] == 'name':
            code_tokens[tk['name']] = None 


    code = prog_p
    variables = code_tokens

    copy_script = copy.copy(code).replace('\t', '    ')
    exec_code = []
    end = ''
    lines = copy_script.split('\n')
    lines.append('\n')
    create_var = copy.deepcopy(variables)

    for key, item in create_var.items():
        end += f'{key} = None\n'

    lines = exec_script(lines, create_var, exec_code)

    for line in lines:
        end += line

    exec(end)

    res = exec_code

    for i in range(len(res)):
        agrup = Agrupamento(teste=teste_mesa, linha=i)
        agrup.save()
        for key in res[i]:
            agrup_index = AgrupamentoIndex(agrupamento=agrup, entrada=key, valor=res[i][key])
            agrup_index.save()
