import io
from keyword import kwlist
import tokenize as tk
import copy as cp


def run_code(code, variables):
    new_code = cp.copy(code)
    new_code = new_code.replace('\t', '    ')
    new_variables = cp.deepcopy(variables)

    res = []
    lines = new_code.split('\n')
    lines.append('\n')

    final_code = ''
    for key, item in new_variables.items():
        final_code += f'{key} = None\n'

    for i in range(len(lines)-1):
        add = '\n'
        if 'else' not in lines[i+1] and 'elif' not in lines[i+1]:
            n = 0
            if lines[i+1].startswith('    '):
                n = 1
                if lines[i+1].startswith('        '):
                    n = 2
                    if lines[i+1].startswith('            '):
                        n = 3

            add += '    ' * n
            add += 'for key, item in new_variables.items():\n'
            add += '    ' * n
            add += '    new_variables[key] = eval(key)\n'
            add += '    ' * n
            add += 'res.append(cp.deepcopy(new_variables))\n'

        lines[i] += add


    for line in lines:
        final_code += line

    exec(final_code)

    return res


def separate(text):
    code = io.StringIO(text)
    res = tk.generate_tokens(code.readline)

    tokens = []
    type_translator = {1: 'name', 2: 'number', 3: 'keyword', 54: 'operator'}
    for value in res:
        if value.type in [1, 2, 54] and '=' in value.line and not value.line.endswith(':'):
            if value.type == 1:
                if value.string not in kwlist:
                    value_type = 1

                else:
                    value_type = 3
            else:
                value_type = int(value.type)

            tokens.append({'line': value.line, 'name': value.string,
                        'type': type_translator[value_type]})

    return tokens


if __name__ == '__main__':
    text = '''bool1 = True
bool2 = False

if bool1 or bool2:
    numero = 1
    for i in range(5):
        numero += i
elif bool1 and bool2:
    numero = 2
else:
    numero = 3

'''

    code = io.StringIO(text)
    res = tk.generate_tokens(code.readline)

    variables = {'bool1': None, 'bool2': None, 'numero': None}
    res = run_code(text, variables)

    print(res)
