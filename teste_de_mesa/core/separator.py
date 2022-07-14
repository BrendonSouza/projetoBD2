import io
from keyword import kwlist
import tokenize as tk
import copy as cp
import re

# Este módulo contem as funções para a separação dos tokens e
# execução do código


def run_code(code, variables):
    '''Executa um código em python e salva os valores de cada
    variável em cada linha do código.\n
    Parâmetros:\n
        code (str) - código em formato string que será executado.\n
        variables (dict) - dicionário com as variáveis e seus valores iniciais.\n

    Retorno:\n
        res (list) - lista com os dicionários de cada linha contendo as variaveis
        e seus respectivos valores.
    '''

    # Remove as linhas vazias do código
    new_code = ''
    for line in code.splitlines():
        if re.match(r'^\s*$', line):
            continue

        new_code += '\n' + line

    # Substitui as tabulações poe espaços para
    # não dar conflito
    new_code = new_code.replace('\t', '    ')

    # Cria uma cópia do dicionário de variáveis para
    # não modificá-lo por referência
    new_variables = cp.deepcopy(variables)

    # Separa as linhas do código e adiciona ao fim uma linha vazia para
    # evitar problemas com a verificação
    res = []
    lines = new_code.split('\n')
    lines.append('\n')

    # Inicializa o código final que será executado com a definição
    # das variáveis de modo que todas estejam definidas quando
    # precisar pegar seus valores
    final_code = ''
    for key, item in new_variables.items():
        final_code += f'{key} = {item}\n'

    # Inicia o tratamento para pegar os valores a cada linha de código
    for i in range(len(lines)-1):
        add = '\n'

        # Verifica se há algum else ou elif, caso exista vai para a próxima iteração
        if 'else' not in lines[i+1] and 'elif' not in lines[i+1]:

            # Trata as tabulações no código que será adicionado
            n = 0
            if lines[i+1].startswith('    '):
                n = 1
                if lines[i+1].startswith('        '):
                    n = 2
                    if lines[i+1].startswith('            '):
                        n = 3

            # Captura o valor de cada variável no código
            add += '    ' * n
            add += 'for key, item in new_variables.items():\n'
            add += '    ' * n
            add += '    new_variables[key] = eval(key)\n'
            add += '    ' * n
            add += 'res.append(cp.deepcopy(new_variables))\n'

        lines[i] += add

    # Junta todas as linhas para o código final
    for line in lines:
        final_code += line

    # Executa o código final.
    exec(final_code)

    return res


def separate(text):
    '''Separa todos os tokens do código passado como parâmetro.\n
    Parâmetros:\n
        text (str) - código em formato string.\n

    Retorno:\n
        tokens (list) - lista com os dicionários de cada token.
    '''

    # Gera os tokens do código
    code = io.StringIO(text)
    res = tk.generate_tokens(code.readline)

    # Define um tradutor para melhorar o entendimento dos tokens desejados
    tokens = []
    type_translator = {1: 'name', 2: 'number', 3: 'keyword', 54: 'operator'}

    # Realiza a filtragem para cada token e cria o seu dicionário
    for value in res:

        # Verifica se há uma atribuição na linha e se um nome é uma palavra
        # reservada do python e realiza a classificação do token de acordo
        if value.type in [1, 2, 54] and '=' in value.line and not value.line.endswith(':'):
            if value.type == 1:
                if value.string not in kwlist:
                    value_type = 1

                else:
                    value_type = 3
            else:
                value_type = int(value.type)

            # Adiciona o dicionário do token com seus valores desejados
            # na lista de tokens que será retornada
            tokens.append({'line': value.line, 'name': value.string,
                           'type': type_translator[value_type]})

    return tokens
