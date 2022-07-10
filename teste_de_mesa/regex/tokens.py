import io
from keyword import kwlist
import tokenize
import copy
from .models import ProgramaO, ProgramaP, DadosTeste
from .models import CasoTeste, TesteDeMesa, Agrupamento, AgrupamentoIndex

def save_test(prog_o, prog_p):

# cod = 1
# lista = [1,2,3,4,5]
# codigo = lista[2]
# cod = 4

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

    for var, item in create_var.items():
        end += f'{var} = None\n'

    for i in range(len(lines)-1):
        code_run_line = '\n'
        if lines[i+1].startswith(' '):
            code_run_line += '    '
            code_run_line += 'for var, item in create_var.items():\n'
            code_run_line += '    '
            code_run_line += '    create_var[var] = eval(var)\n'
            code_run_line += '    '
            code_run_line += 'exec_code.append(copy.deepcopy(create_var))\n'

        else:
            code_run_line += 'for var, item in create_var.items():\n'
            code_run_line += '    create_var[var] = eval(var)\n'
            code_run_line += 'exec_code.append(copy.deepcopy(create_var))\n'

        lines[i] += code_run_line


    for line in lines:
        end += line

    exec(end)

    res = exec_code

    for i in range(len(res)):
        dicionario_parametros = Agrupamento(teste=teste_mesa, linha=i)
        dicionario_parametros.save()
        for key in res[i]:
            valores_teste = AgrupamentoIndex(agrupamento=dicionario_parametros, entrada=key, valor=res[i][key])
            valores_teste.save()






# import io
# from keyword import kwlist
# import tokenize
# import copy
# from .models import ProgramaO, ProgramaP, DadosTeste
# from .models import CasoTeste, TesteDeMesa, Agrupamento, AgrupamentoIndex

# def save_test(prog_o, prog_p):

#     o = ProgramaO(codigo_o=str(prog_o))
#     o.save()
#     p = ProgramaP(codigo_p=str(prog_p))
#     p.save()

#     ct = CasoTeste(programa_o=o, programa_p=p)
#     ct.save()
    
#     teste_mesa = TesteDeMesa(caso_teste=ct)
#     teste_mesa.save()

#     tokens = separate(prog_p)

#     for token in tokens:
#         if token['type'] == 'name':
#             db_token = DadosTeste.objects.filter(
#                 variavel_p=token['name'], teste=teste_mesa)

#             if not db_token:
#                 dados = DadosTeste(teste=teste_mesa,
#                     linha=token['line'], 
#                     variavel_p=token['name'], 
#                     dado_hexa_p=token['name'].encode('utf-8').hex())
#                 dados.save()

#     code_tokens = dict()

#     for token in tokens:
#         if token['type'] == 'name':
#             code_tokens[token['name']] = None 
#     res = start_script(prog_p, code_tokens)

#     for i in range(len(res)):
#         dicionario_parametros = Agrupamento(teste=teste_mesa, linha=i)
#         dicionario_parametros.save()
#         for key in res[i]:
#             valores_teste = AgrupamentoIndex(agrupamento=dicionario_parametros, entrada=key, valor=res[i][key])
#             valores_teste.save()

# def start_script(code, variables):
#     new_code = copy.copy(code)
#     new_code = new_code.replace('\t', '    ')
#     new_variables = copy.deepcopy(variables)

#     res = []
#     lines = new_code.split('\n')
#     lines.append('\n')

#     final_code = ''
#     for key, item in new_variables.items():
#         final_code += f'{key} = None\n'

#     for i in range(len(lines)-1):
#         add = '\n'
#         if lines[i+1].startswith(' '):
#             add += '    '
#             add += 'for key, item in new_variables.items():\n'
#             add += '    '
#             add += '    new_variables[key] = eval(key)\n'
#             add += '    '
#             add += 'res.append(copy.deepcopy(new_variables))\n'

#         else:
#             add += 'for key, item in new_variables.items():\n'
#             add += '    new_variables[key] = eval(key)\n'
#             add += 'res.append(copy.deepcopy(new_variables))\n'

#         lines[i] += add


#     for line in lines:
#         final_code += line

#     exec(final_code)

#     return res


# def separate(text):
#     code = io.StringIO(text)
#     res = tokenize.generate_tokens(code.readline)

#     tokens = []
#     type_translator = {1: 'name', 2: 'number', 3: 'keyword', 54: 'operator'}
#     for value in res:
#         if value.type in [1, 2, 54] and '=' in value.line:
#             if value.type == 1:
#                 if value.string not in kwlist:
#                     value_type = 1

#                 else:
#                     value_type = 3
#             else:
#                 value_type = int(value.type)

#             tokens.append({'line': value.line, 'name': value.string,
#                         'type': type_translator[value_type]})

#     return tokens
