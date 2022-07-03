import io
from keyword import kwlist
import tokenize as tk
import copy as cp


def run_code(code, variables):
    new_code = cp.copy(code)
    new_variables = cp.deepcopy(variables)

    for key in variables:
        new_code = new_code.replace(key, f'new_variables[\'{key}\']')

    res = []
    lines = new_code.split('\n')
    lines.append('\n')

    final_code = ''
    for i in range(len(lines)-1):
        add = '\n'
        if lines[i+1].startswith(' '):
            add += '    '

        add += 'res.append(cp.deepcopy(variables))\n'

        lines[i] += add


    for line in lines:
        final_code += line

    exec(final_code)

    return res


def separate(text):
    code = io.StringIO(text)
    res = tk.generate_tokens(code.readline)

    tokens = {'lines': [], 'names': [], 'numbers': [],
              'operators': [], 'keywords': []}

    tokens = []

    value_translator = {1: 'name', 2: 'number', 3: 'keyword', 54: 'operator'}
    for value in res:
        if value.type in [1, 2, 54] and '=' in value.line:
            if value.type == 1:
                if value.string not in kwlist:
                    value_type = 1

                else:
                    value_type = 3
            else:
                value_type = int(value.type)

            tokens.append({'line': value.line, 'name': value.string,
                        'type': value_translator[value_type]})

    print(tokens)

    return tokens


if __name__ == '__main__':
    text = '''numero = 1
array = ['teste', 1]
for i in range(3):
    array = 2 + i
'''

    code = io.StringIO(text)
    res = tk.generate_tokens(code.readline)

    variables = {'numero': None, 'array': None}
    res = run_code(text, variables)

    print(res)
