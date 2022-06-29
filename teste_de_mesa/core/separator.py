import io
from keyword import kwlist
import tokenize as tk


def separate(text):
    code = io.StringIO(text)
    res = tk.generate_tokens(code.readline)

    tokens = {'lines': [], 'names': [], 'numbers': [],
              'operators': [], 'keywords': []}

    tokens = []
    for value in res:
        value_translator = {1:'name', 2:'number', 3:'keyword', 54:'operator'}

        if value.type in [60, 0, 4]:
            continue

        if value.type == 1:
            if value.string not in kwlist:
                value_type = 1

            else:
                value_type = 3
        else:
            value_type = int(value.type)
        
        tokens.append({'line': value.line, 'name': value.string, 'type': value_translator[value_type]})

    return tokens